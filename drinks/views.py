from django.shortcuts import render, get_object_or_404
from .models import Drink
from .serializers import DrinkSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your views here.

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def drink_list(request):
    if request.method == 'GET':
        # get all drinks
        drinks = Drink.objects.all()

        # serialize the drinks
        serializer = DrinkSerializer(drinks, many=True)

        # return the serialized
        return JsonResponse(serializer.data, safe=False, status=200)

    if request.method == 'POST':
        # create a new drink object
        serializer = DrinkSerializer(data=request.data)
        # if data is valid, save it to the database
        if serializer.is_valid():
            serializer.save()

            # return the serialized data as json
            return JsonResponse(serializer.data, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def drink_detail(request, id):
    # get a specific drink
    drink = get_object_or_404(Drink, pk=id)

    if request.method == 'GET':

        # serialize the drink
        serializer = DrinkSerializer(drink)

        # return the serialized drink
        return JsonResponse(serializer.data, status=200)

    elif request.method == 'PUT':
        # update the drink object
        serializer = DrinkSerializer(drink, data=request.data)

        # if the data is valid, save it to the database
        if serializer.is_valid():
            serializer.save()

            # return the serialized data as json
            return JsonResponse(serializer.data, status=200)
        # invalid data
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        # delete the drink
        drink.delete()

        # return a success message
        return JsonResponse({'message': 'Drink was deleted successfully!'}, status=204)


@api_view(['POST'])
def signup(request):
    # create a new user object from the request data
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        #  get the user object
        user = User.objects.get(username=request.data['username'])

        # hash the password
        user.set_password(request.data['password'])

        # update the user object with the hashed password
        user.save()

        # create a token for the user
        token = Token.objects.create(user=user)

        # return the token and user data
        return Response({'token': token.key, 'user': serializer.data}, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def signin(request):
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({'message': 'Invalid credentials'}, status=400)
    token, _ = Token.objects.get_or_create(user=user)

    serializer = UserSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data}, status=200)


def signout(request):
    pass


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def verify_token(request):
    return Response("passed for {}".format(request.user.email))