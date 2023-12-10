from django.shortcuts import render
from .models import Status


def select_data(request):
    data = Status.objects.all()
    context = {'data': data}
    return render(request, 'status.html', context)


def display_data(request):
    if request.method == 'POST':
        selected_crimes = request.POST.getlist('crime')
        data = Status.objects.filter(범죄대분류__in=selected_crimes)
    else:
        data = Status.objects.all()

    context = {'data': data}
    return render(request, 'statusdata.html', context)
