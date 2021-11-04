import uw_saml2
import uw_saml2.auth
import pytest
import mock
import os
import urllib.parse

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def test_login_redirect(mock_time_and_id):
    """Fix the time and check that the request still looks the same."""
    entity_id = "https://example.org/saml"
    acs_url = "https://example.org/saml/login"
    url = uw_saml2.login_redirect(
        entity_id=entity_id, acs_url=acs_url, return_to="/foo"
    )
    expected_url = (
        "https://idp.u.washington.edu/idp/profile/SAML2/Redirect/SSO?"
        "SAMLRequest=fVPBbqMwEL33KxD34ECjrdZKkGiiaiN1NwjoHvbm2pPEkrFZe9xk%2F35"
        "tmjap1IYL0pv3hvdmhrljvRpo5XGvG%2FjrweFNkhx7pR0dS4vUW00Nc9JRzXpwFDltq5"
        "%2BPtMimdLAGDTcq%2FSC6rmHOgUVpdBStV4v0YbO5r5q8uI3Ab7Au1BZpoI4E5zystUO"
        "mMYDT%2FPtkWkymsy6%2Fo7NvtJj9iaxV8C01w1G5RxwcJUSKIfPZgbm91Ds0OgPhI0iC"
        "661UQKKlgjQgpAWOpG03sVd9ynQvtQjC62GeX0mO%2Fui6elJv2i62qN4iLo12vgfbgn2"
        "RHJ6ax7M9OLJ%2BUJAZuyNxakSZndRpGfRJMo8IHcPb8ivFnFyyzrqB%2FgpG16vaKMn"
        "%2FjXh8HoztGX6dJ8%2FyEZFish2p1Gs3AJdbCSJ9b1MpZQ5LCwxhkaL1kCbkw8dPdwRi"
        "vKowAoQjJkvTD8xKFzcUgnA8JT2nvaQvVTiTBrbl1UvilEdegOvwOhgr4vLCLkF0lgXzx"
        "uJpSJ82f3VNrtgub97Kl79I%2BR8%3D&RelayState=%2Ffoo"
    )
    assert url == expected_url


def test_process_response(mock_time_and_id):
    """
    Take a once-valid SAML Response, mock the time to when it was valid,
    validate the response, and compare the attributes.
    """
    with open(os.path.join(BASEDIR, "samlresponse.txt")) as fd:
        post = dict(urllib.parse.parse_qsl(fd.read()))
    # set a time when this response was still valid
    mock_time_and_id.return_value = 1549304000
    entity_id = "https://samldemo.iamdev.s.uw.edu/saml"
    acs_url = "https://samldemo.iamdev.s.uw.edu/saml/login"
    attributes = uw_saml2.process_response(post, entity_id=entity_id, acs_url=acs_url)
    expected_attributes = {
        "affiliations": ["student", "member"],
        "eppn": "idtest55@washington.edu",
        "groups": ["u_jpf_test-saml"],
        "scoped_affiliations": ["student@washington.edu", "member@washington.edu"],
        "two_factor": False,
        "uwnetid": "idtest55",
    }
    assert attributes == expected_attributes


def test_process_response_replay(mock_time_and_id):
    with open(os.path.join(BASEDIR, "samlresponse.txt")) as fd:
        post = dict(urllib.parse.parse_qsl(fd.read()))
    # set a time when this response was still valid
    mock_time_and_id.return_value = 1549304000
    entity_id = "https://samldemo.iamdev.s.uw.edu/saml"
    acs_url = "https://samldemo.iamdev.s.uw.edu/saml/login"
    attributes = uw_saml2.process_response(post, entity_id=entity_id, acs_url=acs_url)
    with pytest.raises(uw_saml2.auth.SamlResponseError) as excinfo:
        attributes = uw_saml2.process_response(
            post, entity_id=entity_id, acs_url=acs_url
        )
    assert "replay" in str(excinfo.value).lower()


@pytest.fixture
def mock_time_and_id(monkeypatch):
    """Mock the two things guaranteed to be nondeterministic - date and id."""
    import onelogin.saml2.utils

    utils = "onelogin.saml2.utils.OneLogin_Saml2_Utils"
    mock_time = mock.MagicMock()
    mock_time.return_value = 1549302384
    monkeypatch.setattr(f"{utils}.now", mock_time)
    monkeypatch.setattr(f"{utils}.generate_unique_id", lambda: "FOOBAR123")
    uw_saml2.auth.CACHE.clear()
    return mock_time
