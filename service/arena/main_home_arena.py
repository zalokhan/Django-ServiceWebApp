from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login


def main_home_arena(request):
    alert_message = request.session.get('alert_message', None)
    alert_type = request.session.get('alert_type', None)
    if 'alert_message' in request.session:
        del request.session['alert_message']
        del request.session['alert_type']
    return render(request, 'service/main_home_page.html', {'alert_message': alert_message, 'alert_type': alert_type})


def login_check_arena(request):
    user_id = request.POST['user_id']
    password = request.POST['password']
    user = authenticate(username=user_id, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('service:my_home'))
        else:
            message = "This account has been disabled. Contact the admin."
            alert_type = "danger"
            request.session['alert_message'] = message
            request.session['alert_type'] = alert_type
            return HttpResponseRedirect(reverse('service:main_home'))
    else:
        # the authentication system was unable to verify the username and password
        message = "The username or password were incorrect."
        alert_type = "danger"
        request.session['alert_message'] = message
        request.session['alert_type'] = alert_type
        return HttpResponseRedirect(reverse('service:main_home', ))