from django.shortcuts import render
from .models import Persona
from rest_framework import viewsets
from .serializers import PersonaSerializer
# Create your views here.

class PersonasViewset(viewsets.ModelViewSet):
   serializer_class = PersonaSerializer
   queryset= Persona.objects.all()
