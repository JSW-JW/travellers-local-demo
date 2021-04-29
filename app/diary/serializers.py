from rest_framework import serializers
# from easy_thumbnails_rest.serializers import ThumbnailerSerializer
from diary import models

class DiarySerializer(serializers.ModelSerializer):
    """Serializes a diary object"""

    class Meta:
        model = models.Diary
        fields = ('id', 'title', 'description')


class DiaryImageSerializer(serializers.ModelSerializer):
    """Serializes diary-images"""
    # image = ThumbnailSerializer(alias='image')
    # avatar = ThumbnailSerializer(alias='avatar', source='image')
