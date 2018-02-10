from django import forms
from classlists.models import Klass

class Alt_Klass_Schedule_FormOne(forms.Form):
	klass=forms.ModelChoiceField(queryset=Klass.objects.all())
	first_day=forms.DateField(widget=forms.SelectDateWidget())
	last_day=forms.DateField(widget=forms.SelectDateWidget())