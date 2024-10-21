from django.urls import path
from . import views
from .views import custom_login_view, custom_logout_view, register, choice, explore


urlpatterns = [
 
    path('', views.mainpage, name='mainpage'), 
    path('login/', custom_login_view, name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('register/', register, name='register'),

    path('choice/', choice, name='choice'),
    path('explore/', explore, name='explore'),

]