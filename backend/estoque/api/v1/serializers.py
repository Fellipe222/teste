from estoque import models
from rest_framework import serializers

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = '__all__'