import jwt

from django.shortcuts import render
from django.core import exceptions
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


@csrf_exempt
@api_view(['POST'])
def posting_endpoint(request):
    if request.method == 'POST':
        try:
            access_token = request.headers['Authorization']
            _userId = JWTService.decode_jwt(access_token)
        except KeyError:
            raise NoIncludeJwt
        except jwt.exceptions.DecodeError:
            raise InappropriateJwt

        request.data["postId"] = _userId

        serializers = MissingPostSerializers(data=request.data)

        if serializers.is_valid():
            payload = serializers.initial_data

            if UserService.check_id_overlap(payload['name']):
                raise NameIsOverlap

            serializers.save()

            return Response(serializers.validated_data, status=status.HTTP_200_OK)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
