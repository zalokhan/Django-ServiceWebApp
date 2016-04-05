from django.conf.urls import url

from . import views

app_name = 'service'
urlpatterns = [
    # Home page
    url(r'^$', views.login_page, name='login_page'),
    # Login authentication
    url(r'^login/$', views.login, name='login'),
    # Register new user
    url(r'^register/$', views.register, name='register'),
    # Register successful
    url(r'^register/check/$', views.register_check, name='register_check'),
    # User Home page
    url(r'^home/$', views.my_home, name='my_home'),
]