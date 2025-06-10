# Ergashev Faxriddin
# bankomat (ATM) dasturi
# ✅ 1. PIN o‘zgartirish funksiyasi
# ✅ 3. Pul o‘tkazish funksiyasi (boshqa foydalanuvchiga)
# ✅ 4. Avtomatik chiqish (autologout)
# ✅ 5. Foydalanuvchi tilini tanlash (multi-language)
# ✅ 6. Valyuta konvertatsiyasi



# from rich.console import Console
# from rich.prompt import Prompt, IntPrompt
# from rich.panel import Panel
# from rich.text import Text
# from rich.table import Table

# console = Console()

# class Bankomat:
    
#     users = {
#         "1001": {"name": "Ali", "pin": "1234", "balance": 150000},
#         "1002": {"name": "Vali", "pin": "4321", "balance": 250000},
#         "1003": {"name": "Zarina", "pin": "9876", "balance": 500000},
#         "1004": {"name": "Jasur", "pin": "4567", "balance": 75000},
#         "1005": {"name": "Dilorom", "pin": "2345", "balance": 120000},
#         "1006": {"name": "Rustam", "pin": "3456", "balance": 300000},
#         "1007": {"name": "Nigora", "pin": "6543", "balance": 200000},
#         "1008": {"name": "Oybek", "pin": "7654", "balance": 175000},
#         "1009": {"name": "Malika", "pin": "8765", "balance": 220000},
#         "1010": {"name": "Jahon", "pin": "5678", "balance": 90000},
#         "1011": {"name": "Anvar", "pin": "3452", "balance": 130000},
#         "1012": {"name": "Shahnoza", "pin": "4325", "balance": 110000},
#         "1013": {"name": "Bekzod", "pin": "6547", "balance": 280000},
#         "1014": {"name": "Gulbahor", "pin": "9871", "balance": 260000}
#     }

#     def __init__(self, account_number):
#         account_number = str(account_number)
#         if account_number not in Bankomat.users:
#             raise ValueError("hisob raqami topilmadi!")

#         user = Bankomat.users[account_number]
#         self.name = user['name']
#         self.pin = user['pin']
#         self.balance = user['balance']
#         self._account_number = account_number

#         console.print(f"[bold green]xush kelibsiz {self.name}![/bold green]")
    
#     def show_balance(self):
#         return self.balance
    
#     def deposit(self, amount):
#         self.balance += amount
#         Bankomat.users[self._account_number]['balance'] = self.balance
#         console.print(f"[green]Hisobingizga ${amount} qo'shildi[/green]")
#         return f"Yangi balans: ${self.balance}"

#     def withdraw(self, amount):
#         if self.balance < amount:
#             raise ValueError("mablag' yetarli emas!")
#         else:
#             self.balance -= amount
#             Bankomat.users[self._account_number]['balance'] = self.balance
#             console.print(f"[red]hisobingizdan ${amount} yechib olindi[/red]")
#             return f"hisobingizda ${self.balance} qoldi"

# def main():
#     console.print(Panel("[bold blue]bankomat dasturiga xush kelibsiz![/bold blue]"))

#     input_pin = Prompt.ask("parolni kiriting", password=True)
    
#     account_number = None
#     for acc_num, user_info in Bankomat.users.items():
#         if user_info['pin'] == input_pin:
#             account_number = acc_num
#             break
    
#     if account_number is None:
#         console.print("[bold red]parol noto'g'ri yoki topilmadi![/bold red]")
#         return
    
#     atm = Bankomat(account_number)

#     while True:
#         console.print(Panel(
#             "[1] balansni ko'rish\n[2] pul qo'shish\n[3] naqd pul olish\n[0] chiqish",
#             title="Menyu", subtitle="Iltimos tanlang", style="cyan"
#         ))
#         choice = Prompt.ask("buyruqni tanlang")

#         if choice == '1':
#             bal = atm.show_balance()
#             console.print(Panel(f"[bold yellow]balansingizda mavjud: ${bal}[/bold yellow]", style="green"))
        
#         elif choice == '2':
#             amount = IntPrompt.ask("pul miqdori")
#             print(atm.deposit(amount))
        
#         elif choice == '3':
#             amount = IntPrompt.ask("pul miqdori")
#             try:
#                 print(atm.withdraw(amount))
#             except ValueError as e:
#                 console.print(f"[bold red]{e}[/bold red]")
        
#         elif choice == '0':
#             console.print("[bold magenta]OPERATSIYA YAKUNLANDI. PULINGIZ DOIM KO'PAYIB BORSIN![/bold magenta]")
#             break
        
