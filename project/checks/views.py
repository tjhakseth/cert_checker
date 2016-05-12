from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Website
from .forms import WebsiteInputForm


def index(request):
    form = WebsiteInputForm

    if request.method == 'POST':
        form = WebsiteInputForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        else:
            messages.error(request, "Error")

    return render(request, 'index.html', {'form': form})
    