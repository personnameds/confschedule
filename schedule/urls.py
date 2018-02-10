from django.urls import path
from .views import KlassScheduleView, BookSlotView, EditSlotView, PrintScheduleView, PrintPDFView, ClearSlotView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('', KlassScheduleView.as_view(), name='klass-schedule-view'),
    path('print', permission_required('slot.can_delete')(PrintScheduleView.as_view()), name='print-view'),
    path('printpdf', permission_required('slot.can_delete')(PrintPDFView), name='print-pdf-view'),
    
    
    path('<int:slot_id>', BookSlotView.as_view(), name='book-slot'),
    path('clear/(?P<slot>\d+)', permission_required('slot.can_delete')(ClearSlotView.as_view()), name='clear-slot'), 
    path('(?P<slot>\d+)/(?P<pk>\d+)', EditSlotView.as_view(), name='edit-slot'),
]
