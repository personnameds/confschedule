from django.conf.urls import url
from .views import KlassCreateView, KlassScheduleCreateView

urlpatterns = [
    url(r'^class$', KlassCreateView.as_view(), name='klass-create-view'),
    url(r'^schedule/', KlassScheduleCreateView.as_view(), name='klass-schedule-create-view'),
]
