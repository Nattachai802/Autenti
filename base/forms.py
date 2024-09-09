from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    contact_number = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'contact_number', 'password1', 'password2']
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('ชื่อผู้ใช้นี้ถูกใช้ไปแล้ว')
        return username
    def clean(self):
        clean_data = super().clean()
        password1 = clean_data.get('password1')
        password2 = clean_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2','รหัสผ่านไม่ตรงกัน')




        