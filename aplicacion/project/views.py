from django.shortcuts import render

# Create your views here.
def inicio (request):
    return render(request, 'index.html')
def deportes (request):
    return render(request, 'deportes.html')

def quienessomos (request):
    return render(request, 'quienessomos.html')
def instalaciones (request):
    return render(request, 'instalaciones.html')