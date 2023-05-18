from django import forms
from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields='__all__'
        widgets={
            "vehicle_number":forms.TextInput(attrs={"class":"form-control "}),
            "vehicle_type":forms.Select(attrs={"class":"form-select"}),
            "vehicle_model":forms.TextInput(attrs={"class":"form-control "}),
            "vehicle_description":forms.TextInput(attrs={"class":"form-control "}),
                    
        }