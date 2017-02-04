from django.conf.urls import url
from .views import KlassScheduleView, BookSlotView, EditSlotView, PrintScheduleView

urlpatterns = [
    url(r'^$', KlassScheduleView.as_view(), name='klass-schedule-view'),
    url(r'^print$', PrintScheduleView.as_view(), name='print-view'),
    url(r'^(?P<slot>\d+)$', BookSlotView.as_view(), name='book-slot'),
    url(r'^(?P<slot>\d+)/(?P<pk>\d+)', EditSlotView.as_view(), name='edit-slot'),
]
