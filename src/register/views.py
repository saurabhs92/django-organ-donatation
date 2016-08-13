from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DonorForm
from .models import Donor
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas

def register_donor(request):
    form = DonorForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context_1 = {
            'title': 'Donor Details',
        }
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

def register_success(request):
    context = {
        'title': 'Donor Details',
    }
    return render(request, 'register/register_sucess.html', context)

def download_donor_card(request, id):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="donor_card.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, id)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response 

