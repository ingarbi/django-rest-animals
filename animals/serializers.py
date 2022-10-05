from rest_framework import serializers
from .models import Animals

class AnimalsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Animals
        fields = "__all__"