from django.conf.urls import url
from .views import KlassScheduleView, BookSlotView, EditSlotView, PrintScheduleView, PrintPDFView, ClearSlotView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', KlassScheduleView.as_view(), name='klass-schedule-view'),
    url(r'^print$', login_required(PrintScheduleView.as_view()), name='print-view'),
    url(r'^printpdf$', login_required(PrintPDFView), name='print-pdf-view'),
    url(r'^(?P<slot>\d+)$', BookSlotView.as_view(), name='book-slot'),
    url(r'^clear/(?P<slot>\d+)$', login_required(ClearSlotView.as_view()), name='clear-slot'), 
    url(r'^(?P<slot>\d+)/(?P<pk>\d+)$', EditSlotView.as_view(), name='edit-slot'),
]
