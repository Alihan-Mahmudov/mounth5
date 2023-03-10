from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, \
    DirectorValidateSerializer, MovieValidateSerializer, ReviewValidateSerializer
from .models import Director, Movie, Review
from django.db.models import Avg
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination


class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        if request.method == 'GET':
            directors = Director.objects.all()
            serializer = DirectorSerializer(directors, many=True)
            return Response(data=serializer.data)
        elif request.method == 'POST':
            serializer = DirectorValidateSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(data=serializer.errors,
                                status=status.HTTP_406_NOT_ACCEPTABLE)
            name = serializer.validated_data.get('name')
            director = Director.objects.create(name=name)
            director.save()
            return Response(data={'message': 'Data received!',
                                  'director': DirectorSerializer(director).data},
                            status=status.HTTP_201_CREATED)


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail_api_view(request, id):
#     try:
#         directors = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(data={'detail': 'director not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = DirectorSerializer(directors, many=False)
#         return  Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         directors.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = DirectorValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         directors.name = request.data.get('name')
#         directors.save()
#         return Response(data={'message': 'Data received!',
#                               'director': DirectorSerializer(directors).data})


class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        if request.method == 'GET':
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(data=serializer.data)
        elif request.method == 'POST':
            serializer = MovieValidateSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(data=serializer.errors,
                                status=status.HTTP_406_NOT_ACCEPTABLE)
            title = serializer.validated_data.get('title')
            description = serializer.validated_data.get('description')
            duration = serializer.validated_data.get('duration')
            director_id = serializer.validated_data.get('director_id')
            movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
            movie.save()
            return Response(data={'message': 'Data received!',
                                  'Movie': MovieSerializer(movie).data},
                            status=status.HTTP_201_CREATED)


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


# def movie_detail_api_view(request, id):
#     try:
#         movies = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(data={'detail': 'Movie not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = MovieSerializer(movies, many=False)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = MovieValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movies.title = request.data.get('title')
#         movies.description = request.data.get('description')
#         movies.duration = request.data.get('duration')
#         movies.director_id = request.data.get('director_id')
#         movies.save()
#         return Response(data={'message': 'Data received!',
#                               'Movie': MovieSerializer(movies).data})


class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        if request.method == 'GET':
            reviews = Review.objects.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(data=serializer.data)
        elif request.method == 'POST':
            serializer = ReviewValidateSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(data=serializer.errors,
                                status=status.HTTP_406_NOT_ACCEPTABLE)
            text = serializer.validated_data.get('text')
            movie_id = serializer.validated_data.get('movie_id')
            stars = serializer.validated_data.get('stars')
            reviews = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
            reviews.save()
            return Response(data={'message': 'Data received!',
                                  'review': ReviewSerializer(reviews).data},
                            status=status.HTTP_201_CREATED)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'


# def review_detail_api_view(request, id):
#     try:
#         reviews = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'detail': 'review not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = ReviewSerializer(reviews, many=False)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         reviews.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         reviews.text = request.data.get('text')
#         reviews.movie_id = request.data.get('movie_id')
#         reviews.stars = request.data.get('stars')
#         reviews.save()
#         return Response(data={'message': 'Data received!',
#                               'review': ReviewSerializer(reviews).data})


class GetAverage(APIView):
    @staticmethod
    def get_average(request):
        average = Review.objects.aggregate(Avg('stars'))
        return Response({'average_rating': average['stars__avg']})
