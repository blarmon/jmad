from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from solos.models import Solo


# Create your views here.
def index(request):
    context = {'solos': []}

    if request.GET.keys():
        solos_queryset = Solo.objects.all()

        if request.GET.get('instrument'):
            solos_queryset = solos_queryset.filter(instrument=request.GET['instrument'])

        if request.GET.get('artist', None):
            solos_queryset = solos_queryset.filter(artist=request.GET['artist'])

        context['solos'] = solos_queryset

    return render_to_response('solos/index.html', context)
