from django import forms
from . models import subscribers, Mailmessage

class SubscibersForm(forms.ModelForm):
    email = forms.EmailField(label='',
            widget=forms.EmailInput(
                    attrs={'placeholder':'Put your email',
                     'class':'form-control'
            }

    ))
    
    class Meta:
        model = subscribers
        fields = ['email', ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
       
        qs = subscribers.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError('uhpss!! \U0001F644 this email already exists ')
        return email
        