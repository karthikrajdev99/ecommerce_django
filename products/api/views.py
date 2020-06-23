from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import ProductSerializer, CategorySerializer
from products.models import Product, Category

from .permissions import IsGetOrIsAdmin

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = (IsGetOrIsAdmin,)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    permission_classes = (IsGetOrIsAdmin,)

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["category__name", "name", "description"]