from rest_framework import serializers
from ..models import Product


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description')