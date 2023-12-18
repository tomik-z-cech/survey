from django import forms
from .models import SurveyResponse

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = ['name','country_of_birth', 'item', 'description']
        
    name = forms.CharField(
        label='Name',
        help_text='Please enter your full name as it appears on your Facebook profile. This information will help me identify and personalize your responses and contact you in case of you win ;)'
    )
    
    country_of_birth = forms.CharField(
        label='Country of birth',
        help_text='Kindly provide your country of birth. This allows me to understand the diverse backgrounds of locals or expats living in Ireland and helps me tailor my school project better in the world of international community.'
    )

    item = forms.CharField(
        label='Item Missed in Ireland',
        help_text='Share the specific item or thing that you miss the most while living in Ireland. Whether it\'s a cultural aspect, a food item, or a particular service, your response gives me valuable insights into the aspects of locals seen while on holiday or expats find most meaningful from their home countries.'
    )

    description = forms.CharField(
        label='Reason (Description)',
        help_text='Please provide a brief description of why you miss the chosen item in Ireland. Whether it\'s the cultural significance, unique features, or personal memories associated with the item, your insights help me understand the impact of these elements.',
        widget=forms.Textarea
    )