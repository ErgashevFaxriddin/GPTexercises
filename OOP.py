# class Talaba:
#     def __init__(self, ism, yosh, guruh, fakultet, yonalish):
#         self.name = ism
#         self.age = yosh
#         self.group = guruh
#         self.faculity = fakultet
#         self.major = yonalish
        
#     def get_name(self):
#         return self.name
    
#     def get_age(self, yil):
#         return self.age - yil

#     def get_group(self):
#         return self.group

#     def get_faculity(self):
#         return self.faculity

#     def get_yonalish(self):
#         return self.major


#     def tanishtir(self):
#         return f"ism: {self.name} \nyosh: {self.age} \nyo'nalish: {self.major}"
    
#     def __str__(self):
#         return f"{self.name}, {self.age} yosh, {self.group}, {self.faculity}, {self.major}"


# talaba1 = Talaba('Faxriddin', 21, '660-23', 'Biznes', 'Digital Economy')
# talaba2 = Talaba('Muslima', 21, '990-22', 'Matematika', 'Oliy Matematika')

# # talaba1.tanishtir()
# # print(talaba1.get_name())
# # print(talaba2.get_age())

# # Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. 
# # Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting 
# # (ism, foydalanuvchi ismi, email, va hokazo)

# class User:
#     def __init__(self, ism, familiya, e_mail):
#         self.name = ism
#         self.surname = familiya
#         self.e_mail = e_mail
    
#     def get_name(self):
#         """talabaning ismi"""
#         return self.name
    
#     def get_surname(self):
#         """talabaning familiyasi"""
#         return self.surname
    
#     def get_e_mail(self):
#         """talabaning emaili"""
#         return self.e_mail
    
#     def update_bosqich(self):
#         """talabaning bosqichini 1 taga oshiruvchi metod"""
#         if hasattr(self, 'bosqich'):
#             self.bosqich += 1
#         else:
#             self.bosqich = 1
        
#     def set_bosqich(self, yangi_bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = yangi_bosqich


#     # Klassga bir nechta metodlar qo'shing, 
#     # jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin 
#     # (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).

#     # Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.

#     def get_info(self):
#         return f"foydalanuvchi ismi: {self.name} \nfoydalanuvchi familiyasi: {self.surname} \nfoydalanuvchi e-mail: {self.e_mail}"

# foydalanuvchi1 = User("Alijon", "Valiyev", "alijon1994@gmail.com")
# print(foydalanuvchi1.get_info())

# class Fan:
#     """fanga talabalarni qoshish"""
#     def __init__(self, nomi):
#         self.name = nomi
#         self.talablar_soni = 0
#         self.talabalar_royxati = []
    
#     def add_student(self, talaba):
#         """fanga talabalar qoshish"""
#         self.talabalar_royxati.append(talaba)
#         self.talabalar_soni += 1

# english = Fan("English")
# matem = Fan("Mathematics")
# english.add_student(talaba1)

# # Talaba klassi
# class Talaba:
#     def __init__(self, ism, yosh, guruh, fakultet, yonalish):
#         self.name = ism
#         self.age = yosh
#         self.group = guruh
#         self.faculty = fakultet  
#         self.major = yonalish
        
#     def get_name(self):
#         return self.name
    
#     def get_age(self, yil):
#         """Berilgan yil orqali yosh hisoblash"""
#         return self.age - yil

#     def get_group(self):
#         return self.group

#     def get_faculty(self):
#         return self.faculty

#     def get_major(self):
#         return self.major

#     def get_info(self):
#         return f"Ism: {self.name} Yosh: {self.age} Yo'nalish: {self.major}"

#     def set_yosh(self, yangi_yosh):
#         self.age = yangi_yosh
#         return f"Yosh {yangi_yosh} ga o'zgartirildi"
    
#     def update_yosh(self):
#         self.age += 1

# # Obyektlar
# talaba1 = Talaba('Faxriddin', 21, '660-23', 'Biznes', 'Digital Economy')
# talaba2 = Talaba('Muslima', 21, '990-22', 'Matematika', 'Oliy Matematika')

# # Obyekt yaratish
# # foydalanuvchi1 = User("Alijon", "Valiyev", "alijon1994@gmail.com")
# # print(foydalanuvchi1.get_info())


# # Fan klassi (fanga talabalar qo‘shish)
# class Fan:
#     """Fanga talabalarni qo‘shish uchun klass"""
#     def __init__(self, nomi):
#         self.name = nomi
#         self.talabalar_royxati = []
#         self.talabalar_soni = 0

