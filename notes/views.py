from ast import Not
from dataclasses import field
from pyexpat import model
from statistics import mode
from unittest import mock
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView

from .models import Notes

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title','text']
    success_url = '/smart/notes'

class NotesListView(ListView):
    template_name = 'notes/notes_list.html'
    model = Notes
    context_object_name = 'notes'
     
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request,'notes/notes_list.html',{'notes':all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name ='note'

# def detail(request, pk):
#     try:
#         notes = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_detail.html',{'note':notes})