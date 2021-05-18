from rest_framework import serializers
from .models import freq


class FreqSerializers(serializers.ModelSerializer):
    class Meta:
        model = freq
        fields = ['freq_url', 'content']
