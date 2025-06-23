import datetime

from django import forms
from django.forms import ModelForm

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from catalog.models import BookInstance

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weekas (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # check if a date is not in the past 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        
        # check if a data is in the allowed range (+ 4 weeks from today)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        
        return data
    
class RenewBookModelForm(ModelForm):
    
    def clean_renewal_date(self):
        data = self.cleaned_data['due_back']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        
        return data
    
    class Meta:
        model = BookInstance
        fields = ['due_back']
        # fields = '__all__'
        # exclude = ['due_back']
        labels = {'due_back': _('New renewal date')}
        help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3)')}
    
    