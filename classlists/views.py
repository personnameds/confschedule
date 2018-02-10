from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from .models import Klass, KlassForm
from .forms import Alt_Klass_Schedule_FormOne
from homepage.views import KlassListMixin
from schedule.models import Standard_Day_Schedule, Slot, Alt_Klass_Schedule, Alt_Klass_Schedule_FormTwo
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from datetime import date, datetime, timedelta
from schedule.models import Standard_Day_Schedule


class KlassCreateView(KlassListMixin, CreateView):
    model=Klass
    form_class=KlassForm
    template_name='classlists/add_klass_form.html'
    
    def form_valid(self, form):
        new_klass=form.save()
        
        int_dates=Standard_Day_Schedule.objects.all()
        
        ##Create Slots for Class using Standard Schedule
        for int_day in int_dates:
        	slot_start=int_day.start_time
        	slot_length=int_day.slot_length
        	for i in range(0, int_day.num_slots):
        		slot_end=(datetime.combine(date.today(), slot_start)+timedelta(minutes=slot_length)).time()
        		new_slot=Slot.objects.create(klass=new_klass,
        									int_date=int_day.int_date,
        									start=slot_start,
        									end=slot_end,
        									not_available=False)
        		slot_start=slot_end

        return HttpResponseRedirect(reverse_lazy('homepage-view'))


##Not ready not used
class KlassScheduleFormOneView(KlassListMixin, FormView):
    form_class=Alt_Klass_Schedule_FormOne
    template_name='schedule/klassschedule1.html'
    success_url=reverse_lazy('klass-schedule-create-two-view')

##Only modifies for a single day
class KlassScheduleFormTwoView(KlassListMixin, CreateView):
    model=Alt_Klass_Schedule
    form_class=Alt_Klass_Schedule_FormTwo
    template_name='schedule/klassschedule2.html'
    
    def form_valid(self, form):
        new_schedule=form.save()
        klass=new_schedule.klass
        int_date=new_schedule.int_date
        
        ##Delete old slots
        Slot.objects.filter(klass=klass,int_date=int_date).delete()
        
        slot_length=new_schedule.slot_length
        slot_start=new_schedule.start_time
        
        for i in range(0,new_schedule.num_slots):
            slot_end=(datetime.combine(date.today(), slot_start)+timedelta(minutes=slot_length)).time()
            new_slot=Slot.objects.create(klass=klass,
                                         int_date=int_date,
                                         start=slot_start,
                                         end=slot_end,
                                         not_available=False)
            slot_start=slot_end

        return HttpResponseRedirect(reverse_lazy('homepage-view'))