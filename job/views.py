from django.views import generic
from.models import Job
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class IndexView(generic.ListView):
    template_name = 'job/index.html'

    def get_queryset(self):
        return Job.objects.all()

class DetailView(generic.DetailView):
    model = Job
    template_name = 'job/detail.html'

class JobCreate(CreateView):
    model = Job
    fields = ['username' , 'title' , 'description']