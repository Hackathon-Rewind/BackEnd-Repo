from rest_framework.exceptions import APIException


class BadRequset(APIException):
    status_code = 400
    default_detail = "Bad Request"


class IdIsOverlap(APIException):
    status_code = 470
    default_detail = "Id exists"
