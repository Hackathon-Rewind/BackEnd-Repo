import bcrypt

from .models import User


class OneWayHash(object):
    # 패스워드 값을 해시 값으로 만들어주는 함수
    @staticmethod
    def password_to_hash(password):
        _userPw = str(password)

        return bcrypt.hashpw(_userPw.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


class UserServie(object):
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
