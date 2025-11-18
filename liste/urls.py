from django.urls import path
from .views import show_list, delete_item, toggle_item, ListItemViewSet
from rest_framework import routers

urlpatterns = [
    path('', show_list, name='show_list'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
    path('toggle/<int:item_id>/', toggle_item, name='toggle_item'),
]

# Django REST framework
router = routers.DefaultRouter()
router.register(r'tasks', ListItemViewSet)
urlpatterns += router.urls
