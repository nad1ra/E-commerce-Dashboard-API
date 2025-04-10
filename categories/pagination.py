from rest_framework.pagination import PageNumberPagination


class CategoryListPagination(PageNumberPagination):
    page_size = 8