from django.views import generic
from.models import Job

class IndexView(generic.ListView):
    template_name = 'job/index.html'

    def get_queryset(self):
        return Job.objects.all()

class DetailView(generic.DetailView):
    template_name = 'job/index.html'

    def get_queryset(self):
        model = Job
        template_name = 'job/detail.html'