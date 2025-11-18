from rest_framework import serializers
from .models import ListItem
class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = ['id', 'item_name', 'item_done']