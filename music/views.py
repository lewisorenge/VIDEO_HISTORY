from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import music
from history.mixins import ObjectViewMixin

class musicList(ListView):
    model = music

class MusicDetail(ObjectViewMixin, DetailView):
    model = music
