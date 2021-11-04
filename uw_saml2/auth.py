"""UW-specific adapter for the python3-saml package."""
import cachelib
from .python3_saml import get_saml_authenticator
from .idp.uw import UwIdp
from .sp import Config, TWO_FACTOR_CONTEXT
from .idp import attribute
from logging import getLogger

logger = getLogger(__name__)

# For distributed environments, inject a distributed cache.
CACHE = cachelib.SimpleCache()


def login_redirect(
    entity_id=None,
    acs_url=None,
    return_to="/",
    force_authn=False,
    idp=UwIdp,
    two_factor=False,
):
    """
    Return a SAML request URL for redirecting to the Identity Provider (IdP).

    entity_id - The Service Provider (SP) Entity ID.
    acs_url - The SP endpoint the Identity Provider will post back to, known
        technically as the Assertion Consumer Service. This endpoint along
        with the Entity Id are registered with the IdP.
    return_to - The URL to send back to after authentication. This is known
        in a SAML request as 'RelayState'.
    force_authn - whether to force authentication even if the user has already
        authenticated against the IdP.
    idp - which IdP to use, defaulting to UW's IdP. Other IdPs of type
        uw_saml2.idp.IdpConfig can be added.
    two_factor - whether to ask for two-factor authentication. Asking for it
        doesn't mean you get it back on the response. You'll need to check
        there as well.
    """
    sp = Config(entity_id, acs_url)
    config = sp.config(idp, two_factor=two_factor)
    auth = get_saml_authenticator(sp.request(), old_settings=config)
    return auth.login(return_to=return_to, force_authn=force_authn)


def process_response(post, entity_id=None, acs_url=None, idp=UwIdp, two_factor=False):
    """
    Validate a SAML Response posted by the Identity Provider (IdP) and return
    its attributes as a dict.

    post - The post data to process.
    entity_id - The Service Provider (SP) Entity ID.
    acs_url - The SP endpoint the IdP posted back to. At this point entity_id
        and acs_url are used to validate a SAML Response.
    idp - The IdP to validate against.
    two_factor - whether we expect a 2FA response or not. If True then
        non-2FA authentication will raise a SamlResponseError. Another
        technique would be to leave this False and check the attribute we
        add to the attribute data returned.
    """
    sp = Config(entity_id, acs_url)
    config = sp.config(idp, two_factor=two_factor)
    auth = get_saml_authenticator(sp.request(post), old_settings=config)
    auth.process_response()
    errors = auth.get_errors()
    if errors:
        raise SamlResponseError(auth.get_last_error_reason())

    message_id = auth.get_last_message_id()
    if not CACHE.add(f"uw_saml2:response:message_id:{message_id}", True):
        raise SamlResponseError(f"SAML Replay of {message_id}")

    attribute_data = dict(attribute.map(auth.get_attributes(), idp=idp))

    authn_contexts = auth.get_last_authn_contexts()
    attribute_data["two_factor"] = TWO_FACTOR_CONTEXT in authn_contexts

    logger.info(f"{message_id}: {attribute_data}")
    return attribute_data


class SamlResponseError(Exception):
    """Exception to raise when a SAMLResponse can't be validated."""
