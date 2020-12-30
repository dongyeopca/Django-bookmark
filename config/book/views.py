from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView
from .models import Bookmark
from django.urls import reverse_lazy

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 5
    # template_name = 'bookmark_list.html'

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark
    
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')


