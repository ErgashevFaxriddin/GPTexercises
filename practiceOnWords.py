# so'zdagi harflar ustida amallar
# Ergashev Faxriddin
# optimal

def unli_harflar(soz):
    unlilar = 'aeiou'
    return [harf for harf in soz if harf in unlilar]

def undosh_harflar(soz):
    unlilar = 'aeiou'
    return [harf for harf in soz if harf.isalpha() and harf not in unlilar]

def unlilar_len(soz):
    return len(unli_harflar(soz))

def undoshlar_len(soz):
    return len(undosh_harflar(soz))

def barcha_harflar(soz):
    harflar = len(soz)
    return harflar

def unikal_harf(soz):
    harf_sana = {}
    # Harflarni kichik holatda hisoblash uchun (A va a ni bitta deb olish uchun)
    for harf in soz:
        if harf.isalpha():
            harf = harf.lower()
            harf_sana[harf] = harf_sana.get(harf, 0) + 1

    # Endi asl harfni chiqarish uchun yana asl so‘z bo‘yicha yuramiz
    for harf in soz:
        if harf.isalpha() and harf_sana[harf.lower()] == 1:
            return harf

    return "Unikal harf yo'q"

def most_letter(soz):
    soz = soz.lower()
    harflar = {}
    
    for harf in soz:
        if harf.isalpha():
            if harf in harflar:
                harflar[harf] += 1
            else:
                harflar[harf] = 1
        
    natija = []
    for harf, miqdor in harflar.items():
        if miqdor >= 2:
            natija.append(harf)        
    return natija

def count_letter(soz, harf):
    return soz.count(harf)
        

def main():
    soz = input('so\'z kiriting: ').lower()
    while True:
        print("0 - stop")
        print("1 - unli harflar")
        print("2 - undosh harflar")
        print('3 - barcha harflar soni')
        print('4 - eng ko\'p foydalanilgan harf')
        print('5 - unikal harf')
        print('6 - harf takrorlanishi')
        
        tanlov = input('\n>>> ')
        if tanlov == '1':
            print(f"UNLI HARFLAR\n>>> {unli_harflar(soz)}\n>>> UNLI HARFLAR SONI\n>>> {unlilar_len(soz)}")
        elif tanlov == '2':
            print(f"UNDOSH HARFLAR\n>>> {undosh_harflar(soz)}\n>>> UNDOSH HARFLAR SONI\n>>> {undoshlar_len(soz)}")
        elif tanlov == '3':
            print(f"BARCHA HARFLAR SONI\n>>> {barcha_harflar(soz)}")
        elif tanlov == '4':
            print(f"ENG KOP FOYDALANILGAN HARF\n>>> {most_letter(soz)}")
        elif tanlov == '5':
            print(f"UNIKAL HARF\n>>> {unikal_harf(soz)}")
        elif tanlov == '6':
            harf = input('HARF KIRITING\n>>> ')
            print(f"{harf} HARFI {count_letter(soz, harf)} MARTA ISHLATILGAN")
        elif tanlov == '0':
            break
        else:
            print('notog\'ri buyruq kiritdingiz, \nIltimos qaytadan tekshiring')

main()
