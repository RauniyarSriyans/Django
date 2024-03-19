from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Item
from .serializer import ItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# # Create your views here.
# # Inefficient, too much coding, and requires manual work
# def item_list(request):
#     items = Item.objects.all()
#     item_list = []
#     for item in items:
#         item_list.append({
#             "name": item.name,
#             "price": item.price,
#             "description": item.description,
#         })
#     return JsonResponse({'menu_items': item_list})

# Serialization = Changing data type into some other data type --> Example: query object to dictionary

@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def item_list_serialized(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)
