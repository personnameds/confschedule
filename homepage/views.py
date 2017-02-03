from django.shortcuts import render
from django.views.generic.base import TemplateView
from classlists.models import Klass
from schedule.models import SchoolScheduleDetails
from django.conf import settings

class KlassListMixin(object):
    def get_context_data(self, **kwargs):
        context=super(KlassListMixin, self).get_context_data(**kwargs)
        context['list_of_classes']=Klass.objects.all()
        return context


class HomepageView(KlassListMixin, TemplateView):
    template_name='homepage/homepage.html'
    
    def get_context_data(self, **kwargs):
        context=super(HomepageView, self).get_context_data(**kwargs)
        context['school_schedule']=SchoolScheduleDetails.objects.get(name=settings.SCHOOL_NAME)
        return context
