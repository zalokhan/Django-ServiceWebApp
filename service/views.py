from django.contrib.auth.decorators import login_required

from arena.main_home_arena import *
from arena.register_arena import *
from arena.myhome_arena import *


def main_home(request):
    return main_home_arena(request)


def login(request):
    return login_check_arena(request)


def register(request):
    return register_arena(request)


def register_check(request):
    return register_check_arena(request)


@login_required
def my_home(request):
    return my_home_main_arena(request)
