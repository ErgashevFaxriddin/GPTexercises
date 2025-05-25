# rating.py
# Reyting ma'lumotlarini saqlash va ko'rsatish moduli
import json  # JSON fayllar bilan ishlash
import os    # Fayl mavjudligini tekshirish

REYTING_FAYL = "reyting.json"  # Reytinglar saqlanadigan fayl nomi

def save_rating(name, score, total):
    # Reyting fayliga yangi o'yinchi natijasini qo'shadi
    rating_data = []  # Bo'sh ro'yxat tayyorlanadi

    if os.path.exists(REYTING_FAYL):  # Fayl mavjudligini tekshiradi
        with open(REYTING_FAYL, "r") as file:
            rating_data = json.load(file)  # Mavjud reytinglar o'qiladi

    rating_data.append({"name": name, "score": score, "total": total})  # Yangi natija qo'shiladi

    with open(REYTING_FAYL, "w") as file:
        json.dump(rating_data, file, indent=4)  # Yangilangan ma'lumotlar faylga yoziladi

def show_rating():
    # Reytingni ekranga chiqaradi
    if not os.path.exists(REYTING_FAYL):
        print("Reyting ma'lumotlari topilmadi.")
        return

    with open(REYTING_FAYL, "r") as file:
        data = json.load(file)
        print("\nREYTING:")
        for i, player in enumerate(sorted(data, key=lambda x: x['score'], reverse=True), 1):
            # Har bir o'yinchi reytingda chiqariladi, balga ko'ra kamayish tartibida
            print(f"{i}. {player['name']} - {player['score']}/{player['total']}")
