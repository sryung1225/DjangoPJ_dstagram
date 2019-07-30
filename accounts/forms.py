from django.contrib.auth.models import User
from django import forms

#회원 가입 양식 출력
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput) #비밀번호 입력
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput) #비밀번호 재입력

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self): #검사
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']