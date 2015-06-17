from django.shortcuts import render

import urlparse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def search(request):
    employers = Employer.objects.all()
    selected_employer = Employer.objects.filter(name="Wash Cycle Laundry").first()
    comments = selected_employer.usercomment_set.all()
    return render(request, "search.html", {'employers':employers, 'selected_employer':selected_employer, 'comments':comments})

    # if searching by top rank
    # top_employers = Employer.object.all().order_by(score, descending, limit=20)


def employer_home(request):
    return render(request, "employer_home.html")

def jobseeker_home(request):
    return render(request, "jobseeker_home.html")

def consumer_home(request):
    return render(request, "consumer_home.html")

def add_employer(request, employer_id):
    return render(request, "add_employer.html")

def edit_employer(request, employer_id):
    return render(request, "edit_employer.html")