# FlowerShop

# 손님마다 할인율이 다르다
# 판매시 손님의 할인율을 적용해서 판매한다.

class FlowerShop:
    #  상품명, 가격, 재고
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    def sells(self, customer):
        discount_money = self.price - (self.price * customer.discount * 0.01)
        customer.money -= int(discount_money)
        self.stock -= 1


class Customer:
    # 회원명, 연락처, 할인률
    def __init__(self, name, phone_number, discount, money):
        self.name = name
        self.phone_number = phone_number
        self.discount = discount
        self.money = money


customer = Customer('문소영', "01012341234", 50, 100000)
flowerShop = FlowerShop('데이지', 30000, 100)

flowerShop.sells(customer)
print(customer.money)
print(flowerShop.stock)
