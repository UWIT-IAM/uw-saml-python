"""Service Provider configuration."""
from urllib.parse import urlparse
import os

TWO_FACTOR_CONTEXT = "https://refeds.org/profile/mfa"


class Config(object):
    entity_id = ""
    acs_url = ""
    cert_file = ""
    key_file = ""
    _file_store = {}  # cache files we've read

    def __init__(self, entity_id=None, acs_url=None):
        if entity_id:
            self.entity_id = entity_id
        if acs_url:
            self.acs_url = acs_url

    def request(self, post=None):
        post = post or {}
        parsed_url = urlparse(self.acs_url)
        return {
            "https": "on",
            "http_host": parsed_url.netloc,
            "script_name": parsed_url.path,
            "post_data": post,
        }

    def _read_file(self, filename):
        if filename in self._file_store:
            return self._file_store[filename]
        if os.path.isfile(filename):
            with open(filename) as fd:
                filedata = fd.read()
            self._file_store[filename] = filedata
            return filedata
        return ""

    @property
    def cert(self):
        return self._read_file(self.cert_file)

    @property
    def key(self):
        return self._read_file(self.key_file)

    def config(self, idp, two_factor=False):
        """Return config in a way that makes sense to OneLogin_Saml2_Auth."""
        data = {
            "strict": True,
            "idp": {
                "entityId": idp.entity_id,
                "singleSignOnService": {"url": idp.sso_url, "binding": idp.sso_binding},
                "x509cert": idp.x509_cert,
            },
            "sp": {
                "entityId": self.entity_id,
                "assertionConsumerService": {
                    "url": self.acs_url,
                    "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST",
                },
                "x509cert": self.cert,
                "privateKey": self.key,
            },
        }
        if two_factor or getattr(idp, "two_factor", False):
            data.update(
                {
                    "security": {
                        "requestedAuthnContext": [TWO_FACTOR_CONTEXT],
                        "failOnAuthnContextMismatch": True,
                    }
                }
            )
        return data
