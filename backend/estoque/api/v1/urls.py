from django.urls import re_path
from estoque.api.v1 import api_views

app_name = 'api_estoque'

urlpatterns = [
    # Materiais
    re_path(
        r'^(?P<version>(v1))/estoque/materiais/?$',
        api_views.MaterialViewSet.as_view({'get': 'list', 'post': 'create'}), name='material-list-create'
    ),
    re_path(
        r'^(?P<version>(v1))/estoque/materiais/(?P<pk>[0-9]+)/?$',
        api_views.MaterialViewSet.as_view({'delete':'destroy', 'get':'retrieve', 'put':'update', 'patch':'partial_update'}), name='category-update-details'
    ),
]