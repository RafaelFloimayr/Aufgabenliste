from django.db import transaction
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from .models import ListItem
from .forms import ListItemForm
from .serializers import ListItemSerializer


def show_list(request):
    if request.method == 'POST':
        form = ListItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_list')
    else:
        form = ListItemForm()

    items = ListItem.objects.all()
    return render(request, 'liste.html', {'items': items, 'form': form})

def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(ListItem, id=item_id)
        item.delete()
        return redirect('show_list')
    return HttpResponseNotAllowed(['POST'])

def toggle_item(request, item_id):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        with transaction.atomic():
            item = ListItem.objects.select_for_update().get(id=item_id)
            item.item_done = data.get("item_done", False)
            item.save()
        return HttpResponse(status=204)
    return HttpResponseNotAllowed(['POST'])

class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer