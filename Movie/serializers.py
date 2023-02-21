from rest_framework import serializers
from .models import Product, Review, Director, Tag

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    review = ReviewSerializer(many=True, allow_null=True)
    director = DirectorSerializer

    class Meta:
        model = Product
        fields = '__all__'

