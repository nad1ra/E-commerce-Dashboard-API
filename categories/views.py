from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from .pagination import CategoryListPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryListPagination
