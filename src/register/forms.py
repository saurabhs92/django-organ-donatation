from django import forms

from .models import Donor

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
                   'first_name',       
                   'last_name',        
                   'gender',           
                   'email',            
                   'date_of_birth',    
                   'contact_no',       
                   'emergeny_contact', 
                   'street_add1',      
                   'street_add2',      
                   'city',             
                   'state',            
                   'postal_code',      
                   'organ',            
        ]
    