#     def add_student(self, talaba):
#         """Talabani fan ro'yxatiga qo‘shish"""
#         self.talabalar_royxati.append(talaba)

#     def get_students(self):
#         """Talabalar ro'yxatini chiqarish"""
#         # return [str(talaba) for talaba in self.talabalar_royxati]
#         return [talaba.get_info() for talaba in self.talabalar_royxati]

# # Fan obyektlari
# english = Fan("English")
# matem = Fan("Matematika")
# matem.add_student(talaba1)
# # print(matem.talabalar_royxati) #talabalar royxatini korish
# # print(matem.talabalar_soni()) #talalabalar sonini korish
# # print(matem.talabalar_royxati[0].age) #royxatdagi talabaning ismini korish
# # print(matem.talabalar_royxati[0].get_info())
# # print(matem.get_students()) 
# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]
# # print(see_methods(Talaba))
# # Talaba qo‘shish
# english.add_student(talaba1)
# english.add_student(talaba2)

# # Chiqarish
# print("English fanidagi talabalar:")
# for info in english.get_students():
#     print(info)

# print(talaba1.set_yosh(22))  
# print(talaba1.set_yosh(21))
# print(talaba1.update_yosh())




# User klassi (foydalanuvchi)
# class User:
#     def __init__(self, ism, familiya, e_mail):
#         self.name = ism
#         self.surname = familiya
#         self.e_mail = e_mail
#         self.bosqich = 1  # default qiymat

#     def get_name(self):
#         return self.name
    
#     def get_surname(self):
#         return self.surname
    
#     def get_e_mail(self):
#         return self.e_mail
    
#     def update_bosqich(self):
#         """Bosqichni 1 taga oshirish"""
#         self.bosqich += 1
        
#     def set_bosqich(self, yangi_bosqich):
#         """Bosqichni belgilash"""
#         self.bosqich = yangi_bosqich

#     def get_info(self):
#         return f"Foydalanuvchi: {self.name} {self.surname}, email: {self.e_mail}, bosqich: {self.bosqich}"

# Avto degan yangi klass yarating. 
# Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar 
# (model, rang, korobka, narh va hokazo) qo'shing. 
# Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)

class Avto:
    """Avtomobil klassi: brend, model, rang, km, tezlik"""
    def __init__(self, brend, rusum, rang):
        self.brand = brend
        self.model = rusum
        self.color = rang
        self.km = 0
        self.speed = 0

    def get_info(self):
        return f"Brend: {self.brand}, Model: {self.model}, Rang: {self.color}, KM: {self.km}, Tezlik: {self.speed} km/soat"

    def get_model(self):
        return self.model
    
    def get_brand(self):
        return self.brand
    
    def get_color(self):
        return self.color
    
    def get_km(self):
        return self.km  # sizda `sel.km` deb xatolik bor edi
    
    def get_speed(self):
        return self.speed

    def update_km(self, yangi_km):
        if yangi_km >= self.km:
            self.km = yangi_km
        else:
            print("Xatolik: Yangi kilometr avvalgisidan kam bo'lmasligi kerak.")

    def update_speed(self, new_speed):
        self.speed = new_speed


class Avtosalon:
    """Avtosalon klassi"""
    def __init__(self, nom, manzil, telegram, instagram, websayt):
        self.name = nom
        self.location = manzil
        self.telegram = telegram
        self.instagram = instagram
        self.website = websayt
        self.avtolar = []
        
    def add_car(self, new_car):
        """Yangi avtomobil qo‘shish"""
        self.avtolar.append(new_car)
        
    def avtos_info(self):
        """Avtosalondagi barcha avtomobillar haqida ma'lumot"""
        return [avto.get_info() for avto in self.avtolar]


# Avto obyektlari
avto1 = Avto('Chevrolet', 'Gentra', 'qora')
avto2 = Avto('Hyundai', 'Sonata', 'oq')
avto1.update_km(15000)
avto2.update_speed(120)

# Avtosalon obyektini yaratamiz
salon = Avtosalon("AvtoSalon1", "Toshkent", "@avtosalon1", "avtosalon1", "www.avtosalon1.com")

# Avtomobillarni qo‘shamiz
salon.add_car(avto1)
salon.add_car(avto2)

# Ma'lumotlarni chiqaramiz
for info in salon.avtos_info():
    print(info)
