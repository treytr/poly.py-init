class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
    def send_money(self,amount,recipient):
        if self.account_balance >= amount:
            self.account_balance-= amount
            print(f"{amount}KES sent to {recipient} succesfully")
        else:
            print("insufficient Amount to send")


class PersonalMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,idno):
        super().__init__(account_balance,phone_number,)
        self.idno=idno
    def buyairtime(self,amount):
        self.account_balance-=amount
        print(f"{amount} KES airtime bought succesfully")
class BusinessMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,business_name):
        super().__init__(account_balance,phone_number)
        self.business_name=business_name
    def receive_payment (self,amount):
        self.account_balance += amount
        print(f"{amount} KES received from a  customer")

personal=PersonalMpesa(2000,76574322,9564321)
personal.send_money(300,7457646464)
personal.buyairtime(200)

business=BusinessMpesa(7000,624141414,"ford motors")
business.send_money(400,"shawrry")
business.receive_payment(4000)







