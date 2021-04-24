from django.shortcuts import render
from .forms import GuardianForm


def index(request):
    form = GuardianForm()

    if request.method == 'POST':
        form = GuardianForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'guardians/home.html', context)