from rest_framework import viewsets

from .serializers import ProductSerializer, CategorySerializer, UserSerializer
from products.models import Product, Category
from users.models import Users
from .permissons import IsAdminOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAdminOrReadOnly, )

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAdminOrReadOnly, )


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    permission_classes = (IsAdminOrReadOnly, )