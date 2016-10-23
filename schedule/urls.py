from django.conf.urls import url
from .views import KlassScheduleView, BookSlotView, EditSlotView

urlpatterns = [
    url(r'^$', KlassScheduleView.as_view(), name='klass-schedule-view'),
    url(r'^(?P<slot>\d+)$', BookSlotView.as_view(), name='book-slot'),
    url(r'^(?P<slot>\d+)/(?P<pk>\d+)', EditSlotView.as_view(), name='edit-slot'),
]
