from django.shortcuts import render
from django.views.generic import ListView
from .models import Dog


class DogsListView(ListView):
    model = Dog
    template_name = 'base/base.html'
    context_object_name = 'dogs'

    def get_queryset(self):
        all_dogs = Dog.objects.all()
        return all_dogs

