from .models import Essay
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Essay
        fields = '__all__'