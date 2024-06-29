"""
URL configuration for FurnitureMGM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as uviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', uviews.SignupPage, name='signup'),
    path('login/', uviews.LoginPage, name='login'),
    path('logout/', uviews.LogoutPage, name='logout'),
    path('change-password/<str:token>/', uviews.ChangePassword, name='change_password'),
    path('forgot-password/', uviews.ForgotPassword, name='forgot_password'),
    path('profile/', uviews.ProfilePage, name='profile'),
    path('profile/update/', uviews.profile_update, name='profile_update'),
    path('', uviews.landingpage, name='landingpage'),
]
