from rest_framework import serializers

from MyApp.models import Category, Product, Sale, SaleDetail


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sale()
        fields="__all__"