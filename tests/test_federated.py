"""Just importing federated boosts our coverage."""
from uw_saml2.idp import federated, attribute
import pytest


def test_scca_dynamic_entity_id():
    entity_id = "https://example.com"
    scca = federated.SccaIdp(entity_id)
    assert scca.entity_id == entity_id
    assert scca.sso_url == entity_id
