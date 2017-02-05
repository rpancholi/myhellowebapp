from django.shortcuts import render
from collection.models import Places

# Create your views here.
def index(request):
	places = Places.objects.all()
	
	return render(request, 'index.html', {
		'places': places,
	})

def place_detail(request, slug):
	place = Places.objects.get(slug = slug)
	
	return render(request, 'places/place_detail.html', {
		'place': place,
	})