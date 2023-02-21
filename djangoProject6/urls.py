"""djangoProject6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Movie.views import product_list_api_view, product_detail_api_view, directors_list_api_view, director_detail_api_view, review_detail_api_view, review_list_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', product_list_api_view),
    path('api/v1/product/<int:id>/', product_detail_api_view),
    path('api/v1/directors/', directors_list_api_view),
    path('api/v1/directors/<int:id>/', director_detail_api_view),
    path('api/v1/reviews/', review_list_api_view),
    path('api/v1/reviews/<int:id>/', review_detail_api_view),

]