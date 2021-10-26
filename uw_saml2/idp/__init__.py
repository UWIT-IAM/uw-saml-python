class IdpConfig(object):
    """
    Idp base configuration with a common set of defaults that get
    overridden by subclasses.
    """

    entity_id = ""
    sso_url = ""
    sso_binding = "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"
    x509_cert = ""
    id_attribute = "urn:oid:1.3.6.1.4.1.5923.1.1.1.6"  # eppn
    mapped_id_attribute = "remote_user"
    attribute_map = {}
