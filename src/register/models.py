from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import uuid

class Organ(models.Model):
    name             = models.CharField(max_length=50)
    description      = models.TextField()
    
    def __str__(self):
        return self.name

class Donor(models.Model):
    first_name       = models.CharField(max_length=50)
    last_name        = models.CharField(max_length=50)
    gender           = models.IntegerField()
    email            = models.EmailField(unique=True)
    date_of_birth    = models.DateField(auto_now_add=False, auto_now=False)
    contact_no       = models.PositiveIntegerField(max_length=10, unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    emergeny_contact = models.PositiveIntegerField(max_length=10, unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    street_add1      = models.CharField(max_length = 50)
    street_add2      = models.CharField(max_length = 50)
    city             = models.CharField(max_length = 50)
    state            = models.CharField(max_length = 50)
    postal_code      = models.PositiveIntegerField()
    id               = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    registered       = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated          = models.DateTimeField(auto_now_add=False, auto_now=True)
    organ            = models.ManyToManyField(Organ)
    
    def __str__(self):
        return self.first_name
    
    def get_absolute_url(self):
        return reverse('register:detail', kwargs={"id": self.id})
