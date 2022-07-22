

from dataclasses import fields

from .models import Persona
from rest_framework import serializers

class PersonaSerializer(serializers.ModelSerializer):
   class Meta:
      model = Persona
      fields='__all__'


   # def to_representation(self, instance):
   #    return {
   #       "type_document": instance["type_document"],
   #       "document": instance["document"],
   #       "name":instance["name"],
   #       "last_name":instance["last_name"],
   #       "hobbie":instance["hobbie"],
   #    }

