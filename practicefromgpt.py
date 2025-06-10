# # Vazifa: Kitob nomli klass yarating. Unda nomi, 
# # muallifi va sahifalar_soni xususiyatlari bo‘lsin. 
# # get_info() metodi kitob haqida ma’lumot chiqarsin.




# class Kitob:
#     def __init__(self, nom, muallif, sahifalar):
#         self.name = nom
#         self.author = muallif
#         self.pages = sahifalar
        
#     def get_info(self):
#         return f"nomi: {self.name} | muallifi: {self.author} | sahifalar: {self.pages}"

# kitob1 = Kitob("Python Darslari", "John Doe", 250)
# print(kitob1.get_info())




# _______________________________________________________________________________________




# # 2. Klassga metodlar qo‘shish
# # Vazifa: Telefon klassi yarating. 
# # Unda model, firma, narx xususiyatlari bo‘lsin. chegirma(foiz) nomli metod yozing, 
# # bu metod telefon narxiga chegirma qo‘llasin.

# class Telefon:
#     def __init__(self, model, firma, narx):
#         self.model = model
#         self.firma = firma
#         self.narx = narx
        
#     def get_discount(self):
#         if self.narx >= 500:
#             discount = self.narx - 100
#             print(f"asl narx: {self.narx} chegirma narx: {discount}")

# telefon1 = Telefon('iphone', 'apple', 600)
# telefon1.get_discount()




# ___________________________________________________________________________




# # 3. Vorislash (inheritance)
# # Vazifa: Hayvon nomli klass yarating. 
# # So‘ng It va Mushuk klasslarini Hayvondan meros oling. 
# # Har bir hayvon o‘ziga xos ovoz_ber() metodiga ega bo‘lsin.

# class Hayvon:
#     def __init__(self, qol, oyoq):
#         self.arm = qol
#         self.leg = oyoq
        
# class It(Hayvon):
#     pass
        
#     def get_sound(self):
#         return 'woof'
        
# class Mushuk(Hayvon):
#     pass
        
#     def get_sound(self):
#         return 'meow'

# it1 = It(2, 2)
# mushuk1 = Mushuk(2, 2)

# print(it1.get_sound())  # Output: Woof!
# # print(mushuk1.get_sound())  # Output: Meow!




# ____________________________________________________________





# # "Texnika" parent klass. Konstruktorida esa (brand, model, type) parametrlari bor.
#     # info() - (brand, model, type) ni print qilib beradi.
    
# class Texnika:
#     def __init__(self, brend, model, yozish):
#         self.brand = brend
#         self.model = model
#         self.type = yozish
        
#     def get_info(self):
#         return f"{self.brand} {self.model} {self.type}"
    
# mashina1 = Texnika('chevrolet', 'cherry', '123')
# print(mashina1.get_info())



# ____________________________________________________________________________________________




# class Inson:
#     def __init__(self, ism, tyil):
#         self.name = ism
#         self.age = tyil  # Tug'ilgan yil
        
#     def get_name(self):
#         return self.name
        
#     def get_age(self):
#         yosh = 2025 - self.age
#         return yosh
        
# class Talaba(Inson):
#     def get_age(self):  # Bu metod "Inson" dagisini yangilab turibdi (overriding)
#         yosh = 2025 - self.age  # ✅ To‘g‘ri yozilishi shunday
#         return yosh

# talaba1 = Talaba('Faxriddin', 2000)
# print(talaba1.get_name())  # Chiqadi: Faxriddin
# print(talaba1.get_age())






# import random

# word_list = ["olma", "banan", "nok", "behi", "gilos", "uzum", "malina","kun.uz"]

# word = random.choice(word_list)
# guesses = set()

# while True:  # cheksiz sikl ochib, o'yinni davomiyligini ta'minlash uchun
#     display = ""
#     for letter in word:
#         if letter in guesses:
#             display += letter
#         else:
#             display += "_"

#     print(display)

#     if "_" not in display:
#         print("Tabriklaymiz, siz yutdingiz!")
#         break
#     guess = input("Harf o'ylang: ")
#     guesses.add(guess)
#     if guess not in word:
#         print("Xato")
#     else:
#         print("To'g'ri")

#     if len(guesses) == 10:
#         print("Uzr, siz barcha urinishlardan foydalanib bo'ldingiz!", word)
#         break








# # 1. Toq va juft sonlarni ajratish
# # Vazifa: Foydalanuvchi kiritgan sonlar ro'yxatidan juft va toq sonlarni alohida ajrating.

# sonlar = [1,2,3,4,4,5,6,7]
# for son in sonlar:
#     if son % 2 == 0:
#         print('juft')
#     else:
#         print('toq')







# 2. Stringdagi unli harflarni sanash
# Vazifa: Foydalanuvchi kiritgan matnda nechta unli harf borligini aniqlang. (a, e, i, o, u)

unli = 0
undosh = 0
txt = ['asd afskn wfjnonsf wfijnjowef awoj ef']
for i in txt:
    if i in 'aeiouy':
        unli += i
    elif i in undosh:
        undosh += 1
        print(txt)