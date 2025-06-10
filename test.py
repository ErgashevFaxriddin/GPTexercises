# Katta dastur: lambda, map, reduce, filter, rekursiv funksiya, iterator, generator, closure, dekorator
from functools import reduce

# === Dekorator: Har bir bosqichni log qilish uchun ===
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Funksiya chaqirildi: {func.__name__} bilan argumentlar: {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# === Closure: dinamik ko'paytiruvchi funksiyalar yaratish ===
def create_multiplier(factor):
    def multiplier(x):
        return x * factor  # closure tashqi o'zgaruvchi 'factor'ni eslab qoladi
    return multiplier

# === Generator: Fibonacci sonlarini beruvchi generator ===
@logger
def fibonacci_gen(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

# === Iterator: maxgacha toq sonlar generatori ===
class OddIterator:
    def __init__(self, max_val):
        self.max_val = max_val
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_val:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

# === Rekursiv funksiya: Faktorial hisoblash ===
@logger
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# === Asosiy dastur ===
@logger
def main():
    sonlar = list(range(1, 11))  # 1 dan 10 gacha sonlar
    print("Asl sonlar:", sonlar)

    # Lambda: sonni kvadratga oshirish
    kvadrat = lambda x: x ** 2
    kvadratlar = list(map(kvadrat, sonlar))
    print("Lambda & Map bilan kvadratlar:", kvadratlar)

    # Filter: faqat juft sonlarni ajratish
    juftlar = list(filter(lambda x: x % 2 == 0, sonlar))
    print("Filter bilan juftlar:", juftlar)

    # Reduce: barcha sonlar yig'indisi
    jami = reduce(lambda x, y: x + y, sonlar)
    print("Reduce bilan yig'indi:", jami)

    # Rekursiv: Faktorial hisoblash
    print("Faktorial(5):", factorial(5))

    # Iterator: max 10 gacha toq sonlar
    print("Iterator bilan toq sonlar:", list(OddIterator(10)))

    # Generator: Fibonacci sonlar
    print("Generator bilan Fibonacci:", list(fibonacci_gen(7)))

    # Closure: sonlarni 3 ga ko'paytirish
    multiply_by_3 = create_multiplier(3)
    print("Closure bilan 5 * 3:", multiply_by_3(5))

main()
