from django.shortcuts import render

import jwt

from django.shortcuts import render
from django.core import exceptions
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from user.services import (
    JWTService
)

from missing.exception import (
    NoIncludeJwt,
    InappropriateJwt
)

from .models import Report

from .serializers import ReportPostSerializers


@csrf_exempt
@api_view(['POST'])
def report_endpoint(request):
    if request.method == 'POST':
        try:
            access_token = request.headers['Authorization']
            _userId, _userInfo = JWTService.decode_jwt(access_token)
        except KeyError:
            raise NoIncludeJwt
        except jwt.exceptions.DecodeError:
            raise InappropriateJwt

        request.data["reportId"] = _userId
        serializers = ReportPostSerializers(data=request.data)

        if serializers.is_valid():
            payload = serializers.initial_data

            serializers.save()
            return Response(payload, status=status.HTTP_200_OK)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
def report_list_endpoint(request):
    if request.method == 'GET':
        return_dict = {}
        count = 0

        for i in Report.objects.all().order_by('-id').values():
            return_dict[count] = i
            count += 1

        return Response(return_dict, status=status.HTTP_200_OK)
