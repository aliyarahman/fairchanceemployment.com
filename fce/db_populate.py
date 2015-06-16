import django
django.setup()
from app.models import *
from django.contrib.auth.models import User
from django.utils import timezone

# Add test user
rc = User.objects.create_user('ReturningCtzn202', "rc202@fairchanceemployment.com", "Popcorn13")

# Pull up users
aliya = User.objects.filter(username = "aliya").first()
rc = User.objects.filter(username = "ReturningCtzn202").first()


# Add industries
for i in ["Arts & Culture", "Education", "Entertainment", "Food Service", "Government", "Healthcare", "Retail", "Service", "Technology", "Tourism", "Transportation"]:
    industry = Industry(name=i)
    industry.save()


# Add employers
tech = Industry.objects.filter(name = "Technology").first()
gov = Industry.objects.filter(name = "Government").first()
service = Industry.objects.filter(name = "Service").first()
education = Industry.objects.filter(name = "Education").first()

google = Employer(name = "Google", short_name = "Google")
google.save()
google = Employer.objects.filter(name = "Google").first()
google.industries.add(tech)

ohr = Employer(name = "DC Office of Human Rights", short_name = "DC OHR")
ohr.save()
ohr = Employer.objects.filter(short_name = "DC OHR").first()
ohr.industries.add(gov)

dclib = Employer(name = "DC Public Libraries", short_name = "DC Libraries")
dclib.save()
dclib = Employer.objects.filter(short_name = "DC Libraries").first()
dclib.industries.add(gov)
dclib.industries.add(education)


wash_cycle = Employer(name = "Wash Cycle Laundry", short_name = "WashCycle", phone="888-555-5555", hq_address="Pennsylvania", hq_in_dc=False, home_url="www.washcyclelaundry.com", employment_url="@TheWashCyclist", score = 92, stars=5, c1c1_complies_dc = 1, c2c1_friendly_attendance_policy = 1, c2c2_manager_training = 1, c3c1_eligible_work_opportunity = 2, c3c2_participates_work_opportunity = 0,c3c3_federal_bonding = 1, c4c1_merit_based_awards = 1, c4c2_leadership_training =1, c5c1_recruitment = 1, c5c2_supplier_diversity = 1, c5c3_friendly_marketing = 1,c5c4_public_advocacy = 1, c5c1_nature_of_crime = 1, c5c2_no_housing_history_check = 1, c5c3_no_residence_loc_review = 1, c5c4_no_housing_based_disq = 1, c5c5_no_arrests_inquiry = 1, c5c6_disregards_conviction_beyond_cutoff = 1, c5c6num_year_cutoff = 7, c5c7_discusses_unfavorable_check = 0, c5c8_no_automatic_dismiss_on_bg_check = 1, c5c9_differentiates_violent_offenses = 0, c5c10_record_is_not_major_barrier = 1)
wash_cycle.save()
wash_cycle.industries.add(service)


# Add comments
wash = Employer.objects.filter(name = "Wash Cycle Laundry").first()
comment = UserComment(author = aliya, employer = wash, text="I refer EVERYone to Wash Cycle even though don't actually use these folks (because I do my own laundry - no shade if you don't). But I have definitely been tempted! I saw their founder talk about their RC-friendly hiring policies, and as a person who is close to many returning citizens, I'm definitely a fan.", upvotes = 48)
comment.save()
comment = UserComment(author = rc, employer = wash, text = "I work for these folks - it's the only place I've ever worked where I can be honest about my record, and where I didn't get penalized for doing probation stuff. Also - I have great calves now from biking around yalls laundry, haha. Does your job give you that?", upvotes = 72)
comment.save()
