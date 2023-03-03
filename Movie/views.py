from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, DirectorSerializer, ReviewSerializer, ProductCreateSerializer, ProductValidateSerializer, ReviewValidateSerializer, DirectrValidateSerializer

from .models import Product, Director, Review
from django.db.models import Avg

@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)
    if request.method == 'POST':
        serializer = ProductCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = serializer.validated_data.get('title')
        text = serializer.validated_data.get('description')
        is_active = serializer.validated_data.get('is_active')
        director = serializer.validated_data.get('director')
        tags = serializer.validated_data.get('tags')
        product = Product.objects.create(title=title, description=text, is_active=is_active,
                                         director=director, tags=tags)
        product.tags.set(tags)
        product.save()
        return Response(data={'message': 'Data received!',
                              'product': ProductSerializer(product).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'detail': 'product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(product, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        product.name = serializer.validated_data.get('title')
        product.description = serializer.validated_data.get('description')
        product.is_active = serializer.validated_data.get('is_active')
        product.director.set(serializer.validated_data.get('director'))
        product.tags.set(serializer.validated_data.get('tags'))
        product.save()
        return Response(data={'message': 'Data received!',
                              'product': ProductSerializer(product).data})



@api_view(['GET','POST'])
def directors_list_api_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        serializer = DirectorSerializer(director, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data={'message': 'vse ok',
                              'director': DirectorSerializer(director).data},
                        status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'detail' : 'director not found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(director, many = False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        director.name = request.data.get('name')
        director.save()
        return Response(data={'message' : 'Data recived!!!',
                                'director' : DirectorSerializer().data})

@api_view(['GET','POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        product_id = request.data.get('product_id')
        review = Review.objects.create(text=text, stars=stars, product_id=product_id)
        return Response(data={'message': 'vse ok',
                              'review': ReviewSerializer(review).data},
                        status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'detail' : 'review not found!!!'},
                    status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review, many = False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = DirectrValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.product_id = request.data.get('product_id')
        review.save()
        return Response(data={'message': 'Data recived!!!',
                              'review': ReviewSerializer(review).data})



@api_view(['GET'])
def average_stars(request):
    average = Review.objects.aggregate(Avg('stars'))
    return Response({'average_rating' : average})


@api_view(['GET'])
def test_api(request):
    dict_ = {
        'text' : 'eddadsdadwds',
        'int' : 100,
        'float' : 9.99,
        'bool' : True,
        'list' : [1,2,3],
    }
    return Response(data = dict_, status=status.HTTP_204_NO_CONTENT)