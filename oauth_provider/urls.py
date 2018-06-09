from django.conf.urls.static import static

from oauth_provider.compat import url
from django.views.generic import RedirectView
from adl_lrs import settings

from views import request_token, user_authorization, access_token

# LRS CHANGE - ADDED SPEC COMPLIANT ENDPOINTS
urlpatterns = [
    # redirect for just /xapi/OAuth
    url(r'^$', RedirectView.as_view(url='/')),

    url(r'^initiate$', request_token, name='request_token'),
    url(r'^authorize$', user_authorization, name='user_authorization'),
    url(r'^token$', access_token, name='access_token'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
