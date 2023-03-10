from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movie_count'.split()

    def get_movie_count(self, director):
        return director.movie_set.count()


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, min_length=1)

    def validate_director(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('This director does not exists!')
        return director_id


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=50)
    description = serializers.CharField(max_length=200)
    duration = serializers.FloatField()
    director = serializers.IntegerField()

    def validate_movie(self, movie):
        try:
            Movie.objects.get(id=movie)
        except Movie.DoesNotExist:
            raise ValidationError('This Movie does not exists!')
        return movie

    def validate_director(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('This director does not exists!')
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.IntegerField()
    stars = serializers.IntegerField()

    def validate_review(self, review_id):
        try:
            Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            raise ValidationError('This review does not exists!')
        return review_id

    def validate_movie(self, movie):
        try:
            Movie.objects.get(id=movie)
        except Movie.DoesNotExist:
            raise ValidationError('This Movie does not exists!')
        return movie
