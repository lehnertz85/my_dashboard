from django.contrib import messages
from django.contrib.auth import authenticate, logout, update_session_auth_hash, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from dashboard.forms import ServicesForm, DrivesForm, BaseServicesFormModelFormSet
from .models import Services, General, Drives

from my_dashboard.utils import analyze_errors

from psutil import disk_usage
import logging
import json

logger = logging.getLogger('dashboard')


def login_view(request):
    title = General.objects.get(pk=1)

    if request.method == 'POST':
        loginform = AuthenticationForm(request)

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user, backend=None)
                messages.success(request, 'Logged in!')
                return redirect('')
            else:
                messages.error(request, 'Username or password is incorrect')
    else:
        loginform = AuthenticationForm()

    context = {
        'loginform': loginform,
        'title': title,
    }

    return render(request, 'login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('')


@login_required
def profile_view(request, username=None):
    title = General.objects.get(pk=1)

    if request.method == 'POST':
        changeform = PasswordChangeForm(request.user, request.POST)

        if changeform.is_valid():
            user = changeform.save()
            update_session_auth_hash(request, user)
            return redirect('')

    else:
        changeform = PasswordChangeForm(username)

    context = {
        'username': username,
        'changeform': changeform,
        'title': title,
    }

    return render(request, 'profile.html', context)


@login_required
def index(request):
    # Variables:
    drives = {}
    username = request.user

    # Do all the queries
    services = Services.objects.all()
    drive_letters = Drives.objects.all()
    settings_icon = Services.objects.get(service_name__exact='Settings')
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
            success_message = json.dumps({"success": "Saved!!!"})
            return HttpResponse(success_message)
        else:
            # Reconfigure the errors becuase of MaterializesCSS' toasts
            errors = analyze_errors(drivesformset, servicesformset)
            return HttpResponse(errors)
    else:
        servicesformset = ServicesFormSet(prefix='serviceForms')
        drivesformset = DrivesFormSet(prefix='driveForms')

    # Calculate Disk usage
    for d in drive_letters:
        usage = disk_usage(d.letter)
        percentage = usage.percent
        #logger.debug('\"**** Drive ' + d.letter + ' has ' + str(percentage) + '% space left!!')
        drives[d.letter] = percentage

    context = {
        'drivesformset': drivesformset,
        'servicesformset': servicesformset,
        'services': services,
        'settings_icon': settings_icon,
        'title': title,
        'drives': drives,
        'username': username,
    }

    return render(request, 'base.html', context)


# Create the iframe
@login_required
def getiframe(request, service_id=None):

    username = request.user

    url = Services.objects.get(id=service_id)

    services = Services.objects.all()
    settings_icon = Services.objects.get(service_name__exact='Settings')
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
            success_message = json.dumps({"success": "Saved!!!"})
            return HttpResponse(success_message)
        else:
            # Reconfigure the errors becuase of MaterializesCSS' toasts
            errors = analyze_errors(drivesformset, servicesformset)
            return HttpResponse(errors)
    else:
        servicesformset = ServicesFormSet(prefix='serviceForms')
        drivesformset = DrivesFormSet(prefix='driveForms')

    #logger.debug('****  Created iframe -- ')

    context = {
        'drivesformset': drivesformset,
        'servicesformset': servicesformset,
        'services': services,
        'settings_icon': settings_icon,
        'title': title,
        'url': url,
        'username': username,
    }

    return render(request, 'app_iframe.html', context)
