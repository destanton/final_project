from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, User
from django.urls import reverse_lazy, reverse

from sherlock.models import Profile, About


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("index_view")


class IndexView(TemplateView):
    template_name = "index.html"


class ProfileView(ListView):
    model = Profile
