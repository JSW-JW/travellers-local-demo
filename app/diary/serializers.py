from rest_framework import serializers
from diary import models


class DiaryImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DiaryImage
        fields = ('id', 'image', 'diary')
        read_only_fields = ('id',)
        extra_kwargs = {'diary': {'required': False}}


class DiarySerializer(serializers.ModelSerializer):
    """Serializes a diary object"""
    image_set = DiaryImageSerializer(many=True, required=False)

    class Meta:
        model = models.Diary
        fields = ('id', 'target', 'title', 'description', 'user', 'image_set')
        read_only_fields = ('id',)
