"""
Serializers for recipe APIs.
"""

from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.Serializer):
    """ Serializer for recipe. """

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """ Serializer for recipe detail view. (extension of recipe serializer) """

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
