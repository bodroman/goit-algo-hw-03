import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевіряємо відповідність вхідних параметрів до вказаних обмежень
    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
        return []

    # Генеруємо унікальні числа у заданому діапазоні
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    
    # Сортуємо та повертаємо список чисел
    return sorted(numbers)

# Приклад використання
min_num = 2
max_num = 60
quantity = 7
print(get_numbers_ticket(min_num, max_num, quantity))
