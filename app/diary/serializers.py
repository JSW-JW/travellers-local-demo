from rest_framework import serializers
from diary import models


class DiaryImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DiaryImage
        fields = ('image', 'thumbnail', 'diary')


class DiarySerializer(serializers.ModelSerializer):
    """Serializes a diary object"""
    image_set = DiaryImageSerializer(many=True, required=False)

    class Meta:
        model = models.Diary
        fields = ('target', 'title', 'description', 'user', 'image_set')
        extra_kwargs = {
            'user': {'required': False}
        }
