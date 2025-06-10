
# class Avto:
#     """Avtomobil klassi: brend, model, rang, km, tezlik"""
#     def __init__(self, brend, rusum, rang):
#         self.brand = brend
#         self.model = rusum
#         self.color = rang
#         self.km = 0
#         self.speed = 0

#     def get_info(self):
#         return f"Brend: {self.brand}, Model: {self.model}, Rang: {self.color}, KM: {self.km}, Tezlik: {self.speed} km/soat"

#     def get_model(self):
#         return self.model
    
#     def get_brand(self):
#         return self.brand
    
#     def get_color(self):
#         return self.color
    
#     def get_km(self):
#         return self.km  # sizda `sel.km` deb xatolik bor edi
    
#     def get_speed(self):
#         return self.speed

#     def update_km(self, yangi_km):
#         if yangi_km >= self.km:
#             self.km = yangi_km
#         else:
#             print("Xatolik: Yangi kilometr avvalgisidan kam bo'lmasligi kerak.")

#     def update_speed(self, new_speed):
#         self.speed = new_speed


# class Avtosalon:
#     """Avtosalon klassi"""
#     def __init__(self, nom, manzil, telegram, instagram, websayt):
#         self.name = nom
#         self.location = manzil
#         self.telegram = telegram
#         self.instagram = instagram
#         self.website = websayt
#         self.avtolar = []
        
#     def add_car(self, new_car):
#         """Yangi avtomobil qo‘shish"""
#         self.avtolar.append(new_car)
        
#     def avtos_info(self):
#         """Avtosalondagi barcha avtomobillar haqida ma'lumot"""
#         return [avto.get_info() for avto in self.avtolar]


# # Avto obyektlari
# avto1 = Avto('Chevrolet', 'Gentra', 'qora')
# avto2 = Avto('Hyundai', 'Sonata', 'oq')
# avto1.update_km(15000)
# avto2.update_speed(120)

# # Avtosalon obyektini yaratamiz
# salon = Avtosalon("AvtoSalon1", "Toshkent", "@avtosalon1", "avtosalon1", "www.avtosalon1.com")

# # Avtomobillarni qo‘shamiz
# salon.add_car(avto1)
# salon.add_car(avto2)

# # Ma'lumotlarni chiqaramiz
# for info in salon.avtos_info():
#     print(info)

# # Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
# # dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass 
# # va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)

# # print(dir(Avto))

# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Avto))


