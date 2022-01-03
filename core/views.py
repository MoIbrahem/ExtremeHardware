from django.shortcuts import render
from store.views import ProductViewSet as BaseProductViewSet, ProductImageSerializer
from .serializers import ProductSerializer

class ProductViewSet(BaseProductViewSet):
    serializer_class = ProductSerializer


# Create your views here.
