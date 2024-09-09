from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.contrib.auth.views import LoginView, LogoutView , PasswordResetView
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm


class UserRegisterview(CreateView):
    form_class = UserRegisterForm
    template_name = r'register.html'
    success_url = reverse_lazy('base:logintoweb')
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'สมัครสมาชิกสำเร็จ! กรุณารอสักครู่...')
        return self.render_to_response(self.get_context_data(form=form))
    
def form_invalid(self, form):
    messages.error(self.request, 'เกิดข้อผิดพลาดในการลงทะเบียน กรุณาตรวจสอบข้อมูลอีกครั้ง.')
    return self.render_to_response(self.get_context_data(form=form))

class Userloginview(LoginView):
    template_name = r'login.html'

class ResetPasswordview(SuccessMessageMixin,PasswordResetView):
    template_name = r'password_reset.html'
    email_template_name = r'password_reset_email.html'
    subject_template_name = r'image\password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('base:logintoweb')