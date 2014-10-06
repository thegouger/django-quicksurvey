from survey.models import Choice
from django.forms import ModelForm

class ChoiceForm(ModelForm):
	class Meta:
		model = Choice
		fields = ['text', 'program']
		
