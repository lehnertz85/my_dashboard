from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import modelformset_factory

from dashboard.forms import ServicesForm, DrivesForm, BaseServicesFormModelFormSet
from models import Services, General, Drives

from psutil import disk_usage
import logging

from inspector_panel import debug

logger = logging.getLogger('dashboard')


# TODO:
#   1. Login screen w/ change password and add user(?)
#   2. Error checking in forms
#   3. Convert to one view * probably won't do this.


def index(request):
    # Variables:
    drives = {}

    # Do all the queries
    settings = Services.objects.all()
    drive_letters = Drives.objects.all()
    settings_icon = Services.objects.get(app_name__exact='Settings')
    title = General.objects.get(pk=1)

    # Create the Forms
    ServicesFormSet = modelformset_factory(Services, can_delete=True, form=ServicesForm,
                                           formset=BaseServicesFormModelFormSet)
    DrivesFormSet = modelformset_factory(Drives, can_delete=True, form=DrivesForm)

    if request.method == "POST":
        servicesformset = ServicesFormSet(request.POST, prefix='serviceForms')
        drivesformset = DrivesFormSet(request.POST, prefix='driveForms')

        if servicesformset.is_valid() and drivesformset.is_valid():
            servicesformset.save()
            drivesformset.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        servicesformset = ServicesFormSet(prefix='serviceForms')
        drivesformset = DrivesFormSet(prefix='driveForms')
        print("++++++ craeted forms")

    # Calculate Disk usage
    for d in drive_letters:
        usage = disk_usage(d.letter)
        percentage = usage.percent
        logger.debug('\"**** Drive ' + d.letter + ' has ' + str(percentage) + '% space left!!')
        drives[d.letter] = percentage

    context = {
        'drivesformset': drivesformset,
        'servicesformset': servicesformset,
        'settings': settings,
        'settings_icon': settings_icon,
        'title': title,
        'drives': drives,
    }

    return render(request, 'base.html', context)


# Create the iframe
def getiframe(request, app_id=2):
    # Variables:
    drives = {}

    url = Services.objects.get(id=app_id)

    settings = Services.objects.all()
    settings_icon = Services.objects.get(app_name__exact='Settings')
    title = General.objects.get(pk=1)
    drive_letters = Drives.objects.all()

    # Create the Forms
    ServicesFormSet = modelformset_factory(Services, can_delete=True, form=ServicesForm,
                                           formset=BaseServicesFormModelFormSet)
    DrivesFormSet = modelformset_factory(Drives, can_delete=True, form=DrivesForm)

    if request.method == "POST":
        servicesformset = ServicesFormSet(request.POST, prefix='serviceForms')
        drivesformset = DrivesFormSet(request.POST, prefix='driveForms')

        if servicesformset.is_valid() and drivesformset.is_valid():
            servicesformset.save()
            drivesformset.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        servicesformset = ServicesFormSet(prefix='serviceForms')
        drivesformset = DrivesFormSet(prefix='driveForms')
        print("++++++ craeted forms")

    # Calculate Disk usage
    for d in drive_letters:
        usage = disk_usage(d.letter)
        percentage = usage.percent
        #logger.debug('\"**** Drive ' + d.letter + ' has ' + str(percentage) + ' space left!!')
        drives[d.letter] = percentage

    logger.debug('****  Created iframe -- ')

    context = {
        'drivesformset': drivesformset,
        'servicesformset': servicesformset,
        'settings': settings,
        'settings_icon': settings_icon,
        'title': title,
        'drives': drives,
        'url': url
    }

    return render(request, 'app_iframe.html', context)
