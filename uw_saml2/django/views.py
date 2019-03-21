from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
import uw_saml2
from logging import getLogger
logger = getLogger(__name__)
UWNETID_SESSION_KEY = '_uw-saml_uwnetid'


@never_cache
def login_redirect(request, return_to='/'):
    args = dict(entity_id=settings.SAML_ENTITY_ID,
                acs_url=request.build_absolute_uri(settings.SAML_ACS_PATH))
    url = uw_saml2.login_redirect(return_to='/', **args)
    return redirect(url)


@csrf_exempt
def process_saml_response(request):
    if request.method != 'POST':
        return login_redirect(request)
    
    args = dict(entity_id=settings.SAML_ENTITY_ID,
                acs_url=request.build_absolute_uri(settings.SAML_ACS_PATH))
    try:
        attributes = uw_saml2.process_response(request.POST, **args)
        request.session[UWNETID_SESSION_KEY] = attributes['uwnetid']
    except Exception as e:
        return HttpResponse('<h1>Error logging in</h1>', status_code=500)

    relay_state = request.POST.get('RelayState', '/')
    return redirect(request.build_absolute_uri(relay_state))
