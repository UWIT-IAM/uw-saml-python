# uw-saml

A UW-specific adapter to the
[python3-saml](https://github.com/onelogin/python3-saml) package. This package
was built to federate with other IdPs, but the default case is to use the UW
Identity Provider. It can be used against any framework. For a django-specific
package, also consider
[uw-django-saml2](https://github.com/uw-it-aca/uw-django-saml2).

## Installation

```bash
pip install uw-saml[python3-saml]
```

The extra `[python3-saml]` is because the SAML package can be cumbersome to
install in a workstation environment, on account of needing the libxmlsec1-dev
library. Therefore, it's an optional requirement, causing a runtime error
instead of an install-time error. Alternatively, you can use a mock
interface by setting `uw_saml2.python3_saml.MOCK = True`.

If you are able to run your app as a Docker container, you can base your image on
[ghcr.io/uwit-iam/uw-saml-poetry:latest](https://ghcr.io/uwit-iam/uw-saml-poetry:latest)
which comes with all dependencies pre-installed. Here is an example. Note that you 
don't have to use poetry in your install process to use this image.

```
FROM ghcr.io/uwit-iam/uw-saml-poetry:latest AS dependencies
RUN pip install flask uw-saml  # uw-saml and python3-saml are already installed!
COPY app.py ./
CMD flask run app
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

app = Flask(__name__)

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

### Sessions

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

### Replay attack prevention

By default this package uses an in-memory cache to check for replay attacks.
To use a distributed cache such as redis or memcached you would inject a
cache object into `uw_saml2.auth.CACHE`. Here's an example of how to do it...

```python
import werkzeug.contrib.cache
import uw_saml2.auth

uw_saml2.auth.CACHE = werkzeug.contrib.cache.RedisCache()
```

Django's cache backend uses the same methods so that could be injected as well.

# Developers

## Maintenance

People who are developing this package should have either [poetry] or a docker daemon
installed. This is so that you can run validations before pushing your code.

### Using docker (recommended)

This is recommended because this is the script the CI pipeline uses,
so if this works for you, it ought to work in the pipeline, too!

```
./scripts/pre-push.sh
```

### Using poetry

Running directly is helpful when you want to attach debuggers, etc.

```
poetry install
poetry run pytest
poetry run black uw_saml2 tests
```


## Pull Requests

When creating a pull request for this repository, a `semver-guidance` label must be 
applied to the PR. If you do not have write access, a reviewer must do this for 
you.

Use the following guidelines to select a version level for your change: 

- `no-bump` if the change is only for documentation, CI workflow, etc.
- `patch` if the change is a simple update or bugfix (e.g., idp metadata update, 
  certificate renewal, etc.), or if dependencies are updated (`poetry.lock` changes)
- `minor` if new features are added or deprecated but the change is backwards-compatible
- `major` if the change is not backwards compatible and will break consumers
