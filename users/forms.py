from django import forms
from .models import Student,Marketing_Coordinator,Marketing_Manager,User,Faculty
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm


class StudentRegisterForm(UserCreationForm):
    CHOICES=[('M','Male'),('F','Female')]
    roles=(('S','Student'),('MC','Marketing Coordinator'),('MM','Marketing Manager'))
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    role = forms.ChoiceField(initial='S',widget = forms.HiddenInput,choices=roles)
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={"class" : "form-control", "id" : "setting-input-1"}))
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={"class" : "form-control", "id" : "setting-input-1"}))

    class Meta:
        model = Student
        fields = ('image', 'name','role','gender','student_number','faculty','phone_number','address','email','password1')

        widgets = {
            'name' : forms.TextInput(attrs={"class" : "form-control", "id" : "setting-input-1", 'autofocus':True}),
            'image' : forms.FileInput(attrs={'accept': "image/*", 'onchange' : "loadFile(event)", "id" : "my-file-selector"}),
            'last_name' : forms.TextInput(attrs={"class" : "form-control", "id" : "setting-input-1"}),
            'student_number' : forms.TextInput(attrs={"class" : "form-control",  "id" : "setting-input-1"}),
            'faculty' : forms.Select(attrs={"class" : "form-control", "id" : "setting-input-1"}),
            'phone_number' : forms.NumberInput(attrs={"class" : "form-control", "id" : "setting-input-1"}),
            'address' : forms.Textarea(attrs={"class" : "form-control", "id" : "exampleFormControlTextarea5", 'style':'height:100px;'}),
            'email' : forms.EmailInput(attrs={"class" : "form-control", "id" : "setting-input-1", 'autofocus':False}),
            'password1' : forms.PasswordInput(render_value = True,attrs={"class" : "form-control", "id" : "setting-input-1"}),
            'password2' : forms.PasswordInput(attrs={"class" : "form-control", "id" : "setting-input-1"}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is already taken")
        return email  

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        # if len(password1) <= 9:
        #     raise forms.ValidationError("Password must be at least 8 words")
        return password2

        
class StudentUpdateForm(UserChangeForm):
    CHOICES=[('M','Male'),('F','Female')]
    roles=(('S','Student'),('MC','Marketing Coordinator'),('MM','Marketing Manager'))
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    role = forms.ChoiceField(initial='S',widget = forms.HiddenInput,choices=roles)

    class Meta:
        model = Student
        fields = ('image', 'name','role','gender','student_number','faculty','phone_number','address','email')

        widgets = {
            'name' : forms.TextInput(attrs={"class" : "form-control", "id" : "setting-input-1", 'autofocus':True}),
            # 'image' : forms.FileInput(attrs={'accept': "image/*", 'onchange' : "loadFile(event)", "id" : "my-file-selector"}),
            'last_name' : forms.TextInput(attrs={"class" : "form-control", "id" : "setting-input-1"}),
            'student_number' : forms.TextInput(attrs={"class" : "form-control",  "id" : "setting-input-1"}),
            'faculty' : forms.Select(attrs={"class" : "form-control", "id" : "setting-input-1"}),
            'phone_number' : forms.NumberInput(attrs={"class" : "form-control", "id" : "setting-input-1"}),
            'address' : forms.Textarea(attrs={"class" : "form-control", "id" : "exampleFormControlTextarea5", 'style':'height:100px;'}),
            'email' : forms.EmailInput(attrs={"class" : "form-control", "id" : "setting-input-1", 'autofocus':False}),
        }

class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={"id":"signin-password", "name":"signin-password", "class":"form-control signin-password", "placeholder":"Email", "required":"required"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"id":"signin-password", "name":"signin-password", "class":"form-control signin-password", "placeholder":"Password", "required":"required"}),
    )



