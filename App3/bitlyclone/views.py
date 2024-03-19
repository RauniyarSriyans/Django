from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Link
from .forms import LinkForm

# Create your views here.
def home_page(request):
    linklist = Link.objects.all()
    context = {
        'links': linklist
    }
    return render(request, 'bitlyclone/index.html', context)

def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()
    return redirect(link.url)

def add_link(request):
    if request.method == 'POST':
        # form has data 
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = LinkForm()
    context = {
        'form': form
    }
    return render(request, 'bitlyclone/create_link.html', context)