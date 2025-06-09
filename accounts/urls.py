from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signupPage'),
    path('login/', views.LoginPageView.as_view(), name='loginPage'),
    path('logout/', LogoutView.as_view(), name='logoutPage'),
]
