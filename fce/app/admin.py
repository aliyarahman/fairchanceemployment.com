from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from app.models import *

# Register your models here.
admin.site.register(Industry)
admin.site.register(Employer)
admin.site.register(UserComment)
admin.site.register(BlogPost)
