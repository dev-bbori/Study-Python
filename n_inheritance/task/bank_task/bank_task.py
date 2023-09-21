# 은행
#    예금주
#    계좌번호(중복 없음)
#    핸드폰번호(중복 없음)
#    비밀번호
#    통장잔고
#
# 신한
#    입금 시 수수료 50%
# 국민
#    출금 시 수수료 50%
# 카카오
#    잔액조회 재산 반토막


class Bank:

    bank_list = ["shinhan", "kookmin", "Kakao"]
    banks = [[] for bank in bank_list]

    def __init__(self, name: str, account: str, phone_number: str, password: str, balance: int):
        self.name = name
        self.account = account
        self.phone_number = phone_number
        self.password = password
        self.balance = balance


    @classmethod
    def join(cls, name: str, account: str, phone_number: str, password: str, balance: int):
        cls.user_list.append(cls.__dict__)
        return cls(name, account, phone_number, password, balance)

    @staticmethod
    def check_account_number(account_number: str) -> bool:
        for bank in Bank.bank_list:
            for users in bank:
                if users['account']

    @staticmethod
    def check_phone(phone: str) -> bool:
        pass


    def deposit(self, money):
        self.balance += money


    def withdraw(self, money):
        self.balance -= money


    def check_balance(self, user):
        return self.balance