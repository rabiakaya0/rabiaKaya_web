from django.urls import path
from pages.views import IndexView, WhoView, ElectricView, ElectronicView, SoftwareUnityView, SoftwareDjangoView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('kimdir', WhoView.as_view(), name="kimdir"),
    path('elektrik', ElectricView.as_view(), name="elektrik"),
    path('elektronik', ElectronicView.as_view(), name="elektronik"),
    path('yazilim/unity', SoftwareUnityView.as_view(), name="yazilimUnity"),
    path('yazilim/django', SoftwareDjangoView.as_view(), name="yazilimDjango"),
]