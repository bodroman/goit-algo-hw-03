import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та плюсів
    cleaned_number = re.sub(r'\D', '', phone_number)
    
    # Перевіряємо, чи номер починається з плюса
    if cleaned_number.startswith('+'):
        # Якщо номер починається з плюса то перевіряємо, чи відповідає він формату +380
        if len(cleaned_number) == 12 and cleaned_number[1:4] == '380':
            # Якщо відповідає, повертаємо нормалізований номер
            return '+' + cleaned_number[1:]
        else:
            # Якщо не відповідає, повертаємо очищений номер без змін
            return cleaned_number
    else:
        # Якщо номер не починається з плюса, додаємо міжнародний код України
        return '+38' + cleaned_number

# Приклад використання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+0 44 123 4567",
    "0501234567",
    "    +(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "050-111-22-22",
    "050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
