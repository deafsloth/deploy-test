from rest_framework import serializers
from .models import TargetImg

class TargetImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetImg
        fields = '__all__'