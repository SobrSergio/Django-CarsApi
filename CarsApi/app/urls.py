from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CarListView, CarDetailView, RegisterView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('cars/', CarListView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('register/', RegisterView.as_view(), name='register'),
]
