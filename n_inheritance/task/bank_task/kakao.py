from n_inheritance.task.bank_task.bank_task import Bank


class Kakao(Bank):
    def check_balance(self):
        self.money /= 2
        return