from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *


# url registration
router = DefaultRouter()
router.register(r'snippets', SnippetViewSet, basename='snippets')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight',
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list',
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve',
# })
#
#
# urlpatterns = [
#     path('', api_root, name='home'),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippets-detail'),
#     path('snippets/<int:pk>/highlight', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail'),
# ]

# Ссылка на определенный формат (управление форматами)
# urlpatterns = format_suffix_patterns(urlpatterns)
