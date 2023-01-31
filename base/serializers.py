from rest_framework import serializers
from .models import Advocate

class AdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = ['username', 'bio']