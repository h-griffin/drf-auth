from rest_framework import serializers

from .models import Fish

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name','catcher','description','created_at')
        model = Fish

        
        