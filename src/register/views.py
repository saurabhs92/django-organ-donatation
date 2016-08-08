from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DonorForm
from .models import Donor
from django.shortcuts import get_object_or_404

def register_donor(request):
    form = DonorForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'register/register_donor.html', context)

def donor_detail(request, id):
    donor = get_object_or_404(Donor, id=id)
    context = {
        'title': 'Donor Details',
        'donor': donor,
    }
    return render(request, 'register/donor_detail.html', context)
