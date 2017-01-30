from django.views import generic
from .models import Job
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db import models
from django.contrib.auth.models import User

class IndexView(generic.ListView):
    template_name = 'job/index.html'

    def get_queryset(self):
        return Job.objects.all()

class ProfileView(generic.ListView):
    template_name = 'job/registrationForm.html'
    fields = ['username', 'email', 'first_name', 'last_name']

    def get_queryset(self):
        return User.objects.all()

class DetailView(generic.DetailView):
    model = Job
    template_name = 'job/detail.html'

class JobCreate(CreateView):
    model = Job
    fields = ['title', 'description', 'contact', 'location', 'image']

class JobUpdate(UpdateView):
    model = Job
    fields = ['title', 'description', 'contact', 'location', 'image']

class JobDelete(DeleteView):
    model = Job
    success_url = reverse_lazy('job:index')

class UserCreate(CreateView):
    model = User
    fields = ['username', 'email', 'password', 'first_name', 'last_name']
    template_name = 'job/registrationForm.html'
    success_url = reverse_lazy('job:profile')