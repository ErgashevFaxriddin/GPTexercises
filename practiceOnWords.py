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

def birinchi_unikal_harf(soz):
    soz = soz.lower()  
    harf_sana = {}

    for harf in soz:
        if harf.isalpha():  
            harf_sana[harf] = harf_sana.get(harf, 0) + 1

    for harf in soz:
        if harf.isalpha() and harf_sana[harf] == 1:
            return harf

    return "Unikal harf yo'q"

def most_letter(soz):
    harflar = {}

    for harf in soz.lower():
        if harf.isalpha():
            if harf in harflar:
                harflar[harf] += 1
            else:
                harflar[harf] = 1
        eng_kop = max(harflar, key=harflar.get)
    return eng_kop, harflar[eng_kop]
    
def count_letter(soz, harf):
    return soz.count(harf)
        
def main():
    soz = input('so\'z kiriting: ').lower()
    while True:
        print("0 - stop")
        print("1 - unli harflar")
        print("2 - undosh harflar")
        print("3 - unli harflar soni")
        print("4 - undosh harflar soni")
        print('5 - barcha harflar soni')
        print('6 - eng ko\'p foydalanilgan harf')
        print('7 - unikal harf')
        print('8 - harf takrorlanishi')
        
        tanlov = input('\n>>> ')
        if tanlov == '1':
            print(f"UNLI HARFLAR\n>>> {unli_harflar(soz)}\n")
        elif tanlov == '2':
            print(f"UNDOSH HARFLAR\n>>> {undosh_harflar(soz)}")
        elif tanlov == '3':
            print(f"UNLI HARFLAR SONI\n>>> {unlilar_len(soz)}")
        elif tanlov == '4':
            print(f"UNDOSH HARFLAR SONI\n>>> {undoshlar_len(soz)}")
        elif tanlov == '5':
            print(f"BARCHA HARFLAR SONI\n>>> {barcha_harflar(soz)}")
        elif tanlov == '6':
            print(f"ENG KOP FOYDALANILGAN HARF\n>>> {most_letter(soz)}")
        elif tanlov == '7':
            print(f"UNIKAL HARF\n>>> {birinchi_unikal_harf(soz)}")
        elif tanlov == '8':
            harf = input('HARF KIRITING\n>>> ')
            print(f"{harf} - HARFI {count_letter(soz, harf)} MARTA ISHLATILGAN")
        elif tanlov == '0':
            break
        else:
            print('notog\'ri buyruq kiritdingiz, \nIltimos qaytadan tekshiring')

main()