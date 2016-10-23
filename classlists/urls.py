from django.conf.urls import url
from .views import KlassCreateView

urlpatterns = [
    url(r'^$', KlassCreateView.as_view(), name='klass-create-view'),
]
