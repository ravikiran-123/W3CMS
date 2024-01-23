from django import forms
from dashboard.users.models import CustomUser
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = (
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2',
                )
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


#Add User Form
class CustomUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    dob = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    
    GENDER_CHOICES = (
        ('','Choose gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)


    class Meta:
        model = CustomUser
        fields = ( 
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'gender',
                  'avatar',
                  'dob',
                  'phone_number',
                  'groups',
                  'about',
                  'is_active',
                  'facebook_url',
                  'twitter_url',
                  'linkedin_url',
                  'password1',
                  'password2',
                )
        widgets = {
            'avatar': forms.FileInput(),
        }
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    dob = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(),required=False)
   
    GENDER_CHOICES = (
        ('','Choose gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = (
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'gender',
                  'avatar',
                  'dob',
                  'phone_number',
                  'groups',
                  'about',
                  'is_active',
                  'facebook_url',
                  'twitter_url',
                  'linkedin_url',
                )

        widgets = {
            'avatar': forms.FileInput(),
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save()
        return user




class LoginForm(forms.Form):
    email =  forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data
        
    def login(self, request):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        return user
        

class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not CustomUser.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError("There is no user registered with the specified email address!")
        return email


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name','permissions')

class PermissionsForm(forms.ModelForm):
    name = forms.CharField(label='Name', help_text="Example: Can action modelname")
    codename = forms.CharField(label='Code Name', help_text="Example: action_modelname")

    class Meta:
        model = Permission
        fields = ('name','codename','content_type')


class UserPermissionsForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('user_permissions',)



