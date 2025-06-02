from django.urls import path
from . import views

urlpatterns = [

    # Authentication URLs
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),



    # Home view
    path('', views.home_view, name='home'),
    path('profile/', views.profile, name='profile'),
    path('users/', views.users_list, name='users_list'),
    path('notifications/', views.notifications, name='notifications'),
    path('messages/', views.messages, name='messages'),
    path('search/', views.search_view, name='search'),
    path('friends/', views.friends_view, name='friends'),
    path('saved/', views.saved_view, name='saved'),
    path('groups/', views.groups_view, name='groups'),
    path('watch/', views.watch_view, name='watch'),
    path('memories/', views.memories_view, name='memories'),
    path('explore/', views.explore_view, name='explore'),
    path('events/', views.events_view, name='events'),
    path('gaming/', views.gaming_view, name='gaming'),
    

]
