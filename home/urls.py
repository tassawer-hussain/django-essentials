from django.urls import path

from . import views

urlpatterns = [
    # path('home', views.home),
    # path('authorized', views.authorized),
    path('', views.HomeView.as_view(), name='home'),
    path('authorized', views.AuthorizedView.as_view(), name='authorized'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]