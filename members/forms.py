from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator


class SignUpForm(UserCreationForm):

    aadhar_no = forms.CharField(max_length=12, validators=[RegexValidator(r'^\d{1,10}$')], required=True, help_text='')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address',required=True)
    
    # following condition added for unique email address.

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        print(User.objects.filter(email=email).count())
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(u'This email address is already registered.')
        return email


    #def save(self, commit=True):
     #   user = super(SignUpForm, self).save(commit=False)
     #   user.extra_field = self.cleaned_data["aadhar_no"]
     #   if commit:
      #      user.save()
      #  return user

    class Meta:
        model = User
        fields = [
            'username',
            'aadhar_no',
            'first_name',
            'last_name',
            'email', 
            'password1', 
            'password2', 
        ]
