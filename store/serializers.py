import decimal
from rest_framework import serializers

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 255)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source = 'unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calc_tax')
    collection = CollectionSerializer()

    def calc_tax(self, product):
        return product.unit_price * decimal.Decimal(1.1)