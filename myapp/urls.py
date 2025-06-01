from django.urls import path
from . import views

urlpatterns = [

    # Authentication URLs
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),



    # Home view
    path('', views.home_view, name='home'),
]
