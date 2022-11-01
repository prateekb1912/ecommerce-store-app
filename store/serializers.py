from decimal import Decimal
from rest_framework import serializers
from store.models import Collection, Product

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory',  'price', 'price_with_tax', 'collection']

    price = serializers.DecimalField(max_digits=6, decimal_places=2, source = 'unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calc_tax')
    collection = CollectionSerializer()

    def calc_tax(self, product):
        return product.unit_price * Decimal(1.1)