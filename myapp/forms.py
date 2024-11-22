from django import forms
from .models import TrafficViolations, TrafficCameras, Drivers, Vehicles


class TrafficViolationsForm(forms.ModelForm):
    driver = forms.ModelChoiceField(
        queryset=Drivers.objects.all(),  # Query to retrieve all driver records
        widget=forms.Select,
        label="Driver",
        required=True
    )

    vehicle = forms.ModelChoiceField(
        queryset=Vehicles.objects.all(),  # Query to retrieve all vehicle records
        widget=forms.Select,
        label="Vehicle",
        required=True
    )

    camera = forms.ModelChoiceField(
        queryset=TrafficCameras.objects.all(),  # Query to retrieve all camera records
        widget=forms.Select,
        label="Camera",
        required=True
    )

    class Meta:
        model = TrafficViolations
        fields = ['violation_id', 'driver', 'vehicle', 'camera', 'violation_type', 'fine_amount', 'violation_date',
                  'violation_time', 'penalty_points', 'location']
        widgets = {
            'violation_date': forms.DateInput(attrs={'type': 'date'}),
            'violation_time': forms.TimeInput(attrs={'type': 'time'}),
        }