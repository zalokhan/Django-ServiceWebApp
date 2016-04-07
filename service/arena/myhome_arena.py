from django.contrib.auth import logout

def my_home_main_arena(request):
    logout(request)
    return render(request, 'service/user_home.html')
