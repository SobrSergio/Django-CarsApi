from rest_framework import generics, permissions
from .models import Car
from .serializers import CarSerializer
from rest_framework.pagination import PageNumberPagination

class CarListView(generics.ListAPIView):
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination


    def get_queryset(self):
        queryset = Car.objects.all()
        # Фильтрация по параметрам запроса
        brand = self.request.query_params.get('brand', None)
        model = self.request.query_params.get('model', None)
        year = self.request.query_params.get('year', None)
        fuel_type = self.request.query_params.get('fuel_type', None)
        transmission = self.request.query_params.get('transmission', None)
        mileage_min = self.request.query_params.get('mileage_min', None)
        mileage_max = self.request.query_params.get('mileage_max', None)
        price_min = self.request.query_params.get('price_min', None)
        price_max = self.request.query_params.get('price_max', None)
        
        if brand:
            queryset = queryset.filter(brand__iexact=brand)
        if model:
            queryset = queryset.filter(model__iexact=model)
        if year:
            queryset = queryset.filter(year=year)
        if fuel_type:
            queryset = queryset.filter(fuel_type__iexact=fuel_type)
        if transmission:
            queryset = queryset.filter(transmission__iexact=transmission)
        if mileage_min:
            queryset = queryset.filter(mileage__gte=mileage_min)
        if mileage_max:
            queryset = queryset.filter(mileage__lte=mileage_max)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)

        return queryset


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]


from django.contrib.auth.models import User
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    