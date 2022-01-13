from rest_framework import serializers

from .models import Dragon

class DragonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dragon
    fields = ('spotter', 'name_of_dragon', 'title', 'color', 'age', 'estimated_height', 'descritption_of_dragon')