<<<<<<< HEAD
=======
from dataclasses import fields
>>>>>>> 311a2a502f7fe1b8b72a7a081fcf49d64aebb43d
from .models import Persona
from rest_framework import serializers

class PersonaSerializer(serializers.ModelSerializer):
   class Meta:
      model = Persona
      fields='__all__'

<<<<<<< HEAD
 
=======
   # def to_representation(self, instance):
   #    return {
   #       "type_document": instance["type_document"],
   #       "document": instance["document"],
   #       "name":instance["name"],
   #       "last_name":instance["last_name"],
   #       "hobbie":instance["hobbie"],
   #    }
>>>>>>> 311a2a502f7fe1b8b72a7a081fcf49d64aebb43d
