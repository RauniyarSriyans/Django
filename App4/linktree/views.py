from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Profile, Link

# Create your views here.
class LinkListView(ListView):
    model = Link
    template_name = 'link_list.html'

class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy('link-list')

class LinkUpdateView(UpdateView):
    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('link-list')

class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('link-list')

def ProfileView(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        'profile': profile, 
        'links': links
    }
    return render(request, 'linktree/profile.html', context)
