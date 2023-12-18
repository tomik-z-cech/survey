from django import forms
from .models import SurveyResponse

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = ['name','nationality', 'item', 'description']