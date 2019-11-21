from .models import Missing


class UserService(object):
    # 아이디 중복 체크 확인
    @staticmethod
    def check_id_overlap(name):
        overlap_name = list(Missing.objects.filter(
            name=name
        ))

        if len(overlap_name) == 0:
            return False

        return True

