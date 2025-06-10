# class Bankomat:
    
#     users = {
#     "1001": {"name": "Ali", "pin": "1234", "balance": 150000},
#     "1002": {"name": "Vali", "pin": "4321", "balance": 250000},
#     "1003": {"name": "Zarina", "pin": "9876", "balance": 500000},
#     "1004": {"name": "Jasur", "pin": "4567", "balance": 75000},
#     "1005": {"name": "Dilorom", "pin": "2345", "balance": 120000},
#     "1006": {"name": "Rustam", "pin": "3456", "balance": 300000},
#     "1007": {"name": "Nigora", "pin": "6543", "balance": 200000},
#     "1008": {"name": "Oybek", "pin": "7654", "balance": 175000},
#     "1009": {"name": "Malika", "pin": "8765", "balance": 220000},
#     "1010": {"name": "Jahon", "pin": "5678", "balance": 90000},
#     "1011": {"name": "Anvar", "pin": "3452", "balance": 130000},
#     "1012": {"name": "Shahnoza", "pin": "4325", "balance": 110000},
#     "1013": {"name": "Bekzod", "pin": "6547", "balance": 280000},
#     "1014": {"name": "Gulbahor", "pin": "9871", "balance": 260000}
#     }

#     def __init__(self, account_number):
#         account_number = str(account_number)
#         if account_number not in Bankomat.users:
#             raise ValueError("Hisob raqami topilmadi!")

#         user = Bankomat.users[account_number]
#         self.name = user['name']
#         self.pin = user['pin']
#         self.balance = user['balance']
#         self._account_number = account_number

#         print(f"Xush kelibsiz {self.name}!")
    
#     def show_balance(self):
#         return self.balance
    
#     def deposit(self, amount):
#         self.balance += amount
#         Bankomat.users[self._account_number]['balance'] = self.balance
#         return f"Yangi balans: ${self.balance}"

#     def withdraw(self, amount):
#         if self.balance < amount:
#             raise ValueError('Mablag\' yetarli emas!')
#         else:
#             self.balance -= amount
#             Bankomat.users[self._account_number]['balance'] = self.balance
#             return f"Hisobingizda ${self.balance} qoldi"
    
# def main():
#     while True:
#         print('1 - balans \n2 - deposit \n3 - naqd pul olish ')
#         choice = input('nbuyruqni tanlang \n>>> ')
        
#         if choice == '1':
#             print(f"balansingizda mazvjud {balance}")
#         elif choice == '2':
#             print(f"{deposit} kiritildi")
#         elif choice == '3':
#             print(f"{withdraw} yechib olindi")
#         else:
#             print('notog\'ri buyruq!')
#             break

# main()






class Bankomat:
    
    users = {
        "1001": {"name": "Ali", "pin": "1234", "balance": 150000},
        "1002": {"name": "Vali", "pin": "4321", "balance": 250000},
        "1003": {"name": "Zarina", "pin": "9876", "balance": 500000},
        "1004": {"name": "Jasur", "pin": "4567", "balance": 75000},
        "1005": {"name": "Dilorom", "pin": "2345", "balance": 120000},
        "1006": {"name": "Rustam", "pin": "3456", "balance": 300000},
        "1007": {"name": "Nigora", "pin": "6543", "balance": 200000},
        "1008": {"name": "Oybek", "pin": "7654", "balance": 175000},
        "1009": {"name": "Malika", "pin": "8765", "balance": 220000},
        "1010": {"name": "Jahon", "pin": "5678", "balance": 90000},
        "1011": {"name": "Anvar", "pin": "3452", "balance": 130000},
        "1012": {"name": "Shahnoza", "pin": "4325", "balance": 110000},
        "1013": {"name": "Bekzod", "pin": "6547", "balance": 280000},
        "1014": {"name": "Gulbahor", "pin": "9871", "balance": 260000}
    }

    def __init__(self, account_number):
        account_number = str(account_number)
        if account_number not in Bankomat.users:
            raise ValueError("hisob raqami topilmadi!")

        user = Bankomat.users[account_number]
        self.name = user['name']
        self.pin = user['pin']
        self.balance = user['balance']
        self._account_number = account_number

        print(f"xush kelibsiz {self.name}!")
    
    def show_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        Bankomat.users[self._account_number]['balance'] = self.balance
        print(f"hisboingizga ${amount} qo'shildi")
        return f"yangi balans: ${self.balance}"

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError('mablag\' yetarli emas!')
        else:
            self.balance -= amount
            Bankomat.users[self._account_number]['balance'] = self.balance
            print(f"hisobingizdan {amount} yechib olindi")
            return f"hisobingizda ${self.balance} qoldi"

def main():
    input_pin = input("parolni kiriting \n>>> ")
    
    account_number = None
    for acc_num, user_info in Bankomat.users.items():
        if user_info['pin'] == input_pin:
            account_number = acc_num
            break
    
    if account_number is None:
        print("parol noto'g'ri yoki topilmadi!")
        return
    
    atm = Bankomat(account_number)

    while True:
        print('1 - balans \n2 - deposit \n3 - naqd pul olish \n0 - chiqish')
        choice = input('buyruqni tanlang \n>>> ')
        
        if choice == '1':
            print(f"balansingizda mavjud: ${atm.show_balance()}")
        
        elif choice == '2':
            amount = int(input("pul miqdori \n>>> "))
            print(atm.deposit(amount))
        
        elif choice == '3':
            amount = int(input("pul miqdori \n>>> "))
            try:
                print(atm.withdraw(amount))
            except ValueError as e:
                print(e)
        
        elif choice == '0':
            print("OPERATSIYA YAKUNLANDI. PULINGIZ DOIM KO'PAYIB BORSIN!")
            break
        
        else:
            print('noto\'g\'ri buyruq!')

main()