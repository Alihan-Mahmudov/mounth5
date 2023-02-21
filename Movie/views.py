from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, DirectorSerializer, ReviewSerializer
from .models import Product, Director, Review

@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'detail' : 'product not found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product, many = False)
    return Response(data=serializer.data)

@api_view(['GET'])
def directors_list_api_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'detail' : 'director not found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(director, many = False)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'detail' : 'review not found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review, many = False)
    return Response(data=serializer.data)


@api_view(['GET', 'POST'])
def test_api(request):
    dict_ = {
        'text' : 'ali',
        'int' : 100,
        'float' : 9.99,
        'bool' : True,
        'list' : [1,2,3],
    }
    return Response(data = dict_, status=status.HTTP_204_NO_CONTENT)