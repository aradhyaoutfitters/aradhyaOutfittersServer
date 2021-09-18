from rest_framework import serializers

from .models import Contact, ProductImage


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'subject', 'message']


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product_name', 'product_image']
