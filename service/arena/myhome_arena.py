from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render
from django.core.urlresolvers import reverse


def my_home_main_arena(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('service:main_home'))
    # logout(request)
    return render(request, 'service/user_home.html')
