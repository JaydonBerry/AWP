from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Job

def index(request):
    all_jobs = Job.objects.all()
    html = ''
    for job in all_jobs:
        url = '/job/' + str(job.id) + '/'
        html += '<a href="' + url + '">'+ job.title + '</a<br>'
        return render(request, 'job/index.html', {'all_jobs': all_jobs,})

def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
    except Job.DoesNotExist:
        raise Http404("Job does not exist")
    return render(request, 'job/detail.html', {'job': job})