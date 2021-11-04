import urllib.parse
from random import random
from .idp import uw, federated

MOCK_LOGIN_URL = "/mock-login"


class SamlAuthenticator:
    def __init__(self, request, old_settings, *args, **kwargs):
        self.request = request
        self.idp = old_settings["idp"]["entityId"]
        self.errors = []

    def login(self, **kwargs):
        kwargs["idp"] = self.idp
        qs = urllib.parse.urlencode(kwargs)
        return f"{MOCK_LOGIN_URL}?{qs}"

    def process_response(self):
        idp = self.request["post_data"].get("idp")
        if idp != self.idp:
            self.errors.append(f"idp mismatch {idp} != {self.idp}")
        self.message_id = f"MOCKSAML{int(random() * 10**8)}"

    def get_attributes(self):
        """Just reflect what's posted right back."""
        post = self.request["post_data"]
        remote_user = post.get("remote_user", "")
        attributes = {}
        if post.get("idp") in uw.uwnetid_attribute_entities:
            uwnetid = remote_user.split("@washington.edu")[0]
            attributes["uwnetid"] = [uwnetid]
        elif post.get("idp") == federated.CollegenetIdp.entity_id:
            attributes["collegenet_userid"] = [remote_user]
        attributes.update((key, [value]) for key, value in post.items())
        return attributes

    def get_errors(self):
        return self.errors

    def get_last_error_reason(self):
        return self.errors[0]

    def get_last_authn_contexts(self):
        return []

    def get_last_message_id(self):
        return self.message_id
