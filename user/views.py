import jwt
import base64

from django.shortcuts import render
from django.core import exceptions
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .services import (
    OneWayHash,
    UserService,
    JWTService,
    ImageHandler
)

from .exception import (
    BadRequset,
    IdIsOverlap,
    WorngIdAndPw,
)
from .serializers import (
    UserLoginSerializers,
    UserSignupSerializers
)
from missing.exception import (
    InappropriateJwt,
    NoIncludeJwt
)
from .models import User
from missing.models import Missing


@csrf_exempt
@api_view(['POST'])
def signup_endpoint(request):
    if request.method == 'POST':
        try:
            request.data['userPw'] = OneWayHash.password_to_hash(request.data['userPw'])
        except KeyError:
            return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)

        request.data["userPromotion"] = 0
        serializers = UserLoginSerializers(data=request.data)

        if serializers.is_valid():
            payload = serializers.initial_data

            if UserService.check_id_overlap(payload['userId']):
                raise IdIsOverlap

            try:
                serializers.save()
            except exceptions.ValidationError:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_200_OK)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def login_endpoint(request):
    if request.method == 'POST':
        serializers = UserSignupSerializers(data=request.data)

        if serializers.is_valid():
            payload = serializers.initial_data

            if UserService.check_id_pw_same(payload['userId'], payload['userPw']):
                access_token = JWTService.create_jwt(payload)
                return Response({'access_token': access_token}, status=status.HTTP_200_OK)

            raise WorngIdAndPw

        print(request.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
def my_inform_endpoint(request):
    if request.method == 'GET':
        try:
            access_token = request.headers['Authorization']
            _userId, _userInfo = JWTService.decode_jwt(access_token)
        except KeyError:
            raise NoIncludeJwt
        except jwt.exceptions.DecodeError:
            raise InappropriateJwt

        return_dict = {}

        myUser = User.objects.get(
            userId=_userId
        )

        return_dict['name'] = myUser.userId
        return_dict['info'] = myUser.userInfo
        return_dict['phone'] = myUser.userPhone

        myMissing = Missing.objects.order_by('-id').filter(
            postId=myUser.userId
        )

        specific_dict = {}
        count = 0

        for i in myMissing.values():
            specific_dict[count] = i
            count += 1

        return_dict['missing_list'] = specific_dict

        return Response(return_dict, status=status.HTTP_200_OK)
