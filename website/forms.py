from django import forms
from django.forms.widgets import EmailInput, NumberInput, TextInput, Textarea
from .models import ContactInfo

# Create your forms here.
class ContactForm(forms.ModelForm):
    # Meta data
    class Meta:
        model  = ContactInfo
        fields = [
            'name',
            'phone',
            'email',
            'subject',
            'message'
        ]

        # Definition of widgets
        widgets = {
            'name': TextInput(
                attrs={
                    'name': 'name',
                    'class': 'form-control',
                    'id': 'name',
                    'placeholder': 'Name and surname',
                }
            ),

            'phone': NumberInput(
                attrs={
                    'name': 'phone',
                    'class': 'form-control',
                    'id': 'phone',
                    'placeholder': 'Phone number',
                }
            ),

            'email': EmailInput(
                attrs={
                    'name': 'email',
                    'class': 'form-control',
                    'id': 'email',
                    'placeholder': 'Email address',
                }
            ),

            'subject': TextInput(
                attrs={
                    'name': 'subject',
                    'class': 'form-control',
                    'id': 'subject',
                    'placeholder': 'Message Subject...',
                }
            ),

            'message': Textarea(
                attrs={
                    'name': 'message',
                    'rows': '8',
                    'class': 'form-control',
                    'placeholder': 'Message...',
                }
            ),
        }