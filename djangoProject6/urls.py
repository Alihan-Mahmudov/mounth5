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
from Movie import views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.DirectorListAPIView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('api/v1/movies/', views.MovieListAPIView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('api/v1/reviews/', views.ReviewListAPIView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),
    path('api/v1/movies/reviews/', views.GetAverage.as_view()),
    path('api/v1/users/registration/', user_views.RegistrationAPIView.as_view()),
    path('api/v1/users/authorization/', user_views.AuthorizationAPIView.as_view()),
    path('api/v1/users/confirm/', user_views.ConfirmAPIView.as_view())
]