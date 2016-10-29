from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView
from .models import SchoolScheduleDetails, Slot
from classlists.models import Klass, Student, StudentForm, StudentDeleteForm
from homepage.views import KlassListMixin
from django.urls import reverse

class KlassScheduleView(KlassListMixin, TemplateView):
    template_name='schedule/schedule.html'

    def get_context_data(self, **kwargs):
        context=super(KlassScheduleView, self).get_context_data(**kwargs)
        klass=Klass.objects.get(pk=self.kwargs['klass'])
        context['klass']=klass
        context['klass_pm_schedule']=Slot.objects.filter(klass=klass, am_pm='pm')
        context['klass_am_schedule']=Slot.objects.filter(klass=klass, am_pm='am')
        return context
        
class BookSlotView(KlassListMixin, CreateView):
    model=Student
    form_class=StudentForm
    template_name='schedule/bookslot.html'

    def get_context_data(self, **kwargs):
        context=super(BookSlotView, self).get_context_data(**kwargs)
        klass=Klass.objects.get(pk=self.kwargs['klass'])
        slot=Slot.objects.get(pk=self.kwargs['slot'])
        context['klass']=klass
        context['slot']=slot
        return context
    
    def form_valid(self, form):
        new_student=form.save()
        slot=Slot.objects.get(pk=self.kwargs['slot'])
        slot.student=new_student
        slot.save()
        return super(BookSlotView, self).form_valid(form)
        
        
    def get_success_url(self):
        klass=Klass.objects.get(pk=self.kwargs['klass'])
        return reverse('klass-schedule-view', args=[klass.pk])

class EditSlotView(KlassListMixin, FormView):
    model=Student
    form_class=StudentDeleteForm
    template_name='schedule/editslot.html'

    def get_context_data(self, **kwargs):
        context=super(EditSlotView, self).get_context_data(**kwargs)
        klass=Klass.objects.get(pk=self.kwargs['klass'])
        slot=Slot.objects.get(pk=self.kwargs['slot'])
        student=Student.objects.get(pk=self.kwargs['pk'])
        context['klass']=klass
        context['slot']=slot
        context['student']=student
        return context
        
    def get_initial(self):
        initial=super(EditSlotView, self).get_initial()
        student=Student.objects.get(pk=self.kwargs['pk'])
        if self.request.user.is_authenticated():
            initial['first_name']=student.first_name
            initial['last_name']=student.last_name
            initial['phone']=student.phone  
        return initial
    
    def form_valid(self, form):
        form_student=form.save(commit=False)
        slot=Slot.objects.get(pk=self.kwargs['slot'])
        student=Student.objects.get(pk=self.kwargs['pk'])
        if form_student.first_name == student.first_name and form_student.last_name == student.last_name and form_student.phone == student.phone:
            student.delete()
            slot.student=None
            slot.save()
        else:
            ## should be done in clean method
            form.add_error(None, "Are you sure this is your spot? Something does not match. Please try again or click Cancel. ")
            return super(EditSlotView, self).form_invalid(form)
        return super(EditSlotView, self).form_valid(form)
    
    def get_success_url(self):
        klass=Klass.objects.get(pk=self.kwargs['klass'])
        return reverse('klass-schedule-view', args=[klass.pk])