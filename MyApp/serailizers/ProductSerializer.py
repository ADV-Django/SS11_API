from rest_framework import serializers

from MyApp.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    # tracks = serializers.StringRelatedField(many=True)
    class Meta:
        model=Product
        fields="__all__"