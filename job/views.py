from django.shortcuts import render, get_object_or_404
from .models import Job

def index(request):
    all_jobs = Job.objects.all()
    html = ''
    for job in all_jobs:
        url = '/job/' + str(job.id) + '/'
        html += '<a href="' + url + '">'+ job.title + '</a<br>'
        return render(request, 'job/index.html', {'all_jobs': all_jobs,})

def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'job/detail.html', {'job': job})