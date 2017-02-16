from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class School(models.Model):
    school_id = models.CharField(primary_key=True,max_length=20)
    school_name = models.CharField(max_length=300,null=True,blank=True)
    school_branch_area = models.CharField(max_length=200,null=True,blank=True)
    affiliation_number = models.CharField(max_length=100,null=True,blank=True) 
    board = models.CharField(max_length=10,null=True,blank=True)
    address = models.CharField(max_length=1000,null=True,blank=True)
    North = 'North'
    East = 'East'
    West = 'West'
    South = 'South'
    NorthEast = 'North East'
    NorthWest = 'Nort West'
    Central = "Central"
    NewDelhi = "New Delhi"
    SouthWest = "South West"
    zone_choices = (
        (North,'North'),
        (East,'East'),
        (West,'West'),
        (South,'South'),
        (NorthEast,'North East'),
        (NorthWest,'North West'),
        (Central,'Central'),
        (NewDelhi,'New Delhi'),
        (SouthWest,'South West'),
    )
    zone = models.CharField(max_length=15,choices=zone_choices,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    pincode = models.CharField(max_length=6,null=True,blank=True)
    active_status = models.BooleanField(default=1)
    transport_incharge = models.CharField(max_length=50,null=True,blank=True)
    transport_incharge_number = models.CharField(max_length=10,null=True,blank=True)
    check_filed = models.CharField(blank=True,null=True,max_length=100)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.school_name +", "+ self.school_branch_area

    def save(self, *args, **kwargs):
        self.check_filed = self.pincode + self.school_id
        self.slug = slugify(self.school_name +"-"+ self.school_branch_area)
        super(School, self).save(*args, **kwargs)
