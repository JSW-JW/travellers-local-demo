from rest_framework import serializers
from diary import models
from easy_thumbnails.templatetags.thumbnail import thumbnail_url


class ThumbnailSerializer(serializers.ImageField):

    def __init__(self, alias):
        self.alias = alias

    def to_representation(self, instance):
        return thumbnail_url(instance, self.alias)


class DiaryImageSerializer(serializers.ModelSerializer):
    """Serializes diary-images"""
    image = ThumbnailSerializer(alias='image')
    thumb = ThumbnailSerializer(alias='thumb')

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
