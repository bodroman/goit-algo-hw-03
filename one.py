from datetime import datetime

def get_days_from_today(date):
    # перетворюємо рядок дати з формату 'YYY.......' в об'єкт datetime
    given_date = datetime.strptime(date, '%Y-%m-%d')
    # отримуємо поточну дату
    current_date = datetime.today()
    # вираховуємо різницю між актуальною датою та заданою
    difference = current_date - given_date
    # повертаємо різницю у вигляді цілого числа
    return difference.days

# маємо наступний приклад із заданою датою 10 жовтня 2023 року:
given_date = '2023-10-10'
print(get_days_from_today(given_date))