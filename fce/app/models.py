import django, datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Industry(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Employer(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=45)
    industries = models.ManyToManyField(Industry)
    phone = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    hq_address = models.CharField(max_length=255, null=True, blank=True)
    hq_in_dc = models.BooleanField(default=False)
    home_url = models.CharField(max_length=255, null=True, blank=True)
    employment_url = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    score = models.IntegerField(default = 0)
    stars = models.IntegerField(default = 0)

    # Category 1 Criteria
    c1c1_complies_dc = models.IntegerField(default = 0) #Complies w DC's ban the box law

    # Category 2 Criteria
    c2c1_friendly_attendance_policy = models.IntegerField(default = 0)
    c2c2_manager_training = models.IntegerField(default = 0)

    # Category 3 Criteria
    c3c1_eligible_work_opportunity = models.IntegerField(default = 0)
    c3c2_participates_work_opportunity = models.IntegerField(default = 0)
    c3c3_federal_bonding = models.IntegerField(default = 0)

    # Category 4 Criteria
    c4c1_merit_based_awards = models.IntegerField(default = 0)
    c4c2_leadership_training = models.IntegerField(default = 0)

    # Category 5 Criteria
    c5c1_recruitment = models.IntegerField(default = 0)
    c5c2_supplier_diversity = models.IntegerField(default = 0)
    c5c3_friendly_marketing = models.IntegerField(default = 0)
    c5c4_public_advocacy = models.IntegerField(default = 0)

    # Category 6 Criteria
    c5c1_nature_of_crime = models.IntegerField(default = 0)
    c5c2_no_housing_history_check = models.IntegerField(default = 0)
    c5c3_no_residence_loc_review = models.IntegerField(default = 0)
    c5c4_no_housing_based_disq = models.IntegerField(default = 0)
    c5c5_no_arrests_inquiry = models.IntegerField(default = 0)
    c5c6_disregards_conviction_beyond_cutoff = models.IntegerField(default = 0)
    c5c6num_year_cutoff = models.IntegerField(null=True, blank = True)
    c5c7_discusses_unfavorable_check = models.IntegerField(default = 0)
    c5c8_no_automatic_dismiss_on_bg_check = models.IntegerField(default = 0)
    c5c9_differentiates_violent_offenses = models.IntegerField(default = 0)
    c5c10_record_is_not_major_barrier = models.IntegerField(default = 0)
    c5c11_dishonesty_insurance = models.IntegerField(default = 0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.short_name



class UserComment(models.Model):
    author = models.ForeignKey(User)
    employer = models.ForeignKey(Employer)
    text = models.TextField(null=True, blank=True)
    upvotes = models.IntegerField(default= 0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.text[0:30]+"..."



class BlogPost(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=140)
    text = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title