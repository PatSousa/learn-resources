from rest_framework import serializers

from learning.models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('added', 'name', 'url', 'short_description', 'tags')
