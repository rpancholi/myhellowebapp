from django.shortcuts import render, redirect
from collection.models import Places
from collection.forms import PlaceForm

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

def edit_place(request, slug):
	place = Places.objects.get(slug=slug)
	
	form_class = PlaceForm
	
	if request.method == 'POST':
		form = form_class(data=request.POST, instance=place)
		if form.is_valid():
			form.save
			return redirect('place_detail', slug=place.slug)
	else:
		form = form_class(instance=place)
	
	return render(request, 'places/edit_place.html', {
		'place': place,
		'form': form,
	})
	