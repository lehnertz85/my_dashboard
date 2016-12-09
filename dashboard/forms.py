import platform
import re

from django import forms
from django.forms import BaseModelFormSet
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from psutil import disk_usage

from dashboard.models import Services, Drives


class BaseServicesFormModelFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseServicesFormModelFormSet, self).__init__(*args, **kwargs)
        # skip the Settings objects
        self.queryset = Services.objects.exclude(id=1)


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'
        labels = {
            "service_name": 'Service\'s Name:',
            'icon': 'Select and icon:',
            'url': 'Enter a URL:',
            'is_visible': 'Do you want this application visible?'
        }
        required = {
            'service_name': 'false',
            'icon': 'false',
            'url': 'false',
            'is_visible': 'false',
        }
        max_length = {
            'service_name': '512',
            'icon': '512',
            'url': '512',
        }

        widgets = {
            "service_name": forms.TextInput(attrs={'class': 'validate', 'length': '512', 'placeholder': 'Enter the service\'s name:'}),
            'icon': forms.TextInput(attrs={'class': 'validate', 'placeholder': ' Choose an icon'}),
            'url': forms.TextInput(attrs={'class': 'validate', 'placeholder': 'What is the URL', 'length': '512'}),
        }

    def clean(self):
        cleaned_data = super(ServicesForm, self).clean()
        url = cleaned_data.get("url")

        if 'http://' in url or 'https://' in url:
            print('**** url is good to go')
        else:
            print("URL must contain http:// or https://")
            raise forms.ValidationError(_('URL is incorrect'))

        return cleaned_data


class DrivesForm(forms.ModelForm):
    class Meta:
        model = Drives
        fields = '__all__'
        labels = {
            'letter': 'Drive:',
        }
        required = {
            'letter': 'false',
        }
        max_length = {
            'letter': '128',
        }

        widgets = {
            'letter': forms.TextInput(
                attrs={'class': 'validate', 'placeholder': ' Add a new Drive here', 'length': '128'}),
        }

    def clean(self):
        cleaned_data = super(DrivesForm, self).clean()
        letter = cleaned_data.get("letter")
        print('*** Entering drive clean() ... %s' % letter)

        if platform.system() == "Windows":
            if not re.search(r"^[a-zA-Z]:\\$", letter):
                raise forms.ValidationError(_('Drive letter is incorrect. Look at Help for more info'))

        try:
            # Test to make sure the drive is present on the computer.
            disk_usage(letter)
        except:
            raise forms.ValidationError(_('The drive could not be located'))

        return cleaned_data
