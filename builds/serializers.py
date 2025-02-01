from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from .models import BuildPost


class BuildPostSerializer(TaggitSerializer, serializers.ModelSerializer):
    """
    Convert Data to be used & transmitted for tags in the project
    Whole file was created with the help from this tutorial:
    https://www.youtube.com/watch?v=Wy3yrZ-bbvE
    """
    tags = TagListSerializerField()

    class Meta:
        """
        Specify the model used and which fields will be
        used
        """
        model = BuildPost
        fields = ("id", "build_title", "build_author", "tags", "slug")
