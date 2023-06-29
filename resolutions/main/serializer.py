from rest_framework import serializers
from .models import *

class ResolutionSerializer(serializers.ModelSerializer):
    format = serializers.CharField(source='format.name')
    category = serializers.CharField(source='category.name')
    pk = serializers.IntegerField(source='id', required = False)


    def create(self, validated_data):
        format_name = validated_data.pop('format', None).get('name')
        category_name = validated_data.pop('category', None).get('name')

        format_instance = None
        if format_name:
            try:
                format_instance = Format.objects.get(name=format_name)
            except Format.DoesNotExist:
                raise serializers.ValidationError(f"Format with name '{format_name}' does not exist.")

        category_instance = None
        if category_name:
            try:
                category_instance = Category.objects.get(name=category_name)
            except Category.DoesNotExist:
                raise serializers.ValidationError(f"Category with name '{category_name}' does not exist.")

        resolution = Resolution.objects.create(format=format_instance, category=category_instance, **validated_data)
        return resolution


    def delete(self, instance):
        instance.delete()


    class Meta:
        model = Resolution
        fields = ('pk', 'title', 'published', 'rating', 'format', 'category')
