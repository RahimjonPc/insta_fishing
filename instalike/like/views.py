from django.shortcuts import render, redirect
from .models import Fishing
from .forms import FishingForm


def index(request):
    if request.method == 'POST':
        form = FishingForm(request.POST)
        if form.is_valid():
            form.save()
            


    form = FishingForm()
    context = {
        'form': form
    }
    return render(request, 'like/index.html', context)
