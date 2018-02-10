from django.conf.urls import url
from oauth2.views import Oauth2View, Oauth2CallbackView

urlpatterns = [
    url(r'^$', Oauth2View, name='oauth2-view'),
    url(r'^oauth2callback$', Oauth2CallbackView, name='oauth2-callback-view'),
]


