from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Activity
from captcha.fields import ReCaptchaField


class UserRegistrationForm(UserCreationForm):
    captcha = ReCaptchaField()
    ACTIVITY_CHOICES = (
        ('education', 'Education'),
        ('recreational', 'Recreational'),
        ('social', 'Social'),
        ('diy', 'DIY'),
        ('charity', 'Charity'),
        ('cooking', 'Cooking'),
        ('relaxation', 'Relaxation'),
        ('music', 'Music'),
        ('busywork', 'Busywork'),
    )
    
    selected_activity = forms.ChoiceField(choices=ACTIVITY_CHOICES)
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'selected_activity')

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_name']