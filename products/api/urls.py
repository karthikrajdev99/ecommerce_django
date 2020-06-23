from django.urls import path, include
from rest_framework.routers import DefaultRouter


from products.api.views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [path(r'^', include(router.urls))]