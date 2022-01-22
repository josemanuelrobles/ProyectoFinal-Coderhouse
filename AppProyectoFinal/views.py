from xml.dom import HierarchyRequestErr
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse 
from django.template import Context,Template



# class Inicio (TemplateView):
#     template_name= "Inicio.html"

def inicio(self):
    miHtml=open("C:/Users/jm_12/OneDrive/Escritorio/Proyecto Entrega Final/AppProyectoFinal/templates/AppProyectoFinal/Inicio.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)
    