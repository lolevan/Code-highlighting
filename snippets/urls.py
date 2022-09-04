from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import *


urlpatterns = [
    path('snippets/', SnippetList.as_view(), name='snippets-list'),
    path('snippets/<int:pk>/', SnippetDetail.as_view(), name='snippets-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
# Ссылка на определенный формат (управление форматами)
urlpatterns = format_suffix_patterns(urlpatterns)
