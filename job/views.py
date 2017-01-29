from django.views import generic
from .models import Job
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'job/index.html'

    def get_queryset(self):
        return Job.objects.all()

class DetailView(generic.DetailView):
    model = Job
    template_name = 'job/detail.html'

class JobCreate(CreateView):
    model = Job
    fields = ['title', 'description', 'contact', 'image']

class JobUpdate(UpdateView):
    model = Job
    fields = ['title', 'description', 'contact', 'image']

class JobDelete(DeleteView):
    model = Job
    success_url = reverse_lazy('job:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'job/registrationForm.html'
    # Displays blank form if new user
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    # Process Registration form data
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
    # returned user object if correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('job:index')
            return render(request, self.template_name, {'form': form})