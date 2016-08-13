from django.contrib import admin
from .models import Donor, Organ

class DonorModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'contact_no', 'registered']
    list_filter = ['registered', 'organ']
    class Meta:
        model = Donor

admin.site.register(Donor, DonorModelAdmin)
admin.site.register(Organ)
