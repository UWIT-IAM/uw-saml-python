"""UW-specific adapter for the python3-saml package."""
from onelogin.saml2.auth import OneLogin_Saml2_Auth
from .idp.uw import UwIdp
from .sp import Config
from .idp import attribute
from logging import getLogger
logger = getLogger(__name__)


def login_redirect(entity_id='', acs_url='', return_to='/', force_authn=False,
                   idp=UwIdp, two_factor=False):
    sp = Config(entity_id, acs_url)
    config = sp.config(idp, two_factor=two_factor)
    auth = OneLogin_Saml2_Auth(sp.request(), old_settings=config)
    return auth.login(return_to=return_to, force_authn=force_authn)


def process_response(post, entity_id, acs_url, idp=UwIdp, two_factor=False):
    sp = Config(entity_id, acs_url)
    config = sp.config(idp, two_factor=two_factor)
    auth = OneLogin_Saml2_Auth(sp.request(post), old_settings=config)
    auth.process_response()
    errors = auth.get_errors()
    if errors:
        raise SamlResponseException(auth.get_last_error_reason())
    attribute_data = dict(attribute.map(auth.get_attributes(), idp=idp))
    logger.info(attribute_data)
    return attribute_data


class SamlResponseException(Exception):
    """Exception to raise when a SAMLResponse can't be validated."""
