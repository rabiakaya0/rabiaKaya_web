from django import forms
from . models import Contact
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    konu = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Konu',
        'label': 'Konu'
    })) 
    isim = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'İsminiz',
        'label': 'İsim Soyisim'
    })) 
    eposta = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'E-Posta',
        'label': 'E-Posta'
    })) 
    mesaj = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Mesajınız',
        'label': 'Mesaj',
        'rows': 15,  
        'maxlength': 500
    }))
    class Meta:
        model = Contact
        fields = ['isim', 'eposta', 'mesaj']
    def save(self, konu, isim, eposta, mesaj):
        
        send_mail(
            konu,
            f'İsim: {isim} \nMesaj: {mesaj} \nMail Adresi: {eposta}',
            settings.EMAIL_HOST_USER,  
            ['admin@rabiakaya.com'],
            fail_silently=False,
        )