# 캐릭터 닉네임 정할 때 비속어를 사용하지 못하게 막아주기
# 바보 멍게 해삼 운영자
# 직접 Error를 제작하여 발생시 안내 메세지까지 출력하기


class YorkError(Exception):
    def __str__(self):
        return "욕 안댐"

def check_york(nickname):
    york_list = ['바보', '해삼', '운영자']
    for york in york_list:
        if nickname.__contains__(york):
            raise YorkError
    return nickname

nickname = input('닉네임: ')
check_york(nickname)
print(nickname)

# 강사님 코드
# class NickNameError(Exception):
#     def __str__(self):
#         return "사용하실 수 없는 닉네임입니다."
#
#
# def check_nickname(nickname):
#     not_allowed_names = ['바보', '멍게', '해삼', '운영자']
#     for name in not_allowed_names:
#         if nickname.__contains__(name):
#             raise NickNameError
#
#
# nickname = input("닉네임: ")
#
# try:
#     check_nickname(nickname)
#     print(f'어서오시게, {nickname} 용사')
#
# except NickNameError as e:
#     print(e)