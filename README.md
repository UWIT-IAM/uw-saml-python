# uw-saml

A UW-specific adapter to the
[python3-saml](https://github.com/onelogin/python3-saml) package. This package
was built to federate with other IdPs, but the default case is to use the UW
Identity Provider. It can be used against any framework. For a django-specific
package, also consider
[uw-django-saml2](https://github.com/uw-it-aca/uw-django-saml2).

## Installation

```bash
pip install uw-saml
```

## Example login endpoint using flask

In this example you've gone to
[SP Registry](https://iam-tools.u.washington.edu/spreg) and registered an
Entity ID of https://samldemo.iamdev.s.uw.edu/saml, with an ACS endpoint of
https://samldemo.iamdev.s.uw.edu/saml/login. GETs will return a
redirect to the IdP for authentication, and POSTs will try to process a SAML
Response.

```python
from flask import request, session, redirect
import uw_saml2

@app.route('/saml/login', methods=['GET', 'POST'])
def login():
    session.clear()
    args = {
        'entity_id': 'https://samldemo.iamdev.s.uw.edu/saml',
        'acs_url': 'https://samldemo.iamdev.s.uw.edu/saml/login'
    }
    if request.method == 'GET':
        args['return_to'] = request.args.get('url', None)
        return redirect(uw_saml2.login_redirect(**args))

    attributes = uw_saml2.process_response(request.form, **args)
    session['userid'] = attributes['uwnetid']
    session['groups'] = attributes.get('groups', [])

    relay_state = request.form.get('RelayState')
    if relay_state and relay_state.startswith('/'):
        return redirect(urljoin(request.url_root, request.form['RelayState']))

    return 'Welcome ' + session['userid']
```

## Considerations

Give some consideration to session lifetime. The session in this example lives as a
signed cookie. Ideally the cookie would expire at browser close, along with
some time limit appropriate for your application. An example again with flask
for a ten minute limit...

```python
from datetime import timedelta

app.config.update(
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=10)
)
```
