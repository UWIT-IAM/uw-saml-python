from django.conf import settings
from django.conf.urls import url
from . import views

login_url= r'^{}$'.format(settings.LOGIN_URL[1:])
saml_endpoint = r'^{}$'.format(settings.SAML_ACS_PATH[1:])

urlpatterns = [
    url(login_url, views.login_redirect),
    url(saml_endpoint, views.process_saml_response)
]
