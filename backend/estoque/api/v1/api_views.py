from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from estoque.models import *
from estoque.api.v1 import serializers

class BasePagination(PageNumberPagination):
    page_size = 10

class MaterialViewSet(ModelViewSet,BasePagination):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.MaterialSerializer
    queryset = Material.objects.all().order_by('id')