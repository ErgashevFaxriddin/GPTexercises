# main.py
# Asosiy fayl — foydalanuvchi tanlov qiladi va tegishli funksiyalar chaqiriladi

# quiz modulidan testni ishlatish funksiyasini chaqiramiz
from quiz import run_quiz
# rating modulidan reytingni ko'rsatish va saqlash funksiyalarini chaqiramiz
from rating import show_rating, save_rating

while True:
    # Foydalanuvchiga menyu ko‘rsatiladi
    print("\nKim millioner bo'lishni istaydi o'yiniga xush kelibsiz!")
    print("Buyruqni tanlang:")
    print("1 - o'ynash")
    print("2 - reyting")
    print("0 - dasturdan chiqish")
    tanlov = input("> ")  # Foydalanuvchi tanlovi olinadi

    if tanlov == "1":
        # Agar o'yin tanlansa, o'yin boshlanadi va natijalar saqlanadi
        name, score, total = run_quiz()  # name (ism), score (to'g'ri javoblar soni), total (jami savollar)
        save_rating(name, score, total)  # reyting fayliga saqlanadi
    elif tanlov == "2":
        # Reyting ko'rsatiladi
        show_rating()
    elif tanlov == "0":
        # Dasturdan chiqiladi
        break
    else:
        print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")

