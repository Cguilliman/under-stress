from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("title", )
