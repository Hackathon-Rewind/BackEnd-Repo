from rest_framework.exceptions import APIException


class BadRequset(APIException):
    status_code = 400
    default_detail = "Bad Request"


class IdIsOverlap(APIException):
    status_code = 470
    default_detail = "Id exists"


class WorngIdAndPw(APIException):
    status_code = 471
    default_detail = "wrong password"


# decode 실패 jwt
class InappropriateJwt(APIException):
    status_code = 422
    default_detail = "inappropriate jwt"