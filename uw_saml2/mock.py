import urllib.parse


class SamlAuthenticator:
    def __init__(self, request, old_settings, *args, **kwargs):
        self.request = request
        self.idp = old_settings['idp']['entityId']
        self.errors = []

    def login(self, **kwargs):
        kwargs['idp'] = self.idp
        qs = urllib.parse.urlencode(kwargs)
        return f'mock-login?{qs}'

    def process_response(self):
        idp = self.request['post_data'].get('idp')
        if idp != self.idp:
            self.errors.append(f'idp mismatch {idp} != {self.idp}')
        return

    def get_attributes(self):
        """Just reflect what's posted right back."""
        items = self.request['post_data'].items()
        return dict((key, [value]) for key, value in items)

    def get_errors(self):
        return self.errors

    def get_last_error_reason(self):
        return self.errors[0]

    def get_last_authn_contexts(self):
        return []
