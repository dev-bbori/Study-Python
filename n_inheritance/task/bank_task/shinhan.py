from n_inheritance.task.bank_task.bank_task import Bank


class Shinhan(Bank):
    def deposit(self, money):
        self.balance += money * 0.5
