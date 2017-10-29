from django.conf.urls import url
from .views import KlassCreateView, KlassScheduleCreateView
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    url(r'^class$', staff_member_required(KlassCreateView.as_view()), name='klass-create-view'),
    url(r'^schedule/', staff_member_required(KlassScheduleCreateView.as_view()), name='klass-schedule-create-view'),
]
