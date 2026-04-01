#crop recommendation form
from django import forms

class CropForm(forms.Form):
    N = forms.FloatField(label="Nitrogen")
    P = forms.FloatField(label="Phosphorus")
    K = forms.FloatField(label="Potassium")
    temperature = forms.FloatField(label="Temperature (°C)")
    humidity = forms.FloatField(label="Humidity (%)")
    ph = forms.FloatField(label="Soil pH")
    rainfall = forms.FloatField(label="Rainfall (mm)")