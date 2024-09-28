from django.shortcuts import render
from .models import Project
def portfolio(request):
    projects = Project.objects.all() 
    return render(request, "portfolio/portfolio.html", # <=====
        {'projects':projects}) 
#el diccionario nos permite ir agregando proyectos
# Create your views here.