#         else:
#             console.print("[bold red]noto'g'ri buyruq![/bold red]")

# main()



# Ergashev Faxriddin
# Bankomat (ATM) dasturi - to'liq funksiyalar bilan

from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from rich.table import Table

console = Console()

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
        self.history = []

        console.print(f"[bold green]Xush kelibsiz {self.name}![/bold green]")

    def show_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        Bankomat.users[self._account_number]['balance'] = self.balance
        self.history.append(f"+${amount} qo'shildi")
        console.print(f"[green]Hisobingizga ${amount} qo'shildi[/green]")
        return f"Yangi balans: ${self.balance}"

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Mablag' yetarli emas!")
        else:
            self.balance -= amount
            Bankomat.users[self._account_number]['balance'] = self.balance
            self.history.append(f"-${amount} yechildi")
            console.print(f"[red]Hisobingizdan ${amount} yechildi[/red]")
            return f"Qolgan balans: ${self.balance}"

    def show_history(self):
        if not self.history:
            console.print("[yellow]Tranzaksiyalar mavjud emas.[/yellow]")
        else:
            table = Table(title="Tranzaksiyalar Tarixi")
            table.add_column("#", justify="center")
            table.add_column("Harakat", justify="left")
            for i, h in enumerate(self.history, 1):
                table.add_row(str(i), h)
            console.print(table)

    def change_pin(self, new_pin):
        self.pin = new_pin
        Bankomat.users[self._account_number]['pin'] = new_pin
        console.print("[green]PIN kod muvaffaqiyatli o'zgartirildi![/green]")

    def transfer(self, recipient_acc, amount):
        if recipient_acc not in Bankomat.users:
            raise ValueError("Qabul qiluvchi topilmadi!")
        if self.balance < amount:
            raise ValueError("Balans yetarli emas!")
        self.withdraw(amount)
        Bankomat.users[recipient_acc]['balance'] += amount
        self.history.append(f"-${amount} --> {recipient_acc}")
        console.print(f"[blue]{amount}$ {recipient_acc} raqamiga yuborildi.[/blue]")

def main():
    console.print(Panel("[bold cyan]BANKOMAT DASTURIGA XUSH KELIBSIZ![/bold cyan]"))

    attempts = 3
    account_number = None
    while attempts > 0:
        input_pin = Prompt.ask("Parolni kiriting", password=True)
        for acc_num, user_info in Bankomat.users.items():
            if user_info['pin'] == input_pin:
                account_number = acc_num
                break
        if account_number:
            break
        else:
            attempts -= 1
            console.print(f"[red]Noto'g'ri parol. Qolgan urinishlar: {attempts}[/red]")

    if not account_number:
        console.print("[bold red]Tizimdan chiqarildingiz. Urinishlar tugadi.[/bold red]")
        return

    atm = Bankomat(account_number)

    while True:
        console.print(Panel(
            "[1] Balansni ko'rish\n[2] Pul qo'shish\n[3] Naqd pul olish\n[4] PIN kodni o'zgartirish\n[5] Tranzaksiya tarixi\n[6] Pul o'tkazish\n[0] Chiqish",
            title="Menyu", subtitle="Iltimos tanlang", style="cyan"
        ))
        choice = Prompt.ask("Buyruqni tanlang")

        try:
            if choice == '1':
                bal = atm.show_balance()
                console.print(Panel(f"[bold yellow]Balansingiz: ${bal}[/bold yellow]", style="green"))

            elif choice == '2':
                amount = IntPrompt.ask("Pul miqdori")
                print(atm.deposit(amount))

            elif choice == '3':
                amount = IntPrompt.ask("Pul miqdori")
                print(atm.withdraw(amount))

            elif choice == '4':
                new_pin = Prompt.ask("Yangi PIN kodni kiriting", password=True)
                atm.change_pin(new_pin)

            elif choice == '5':
                atm.show_history()

            elif choice == '6':
                recipient = Prompt.ask("Qabul qiluvchi hisob raqami")
                amount = IntPrompt.ask("Pul miqdori")
                atm.transfer(recipient, amount)

            elif choice == '0':
                console.print("[bold magenta]OPERATSIYA TUGADI. RAHMAT![/bold magenta]")
                break

            else:
                console.print("[bold red]Noto'g'ri buyruq![/bold red]")
        
        except ValueError as e:
            console.print(f"[bold red]{e}[/bold red]")

main()
