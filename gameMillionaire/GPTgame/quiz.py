# quiz.py
# Test savollari bilan ishlovchi modul
import time
import random
from questions import questions  # Savollar tashqi fayldan olinadi

def get_player_name():
    # Foydalanuvchi ismini kiritadi
    return input("O'yinchining ismini kiriting: ")

def ask_question(index, question_data):
    # Bitta savolni ko‘rsatish va foydalanuvchi javobini tekshirish
    print(f"\nsavol {index + 1}/{len(questions)}")
    print(question_data["savol"])

    for variant in question_data["variantlar"]:
        print(variant)

    print("h - yordam")  # Yordam varianti
    javob = input("Javobni kiriting: ").lower()  # Javob kiritiladi

    if javob == question_data["tugri_javob"]:
        # To‘g‘ri javob bo‘lsa 1 ball
        print("Javob to'g'ri\n")
        return 1
    elif javob == "h":
        # Yordam so‘ralganda to‘g‘ri javob ko‘rsatiladi va 2 noto‘g‘ri javob olib tashlanadi
        tugri = question_data['tugri_javob']
        variantlar = question_data['variantlar']

        # To‘g‘ri variantni topamiz
        correct_option = [v for v in variantlar if v.startswith(tugri)][0]

        # Noto‘g‘ri variantlardan ikkitasini tanlab olib tashlaymiz
        incorrect_options = [v for v in variantlar if not v.startswith(tugri)]
        to_remove = random.sample(incorrect_options, 2)

        # Qolgan variantlarni chiqaramiz
        print("Yordam: Quyidagi variantlardan tanlang:")
        for v in variantlar:
            if v not in to_remove:
                print(v)

        # Foydalanuvchidan yana javob olish
        javob2 = input("Javobni kiriting: ").lower()
        if javob2 == tugri:
            print("Javob to'g'ri\n")
            return 1
        else:
            print(f"Noto'g'ri javob. To'g'ri javob — {tugri})\n")
            return 0
    else:
        # Noto‘g‘ri javob bo‘lsa 0 ball
        print("Noto'g'ri javob\n")
        return 0

def run_quiz():
    # To‘liq testni o‘tkazish funksiyasi
    name = get_player_name()
    score = 0

    for index, question_data in enumerate(questions):
        # Har bir savolga navbatma-navbat javob beriladi
        score += ask_question(index, question_data)
        time.sleep(1)  # Kichik kutish

    print(f"\nO'yin tugadi! {name} ning bali: {score}/{len(questions)}")
    return name, score, len(questions)  # Natijalar qaytariladi
