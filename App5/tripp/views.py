from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Trip, Note

# Create your views here.
class HomeView(TemplateView):
    template_name = 'tripp/index.html'

def TripsList(request):
    trips = Trip.objects.all()
    context = {
        'trips': trips
    }
    return render(request, 'tripp/trips_list.html', context)