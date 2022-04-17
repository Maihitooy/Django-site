from django.shortcuts import render
from .forms import DataForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    else:
        form = DataForm()
    return render(request, 'main/index.html', {'form': form})
