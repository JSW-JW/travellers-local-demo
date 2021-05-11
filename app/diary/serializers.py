import six

from rest_framework import serializers
from diary import models

from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class DiaryImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DiaryImage
        fields = ('id', 'image', 'diary')
        read_only_fields = ('id',)
        extra_kwargs = {'diary': {'required': False}}


class DiarySerializer(TaggitSerializer, serializers.ModelSerializer):
    """Serializes a diary object"""
    image_set = DiaryImageSerializer(many=True, required=False)
    tags = TagListSerializerField(required=False)

    class Meta:
        model = models.Diary
        fields = ('id', 'target', 'title', 'description', 'user', 'image_set', 'tags')
        read_only_fields = ('id',)
        extra_kwargs = {'tags': {'required': False},
                        'user': {'required': False},
                        'image_set': {'required': False}}
