from django.urls import path
from .views import KlassCreateView, KlassScheduleFormOneView, KlassScheduleFormTwoView
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('class', staff_member_required(KlassCreateView.as_view()), name='klass-create-view'),
    path('schedule_dates', staff_member_required(KlassScheduleFormOneView.as_view()), name='klass-schedule-create-one-view'),
    path('schedule_info', staff_member_required(KlassScheduleFormTwoView.as_view()), name='klass-schedule-create-two-view'),

]
