from django.shortcuts import render
from .forms import GetNameForm
# from django.http import HttpResponse


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Michal'})


def show_name_form(request):
    form = GetNameForm()
    if request.method == "POST":
        form = GetNameForm(request.POST)
        if form.is_valid():
            return render(request, 'hello.html',
                          form.cleaned_data)
        else:
            print('ERROR')
    return render(request, 'name-form.html', {'form': form})
