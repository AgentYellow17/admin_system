from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Role, Link
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from user.models import UserManager, User
from user.forms import SignUpForm


@login_required(login_url = '/accounts/login')
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_links = Link.objects.all().count()
    current = request.user
    if(current.is_staff):
      if(current.is_superuser):
        permission = 'Superuser'
      else:
        if(current.groups.all().count() == 1):
          permission = current.groups.get()
        else:
          permission = request.user.groups.exclude(name = 'Global').get()
    else:
      permission = 'Permission pending'
    context = {
        'num_links': num_links,
        'permission': permission,
    }
    return render(request, 'index.html', context = context)

class LinkListView(ListView):
  template_name = 'link/link_list.html'
  def get_queryset(self):
    group = list(self.request.user.groups.all())
    return Link.objects.filter(role__category__in = group)

class LinkDetailView(generic.ListView):
    model = Link

def signup(request):
    if(request.method == 'POST'):
      form = SignUpForm(request.POST)
      if form.is_valid():
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(email = email, password=password)
        return redirect('index')
    else:
        form = SignUpForm
    return render(request, 'signup.html', {'form': form})