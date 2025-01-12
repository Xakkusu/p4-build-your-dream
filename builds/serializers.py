"""
Whole file was created with the help from this tutorial:
https://www.youtube.com/watch?v=Wy3yrZ-bbvE
"""

from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from .models import BuildPost

class BuildPostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = BuildPost
        fields = ("id", "build_title", "build_author", "tags", "slug")

