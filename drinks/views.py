from django.shortcuts import render
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
        return JsonResponse(serializer.data, safe=False)
   
   