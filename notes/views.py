from django.shortcuts import render
from django.http import Http404


from django.views.generic import DetailView, ListView

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

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"