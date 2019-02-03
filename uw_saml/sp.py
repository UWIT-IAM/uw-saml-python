"""Service Provider configuration."""
from urllib.parse import urlparse
CERT = ''
KEY = ''


class Config(object):
    def __init__(self, entity_id, acs_url, cert=CERT, key=KEY):
        self.entity_id = entity_id
        self.acs_url = acs_url
        self.cert = cert
        self.key = key
    
    def request(self, post=None):
        post = post or {}
        parsed_url = urlparse(self.acs_url)
        return {
            'https': 'on',
            'http_host': parsed_url.netloc,
            'script_name': parsed_url.path,
            'post_data': post
        }

    def config(self, idp, two_factor=False):
        """Return config in a way that makes sense to OneLogin_Saml2_Auth."""
        data = {
            'strict': True,
            'idp': {
                'entityId': idp.entity_id,
                'singleSignOnService': {
                    'url': idp.sso_url,
                    'binding': idp.sso_binding
                },
                'x509cert': idp.x509_cert
            },
            'sp': {
                'entityId': self.entity_id,
                'assertionConsumerService': {
                    'url': sp.acs_url,
                    'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'
                },
                'x509cert': self.cert,
                'privateKey': self.key
            }
        }
        if two_factor:
            data.update({'security': {
                'requestedAuthnContext': ['https://refeds.org/profile/mfa'],
                'failOnAuthnContextMismatch': True
            }})
        return data