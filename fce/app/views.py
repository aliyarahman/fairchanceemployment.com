from django.shortcuts import render

import urlparse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from app.forms import CustomLoginForm, CreateAccountForm 


def index(request):
    if request.method == 'POST':
        login_form = CustomLoginForm(data = request.POST or None)
        registration_form = CreateAccountForm(data = request.POST or None)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if request.user.is_authenticated():
                    return HttpResponseRedirect(reverse('jobseeker_home'))
            else:
                return HttpResponse("That is not the correct username / password") #do we want an http respons for this?
        elif registration_form.is_valid():
            username = registration_form.cleaned_data.get('username')
            email = registration_form.cleaned_data.get('email')
            password = registration_form.cleaned_data.get('password')
            retype_password = registration_form.cleaned_data.get('retype_password')
            user = User.objects.create_user(username, email, password) 
            user.first_name = registration_form.cleaned_data.get('first_name')
            user.last_name = registration_form.cleaned_data.get('last_name')
            user.save()
            user = authenticate(email=email, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('jobseeker_home'))

    login_form = CustomLoginForm()
    registration_form = CreateAccountForm()
    return render(request, "index.html", {'login_form': login_form, 'registration_form': registration_form}) 

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



# def logout(request):
#     logout(request)
#     return render(request, "index.html")

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



















