from django.forms import ModelForm
from collection.models import Places

class PlaceForm(ModelForm):
	class Meta:
		model = Places
		fields = ('name', 'description',)