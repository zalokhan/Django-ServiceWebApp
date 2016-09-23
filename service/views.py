from arena.main_home_arena import main_home_arena, login_check_arena, logout_arena
from arena.register_arena import register_arena, register_check_arena
from arena.user_home_arena import user_home_main_arena

"""
Main Home Page
Website landing page
"""


def main_home(request):
    return main_home_arena(request)


"""
Login Check
Validates login values
"""


def login(request):
    return login_check_arena(request)


"""
Logout
Logs out the user
"""


def logout(request):
    return logout_arena(request)


"""
Register Page
Register new account landing page
"""


def register(request):
    return register_arena(request)


"""
Register Check
Validates registration values
"""


def register_check(request):
    return register_check_arena(request)


"""
User Home page
User Dashboard and home landing page
"""


def user_home(request):
    return user_home_main_arena(request)
