from django import forms
from KotlinApp.models import Appointment,ImageModel

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields ='__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'