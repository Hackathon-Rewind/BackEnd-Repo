import bcrypt
import jwt
import base64
from datetime import datetime, timedelta

from .models import User
from django.core import exceptions
from mysite.settings import JWT_SECRET_KEY


class OneWayHash(object):
    # 패스워드 값을 해시 값으로 만들어주는 함수
    @staticmethod
    def password_to_hash(password):
        _userPw = str(password)

        return bcrypt.hashpw(_userPw.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


class UserService(object):
    # 아이디 중복 체크 확인
    @staticmethod
    def check_id_overlap(id):
        _userId = str(id)
        overlap_user = list(User.objects.filter(
            userId=_userId
        ))

        if len(overlap_user) == 0:
            return False

        return True

    # 아이디 비밀번호 일치 확인
    @staticmethod
    def check_id_pw_same(user_id, hashed_password):
        try:
            filter_user = User.objects.get(
                userId = user_id
            )

            return bcrypt.checkpw(str(hashed_password).encode('utf-8'), filter_user.userPw.encode('utf-8'))

        except exceptions.ObjectDoesNotExist:
            return False


class JWTService(object):

    # jwt encoding
    @staticmethod
    def create_jwt(payload):
        data = {
            'id': payload['userId'],
            'exp': datetime.utcnow() + timedelta(seconds=60*60*24)
        }
        encoded_jwt = jwt.encode(data, JWT_SECRET_KEY, algorithm='HS256')

        return encoded_jwt

    # jwt decoding
    @staticmethod
    def decode_jwt(token):
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
        filter_user = User.objects.get(
            userId=payload['id']
        )
        return filter_user.userId, filter_user.userInfo


class ImageHandler(object):

    # 사진 올리기
    @staticmethod
    def upload_photo(user_id, my_base64):
        with open(f"Data/User/{user_id}.png", "wb") as f:
            f.write(base64.decodebytes(my_base64))
