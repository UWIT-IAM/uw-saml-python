"""Just importing federated boosts our coverage."""
from uw_saml2.idp import federated


def test_cascadia_employee():
    id_attribute = 'urn:mace:washington.edu:dir:attribute-def:stu-validationID'
    assert federated.CascadiaEmployeeIdp.id_attribute == id_attribute


def test_scca_dynamic_entity_id():
    entity_id = 'https://example.com'
    scca = federated.SccaIdp(entity_id)
    assert scca.entity_id == entity_id
    assert scca.sso_url == entity_id
