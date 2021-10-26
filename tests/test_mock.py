import pytest
import uw_saml2


@pytest.fixture(autouse=True)
def flick_mock_flag(monkeypatch):
    monkeypatch.setattr("uw_saml2.python3_saml.MOCK", True)


def test_login_redirect():
    expected = (
        "/mock-login?return_to=%2F&force_authn=False"
        "&idp=urn%3Amace%3Aincommon%3Awashington.edu"
    )
    assert uw_saml2.login_redirect() == expected


def test_process_response():
    post = {
        "idp": "urn:mace:incommon:washington.edu",
        "remote_user": "javerage@washington.edu",
        "uwnetid": "javerage",
    }
    expected = {"two_factor": False, **post}
    assert uw_saml2.process_response(post) == expected


def test_process_respose_error():
    post = {"idp": "badidp", "foo": "bar"}
    with pytest.raises(uw_saml2.SamlResponseError):
        uw_saml2.process_response(post)
