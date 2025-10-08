from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('register_page', views.register_page, name='register_page'),
    path('logout_page',views.logout_page, name='logout_page'),
    path('profile',views.profile, name='profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('change_password', views.change_password, name='change_password')
]