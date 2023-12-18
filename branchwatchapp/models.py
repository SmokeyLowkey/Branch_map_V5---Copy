from django.contrib.gis.db import models
from django.contrib.auth.hashers import make_password, check_password
from tinymce.models import HTMLField

class CompanyBranch(models.Model):
    Branch_Id = models.CharField(max_length=500, unique=True, primary_key=True)
    Branch_Name = models.CharField(max_length=500)
    Info = HTMLField()
    # Address = HTMLField()
    # Phone = HTMLField()
    # Branch_Info = HTMLField()
    # Shipping_Instructions = HTMLField()
    # Ordering_Instructions = HTMLField()
    # Branch_Specific_Policies = HTMLField()
    # Dropbox_Locations_Carriers = HTMLField()
    # Other_Notes = HTMLField()
    Geom = models.PointField(null=True)
    time_zone = models.CharField(max_length=50, null=True, blank=True)
    Division = models.CharField(max_length=50, null=True, blank=True)
    
    
    def __str__(self):
        return self.Branch_Name

    class Meta:
        verbose_name_plural = 'Company Branch Info'

from django.db import models

class Branch(models.Model):
    Branch_Id = models.CharField(max_length=500, unique=True, primary_key=True)
    Name = models.CharField(max_length=255)
    Contacts = HTMLField()
    # Misc = HTMLField()
    # Parts = HTMLField()
    # Shipping_Info = HTMLField()
    # Service = HTMLField()
    # Sales = HTMLField()

    def __str__(self):
        return self.Name
    class Meta:
        verbose_name_plural = 'Company Branch Contact'


class UserAuthentication(models.Model):
    username = models.CharField(max_length=50, unique=True)
    hashed_password = models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.hashed_password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.hashed_password)