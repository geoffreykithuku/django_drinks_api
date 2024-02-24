from django.shortcuts import render, get_object_or_404
from .models import Drink
from .serializers import DrinkSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def drink_list(request):
   if request.method == 'GET':
       # get all drinks
        drinks = Drink.objects.all()

        #serialize the drinks
        serializer = DrinkSerializer(drinks, many=True)

        #return the serialized 
        return JsonResponse(serializer.data, safe=False, status=200)
   
   if request.method == 'POST':
         # create a new drink object
       serializer = DrinkSerializer(data=request.data)
       # if data is valid, save it to the database
       if serializer.is_valid():
           serializer.save()

              #return the serialized data as json
           return JsonResponse(serializer.data, status=201)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):

    # get a specific drink
    if request.method == 'GET':
        drink = get_object_or_404(Drink, pk=id)

        # serialize the drink
        serializer = DrinkSerializer(drink)

        # return the serialized drink
        return JsonResponse(serializer.data, status=200)
   
        