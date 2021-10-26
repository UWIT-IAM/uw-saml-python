MOCK = False


def get_saml_authenticator(*args, **kwargs):
    if MOCK:
        from . import mock

        return mock.SamlAuthenticator(*args, **kwargs)
    else:
        from onelogin.saml2.auth import OneLogin_Saml2_Auth

        return OneLogin_Saml2_Auth(*args, **kwargs)
