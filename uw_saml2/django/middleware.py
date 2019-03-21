from . import views
from django.conf import settings


def uwnetid_middleware(get_response):
    """
    Middleware to add 'uwnetid' to the request if it exists on the session.
    """
    def middleware(request):
        request.uwnetid = request.session.get(views.UWNETID_SESSION_KEY)
        return get_response(request)
    return middleware


def always_require_uwnetid(get_response):
    def middleware(request):
        if request.path in (settings.LOGIN_URL, settings.SAML_ACS_PATH):
            return get_response(request)
        request.uwnetid = request.session.get(views.UWNETID_SESSION_KEY)
        if not request.uwnetid:
            path = request.get_full_path()
            return views.login_redirect(request, return_to=path)
        return get_response(request)
    return middleware
