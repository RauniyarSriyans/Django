from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("My name is Sriyans")

def dynamicHello(request, first_name):
    return HttpResponse(f"Hello {first_name}")

def addNumbers(request, num1, num2):
    return HttpResponse(f"The total is {num1 + num2}")

# ----------------------------------------------------------------------

# everything below is for movies 

def indexMovies(request):
    context = {
        'movies': ['Gladiator', 'StarWar', 'KGF', 'bhootiya', 'chutoya', 'Randibaaz']
    }
    return render(request, 'my_first_app/index.html', context)


