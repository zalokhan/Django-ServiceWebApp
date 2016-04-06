from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .models import User as UserModel
import dj_database_url


def login_page(request):
    # print (dj_database_url.config())
    return render(request, 'service/login_page.html')


def login(request):
    user_id = request.POST['user_id']
    password = request.POST['password']
    user = authenticate(username=user_id, password=password)
    if user is not None:
        if user.is_active:
            print("User is valid, active and authenticated")
            auth_login(request, user)
            return HttpResponseRedirect(reverse('service:my_home'))
        else:
            print("The password is valid, but the account has been disabled!")
            return HttpResponseRedirect(reverse('service:login_page'))
    else:
        # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")
        return HttpResponseRedirect(reverse('service:login_page'))


def register(request):
    return render(request, 'service/register.html')


def register_check(request):
    user_id = request.POST['user_id']
    user_first_name = request.POST['user_first_name']
    user_last_name = request.POST['user_last_name']
    user_email = request.POST['user_email']
    user_phone = request.POST['user_phone']
    user_dob = request.POST['user_dob']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if user_id is None or \
                    user_email is None or \
                    user_first_name is None or \
                    user_last_name is None or \
                    user_phone is None or \
                    user_dob is None or \
                    password is None or \
                    password != repassword:
        print ("Invalid entries for registration !")
        return HttpResponseRedirect(reverse('service:register'))

    try:
        db_user = get_object_or_404(UserModel, user_id=user_id)
    except(Http404):
        pass
    else:
        print("User ID already present")
        return HttpResponseRedirect(reverse('service:register'))

    auth_user = User.objects.create_user(user_id, user_email, password)
    user = UserModel(user_id=user_id,
                     user_email=user_email,
                     user_first_name=user_first_name,
                     user_last_name=user_last_name,
                     user_phone=user_phone,
                     user_dob=user_dob)
    user.save()
    return HttpResponseRedirect(reverse('service:login_page'))


@login_required
def my_home(request):
    logout(request)
    return render(request, 'service/user_home.html')
