from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Отримуємо поточну дату
    today = datetime.today().date()
    
    # Створюємо список для зберігання інформації про привітання
    upcoming_birthdays = []
    
    # Проходимось по кожному користувачеві
    for user in users:
        # Перетворюємо рядок з датою народження у datetime об'єкт
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Визначаємо день народження на наступний рік, якщо він вже минув у поточному році
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        
        # Визначаємо різницю між днем народження та сьогоднішньою датою
        days_until_birthday = (birthday - today).days
        
        # Перевіряємо, чи день народження випадає вперед на 7 днів включаючи поточний день
        if 0 <= days_until_birthday <= 7:
            # Перевіряємо, чи день народження припадає на вихідний
            if (today + timedelta(days=days_until_birthday)).weekday() >= 5:
                # Якщо так, переносимо дату привітання на наступний понеділок
                days_until_birthday += (7 - (today + timedelta(days=days_until_birthday)).weekday())
            
            # Додаємо ім'я користувача та дату привітання до списку
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": (today + timedelta(days=days_until_birthday)).strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
