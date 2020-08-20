from django.shortcuts import render

from Login_app.forms import UserForm, UserInfoForm
# Create your views here.

#authenticate user, login user, and logout user function
from django.contrib.auth import authenticate, login, logout
#http response and redirect function
from django.http import HttpResponseRedirect, HttpResponse
#useing decorators and login_required we find user login or not.
from django.contrib.auth.decorators import login_required
#move one view to other view with urls
from django.urls import reverse

#User model added
from django.contrib.auth.models import User
#UserInfo model added
from Login_app.models import UserInfo



def login_page(request):

    diction={
        'title': 'Login | Authentication'
    }
    return render(request, 'Login_app/login.html', context=diction)

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Login_app:Home'))
            else:
                return HttpResponse("Account is not active!!")
        else:
            return HttpResponse("Username or password was wrong!!")

    else:
        return HttpResponseRedirect(reverse('Login_app:login'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_app:Home'))


def index(request):

    diction={
        'title': 'Home | Authentication'
    }
    if request.user.is_authenticated:
        current_user = request.user
        print(current_user.username)
        print(current_user.id)
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = UserInfo.objects.get(user__id = user_id)
        diction = {
            'user_basic_info':user_basic_info,
            'user_more_info':user_more_info
        }
        diction.update({'title': 'Login-Home | Authentication'})
    return render(request, 'Login_app/index.html', context=diction)

def register(request):

    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():

            user = user_form.save()#create a object of last added data
            user.set_password(user.password)#last added objects password enctyped by this
            user.save()

            user_info = user_info_form.save(commit=False)#creat object but not save
            user_info.user = user #one to one connection wih two model

            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']

            user_info.save()
            registered = True
    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()

    diction = {
        'title': 'Register | Authentication',
        'user_form':user_form,
        'user_info_form':user_info_form,
        'registered':registered
    }
    return render(request, 'Login_app/register.html', context=diction)
