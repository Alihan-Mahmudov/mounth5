from rest_framework import serializers
from .models import Product, Review, Director, Tag
from rest_framework.exceptions import ValidationError

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
    tags = TagSerializer(many=True)
    director = DirectorSerializer

    class Meta:
        model = Product
        fields = '__all__'

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    tags = serializers.ListField(child=serializers.IntegerField())
    description = serializers.CharField(max_length=500)
    duration = serializers.IntegerField()
    director = serializers.IntegerField()
    is_active = serializers.BooleanField(default=True)

    def validate_director_id(self, director):  # 100
        try:
            Director.objects.get(id=director)
        except Director.DoesNotExist:
            raise ValidationError('This category does not exists!')
        return director

    def validate_tags(self, tags):  # [1,2,100]
        tags_db = Tag.objects.filter(id__in=tags)
        if len(tags_db) != len(tags):
            raise ValidationError('Tag does not exists')
        return tags

class ProductCreateSerializer(ProductValidateSerializer):
    pass


class ProductUpdateSerializer(ProductValidateSerializer):
    pass


class DirectrValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)



class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, max_length=500)
    stars = serializers.IntegerField(required=True)

    def review_validate_stars(self, stars):
        if stars > 5:
            raise ValidationError('Too many stars max value=5')
        elif stars < 1:
            raise ValidationError('Too few stars min value=5')

