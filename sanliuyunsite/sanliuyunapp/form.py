from django import forms
from django.core.exceptions import ValidationError
from sanliuyunapp.models import Person

def word_length(password):
    if len(password)<6 or len(password)>20:
        raise ValidationError('密码字数请设置在6位到20位之间')

class loginForm(forms.Form):
    inputName = forms.CharField(
    widget=forms.TextInput(attrs={'placeholder':'昵称/邮箱地址'}),
    max_length=25,
    label='昵称/邮箱地址',
    error_messages={'required': '昵称/邮箱地址不能为空哦~'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs  = {'placeholder':'密码'}),
        max_length=25,
        validators = [word_length],
        label = '密码',
        error_messages={'required': '请填写密码！'}
    )


class registerForm(forms.Form):
    nickname = forms.CharField(
    widget=forms.TextInput(attrs={'placeholder':'昵称'}),
    max_length=25,
    label='昵称',
    error_messages={'required': '昵称不能为空哦~'}
    )
    email_address = forms.CharField(widget=forms.EmailInput(attrs  = {'placeholder':'邮箱地址'}),label='邮箱地址',error_messages={'required': '请填写正确的邮箱！'}
)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs  = {'placeholder':'密码'}),
        max_length=25,
        validators = [word_length],
        label = '密码',
        error_messages={'required': '请填写密码！'}
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs  = {'placeholder':'确认密码'}),
        max_length=25,
        validators = [word_length],
        label = '确认密码',
        error_messages={'required': '请填写密码！'}

        )
