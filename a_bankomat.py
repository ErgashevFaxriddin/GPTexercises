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
            raise ValueError("Hisob raqami topilmadi!")

        user = Bankomat.users[account_number]
        self.name = user['name']
        self.pin = user['pin']
        self.balance = user['balance']
        self._account_number = account_number

        print(f"Xush kelibsiz {self.name}!")
    
    def authentification(self, input_pin):
        return self.pin == input_pin

    def balance(self):
        return f"balans: ${self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        Bankomat.users[self._account_number]['balance'] = self.balance
        return f"balansingizga ${self.amount} qo'shildi"
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            Bankomat.users[self._account_number]['balance'] = self.balance
            return f"${amount} yechildi"
        else:
            return 'No enough money!'

def main():
    pin = input('PIN kodni kiriting\n>>> ')
    
    for acc_number, info in Bankomat.users.items():
        if info['pin'] == pin:
            atm = Bankomat(acc_number)
            break
    else:
        print('PIN noto\'g\'ri yoki topilmadi!')
        return
    while True:
        print('1 - balans \n2 - pul qo\'shish \n3 - pul yechish\n')
        choice = input('buyruq raqamini kiriting\n>>> ')
        
        if choice == '1':
            print(f"balansingizda mavjud ${atm.balance}")
        elif choice == '2':
            amount = int(input("Qo'shmoqchi bo'lgan summani kiriting\n>>> "))
            print(atm.deposit(amount))
            amount = int(input("Yechmoqchi bo'lgan summani kiriting\n>>> "))
            print(atm.withdraw(amount))
            print(at.withdraw(amount))
        elif choice == '0':
            print('Dastur to\'xtatildi, xayr!')
            break
        else:
            print('Noto\'g\'ri buyruq\nIltimos tekshirib qaytadan kiriting!')
            
main()