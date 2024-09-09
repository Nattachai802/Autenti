
from .views import *
from django.urls import path , include
from django.contrib.auth import views as auth_views


app_name = 'base'


urlpatterns = [
    path('signup/', UserRegisterview.as_view() , name='UserRegisterview'),
    path('login/',Userloginview.as_view(), name='logintoweb'),
    path('accounts/',include('django.contrib.auth.urls')),
    
    path('password-reset/', ResetPasswordview.as_view(), name='password_reset'),
    
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',
                                                     success_url=reverse_lazy('base:password_reset_complete')),
         name='password_reset_confirm'),
    
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    
    ]
