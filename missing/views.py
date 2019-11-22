import jwt

from django.shortcuts import render, get_object_or_404
from django.core import exceptions
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from user.services import JWTService

from .serializers import (
    MissingPostSerializers
)
from .services import (
    UserService
)
from .exception import (
    NameIsOverlap,
    NoIncludeJwt,
    InappropriateJwt
)
from .models import Missing

from user.models import User

@csrf_exempt
@api_view(['POST'])
def posting_endpoint(request):
    if request.method == 'POST':
        try:
            access_token = request.headers['Authorization']
            _userId, _userInfo = JWTService.decode_jwt(access_token)
        except KeyError:
            raise NoIncludeJwt
        except jwt.exceptions.DecodeError:
            raise InappropriateJwt

        request.data["postId"] = _userId

        serializers = MissingPostSerializers(data=request.data)

        if serializers.is_valid():
            payload = serializers.initial_data

            serializers.save()

            return Response(serializers.validated_data, status=status.HTTP_200_OK)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
def post_list_endpoint(request):
    if request.method == 'GET':
        return_dict = {}
        count = 0

        for i in Missing.objects.all().order_by('-id').values():
            return_dict[count] = i
            count += 1

        print(count)

        print(return_dict)
        return Response(return_dict, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def post_list_detail_endpoint(request, pk):
    if request.method == 'GET':
        return_dict = Missing.objects.filter(pk=pk).values()
        try:
            return Response(return_dict[0], status=status.HTTP_200_OK)
        except:
            return Response("no exists primary key", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def promotion_endpoint(request, pk):
    if request.method == 'POST':
        try:
            access_token = request.headers['Authorization']
            _userId, _userInfo = JWTService.decode_jwt(access_token)
        except KeyError:
            raise NoIncludeJwt
        except jwt.exceptions.DecodeError:
            raise InappropriateJwt

        myUser = User.objects.get(
            userId=_userId
        )

        myUser.userPromotion += 1
        myUser.save()

        myProm = get_object_or_404(Missing, pk=pk)

        return Response(status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def promotion_list_endpoint(request):
    if request.method == 'GET':
        return_dict = {}
        count = 0

        for i in User.objects.all().order_by('-userPromotion').values():
            if i["userPromotion"] <= 0 or i["userInfo"] is not True:
                continue
            return_dict[count] = i
            count += 1

        return Response(return_dict, status=status.HTTP_200_OK)
