from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response

from orders.models import Order, Cart
from .serializers import OrderSerializer, CartSerializer
from .permissions import IsPostOrIsAdmin

class OrdersViewSet(ModelViewSet):
    """
    API view for listing (admin) or creating (authenticated user) orders.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CartViewSet(ModelViewSet):
    """
    API viewset for cart 
    """

    queryset = Cart.objects.all()
    serializer_class = CartSerializer