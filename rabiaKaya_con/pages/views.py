from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class WhoView(TemplateView):
    template_name = 'kimdir.html'

class ElectricView(TemplateView):
    template_name = 'elektrik.html'

class ElectronicView(TemplateView):
    template_name = 'elektronik.html'

class SoftwareUnityView(TemplateView):
    template_name = 'yazilimUnity.html'

class SoftwareDjangoView(TemplateView):
    template_name = 'yazilimDjango.html'

class ContactView(TemplateView):
    template_name = 'iletisim.html'
