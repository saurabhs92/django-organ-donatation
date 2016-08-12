from django.db import models
from django.core.urlresolvers import reverse

class Organ(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Donor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    #unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    registered = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    dob = models.DateField(auto_now_add=False, auto_now=False)
    living = models.BooleanField()
    organ = models.ManyToManyField(Organ)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('register:detail', kwargs={"id": self.id})
