from student.student_manager import StudentManager

def main():
    manager = StudentManager()
    
    while True:
        print('\n' + '='*30)
        print('     O\'quvchilar ro\'yxati')
        print('='*30)
        print('1 - O\'quvchi qo\'shish')
        print('2 - O\'quvchilarni ko\'rish')
        print('3 - O\'quvchini o\'chirish')
        print('0 - Dasturdan chiqish')
        print('-'*30)

        tanlov = input('Tanlang >>> ').strip()

        if tanlov == '1':
            print('\n--- O\'quvchi qo\'shish ---')
            name = input('Ism: ').strip()
            
            if not name:
                print("❌ Ism bo'sh bo'lishi mumkin emas!")
                continue
                
            try:
                age = int(input('Yosh: '))
                if age <= 0:
                    print("❌ Yosh musbat son bo'lishi kerak!")
                    continue
                    
                manager.add_student(name, age)
                print(f"✅ {name} muvaffaqiyatli qo'shildi!")
                
            except ValueError:
                print("❌ Yosh butun son bo'lishi kerak!")
                
        elif tanlov == '2':
            print('\n--- O\'quvchilar ro\'yxati ---')
            manager.list_students()
            
        elif tanlov == '3':
            print('\n--- O\'quvchini o\'chirish ---')
            manager.list_students()
            
            if manager.students:  # Agar ro'yxat bo'sh bo'lmasa
                try:
                    idx = int(input('O\'chirish uchun ID raqam: ')) - 1
                    
                    if 0 <= idx < len(manager.students):
                        removed_student = manager.students[idx]
                        manager.remove_student(idx)
                        print(f"✅ {removed_student['name']} o'chirildi!")
                    else:
                        print("❌ Noto'g'ri ID raqam!")
                        
                except ValueError:
                    print("❌ Faqat raqam kiriting!")
            else:
                print("📝 Ro'yxat bo'sh!")
                
        elif tanlov == '0':
            print('\n👋 Dastur yakunlandi! Xayr!')
            break
            
        else:
            print("❌ Noto'g'ri tanlov! Iltimos, 0-3 orasida raqam kiriting.")

if __name__ == "__main__":
    main()