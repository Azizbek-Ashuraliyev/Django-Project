from django.http import Http404, HttpResponseRedirect
from django.views.generic import CreateView,UpdateView, ListView, DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm 
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url()) 
    
class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm 

class NotesListView(LoginRequiredMixin,ListView):
    template_name = 'notes/notes_list.html'
    model = Notes
    context_object_name = 'notes'
    login_url = '/admin'
    
    def get_queryset(self):
        return self.request.user.notes.all()
     
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