"""Just importing federated boosts our coverage."""
from uw_saml2.idp import federated, attribute
import pytest


@pytest.mark.parametrize(
    "student,employee",
    [
        (["loser"], ["winner"]),
        (["winner"], None),
        (None, ["winner"]),
        ([], ["winner"]),
        (["winner"], []),
    ],
)
def test_cascadia_employee_attributes(student, employee):
    """
    Cascadia Employees should come across as such, but our test one comes
    through as a student. This checks that if either one is set, we get
    a value for remote_user. It's still entirely possible for student to
    win out.
    """
    prefix = "urn:mace:washington.edu:dir:attribute-def"
    attrs = {}
    if student is not None:
        attrs[f"{prefix}:stu-validationID"] = student
    if employee is not None:
        attrs[f"{prefix}:emp-validationID"] = employee
    mapped_attrs = dict(attribute.map(attrs, federated.CascadiaEmployeeIdp))
    assert mapped_attrs["remote_user"] == "winner"


def test_scca_dynamic_entity_id():
    entity_id = "https://example.com"
    scca = federated.SccaIdp(entity_id)
    assert scca.entity_id == entity_id
    assert scca.sso_url == entity_id
