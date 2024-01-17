from rest_framework import serializers
from .models import PlayerScore

class PlayerScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerScore
        fields = '__all__'
