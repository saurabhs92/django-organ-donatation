from django.contrib import admin
from .models import Donor, Organ

class DonorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'registered']
    list_filter = ['registered', 'organ']
    class Meta:
        model = Donor

admin.site.register(Donor, DonorModelAdmin)
admin.site.register(Organ)
