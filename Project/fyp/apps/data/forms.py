from dataclasses import fields
from django import forms
from pkg_resources import require

from apps.authentication.models import CustomUser

from .models import ClassSchedule, GymPlan, UserBooking


class PlanForm(forms.ModelForm):
    plan_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Plan Name",
                "class": "form-control"
            }
        ))
    plan_duration = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Plan Duration",
                "class": "form-control"
            }
        ))
    plan_cost = forms.FloatField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Plan Cost",
                "class": "form-control"
            }
        ))
    
    class Meta:
        model = GymPlan
        fields = [
            'plan_name',
            'plan_duration',
            'plan_cost'
        ]
        
        
class UserBookingForm(forms.ModelForm):
    plan_type = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "class" : "form-control"
            },
        ),
        queryset=GymPlan.objects.all(),
        empty_label='No Gym Plan Available',
        required=True,
    )

    payment_method = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={},
        ),
        choices={
            'khalti' : 'Khalti',
            'esewa' : 'E-Sewa'
        },
        required=False
    )
    
    class Meta:
        model = UserBooking
        fields = ['plan_type', 'payment_method']
        

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email Address",
                "class": "form-control"
            }
        ))
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address",
                "class": "form-control"
            }
        ))
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "City",
                "class": "form-control"
            }
        ))
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Country",
                "class": "form-control"
            }
        ))
    postal_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Postal Code",
                "class": "form-control"
            }
        ))
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'address',
            'city',
            'country',
            'postal_code'
        ]
        
class UserForm(ProfileForm):
    CLIENT = 'CL'
    FITNESS_INSTRUCTOR = 'FI'
    
    USER_TYPE_CHOICES = [
        (CLIENT, 'Client'),
        (FITNESS_INSTRUCTOR, 'Fitness Instructor'),
    ]
    
    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        widget=forms.Select(
            attrs={
                "placeholder": "Postal Code",
                "class": "form-control"
            }
        )
        )
    
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'address',
            'city',
            'country',
            'postal_code',
            'is_superuser',
            'user_type'
        ]

class ClassScheduleForm(forms.ModelForm):
    class_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control'
            }
        ),
        required=False
    )
    class_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control'
            }
        ),
        required=False
    )
    class_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'class' : 'form-control', 
                'type' : 'datetime-local'
            },
        ),
        required=True
    )
    tutor_id = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(user_type="FI"),
        widget=forms.Select(
            attrs={
                'class' : 'form-control', 
            },
        ),
        required=True
    )
    
    class Meta:
        model = ClassSchedule
        fields = [
            'class_name',
            'class_description',
            'class_date',
            'tutor_id',
        ]