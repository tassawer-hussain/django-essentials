from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect


from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse

from .forms import NotesForm
from .models import Notes

# Create your views here.
# def list(request):
#     all_notes = Notes.objects.all()
#     return render( request, 'notes/notes_list.html', { 'notes': all_notes } )

# def detail( request, pk ):
#     try:
#         note = Notes.objects.get( pk=pk )
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render( request, 'notes/notes_detail.html', { 'note': note } )

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes" # defualt is object. This will be use in the template file to render the data
    template_name = "notes/notes_list.html" # we can skip this because it's django naming standards

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes" # defualt is object. This will be use in the template file to render the data
    template_name = "notes/popular_notes_list.html" # we can skip this because it's django naming standards
    queryset = Notes.objects.filter(likes__gte=1)

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

class NotesCreateView(CreateView):
    model = Notes
    # fields = [ 'title', 'text' ]
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

def add_like_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse("notes.detail", args=(pk,)))
    raise Http404