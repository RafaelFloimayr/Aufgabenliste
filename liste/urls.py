from django.urls import path
from .views import show_list, delete_item, toggle_item
urlpatterns = [
    path('', show_list, name='show_list'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
    path('toggle/<int:item_id>/', toggle_item, name='toggle_item')
]
