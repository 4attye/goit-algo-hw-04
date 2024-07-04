def total_salary(path):
    try:
        # Відкриваємо файл для читання й читаємо рядки
        with open(path, "r", encoding='utf-8') as file:
            lines = file.readlines()
        # Створюємо змінні для загальної зарплати та кількості рядків
        total_salarys = 0
        count = 0
        # Перебіраємо кожен рядок у списку lines
        for line in lines:
            name, salary = line.split(',')  # Розділяємо рядок на ім'я та зарплату
            total_salarys += int(salary)  # Додаємо зарплату до загальної зарплати
            count += 1  # Збільшуємо кількість рядків на 1

        average_salary = total_salarys / count  # Рахуємо середню заробітню плату
        return total_salarys, int(average_salary)  # Повертаємо загальну та середню зарплати

    # Обробляємо помилку "Файл не знайдено"
    except FileNotFoundError:
        return "Файл не знайдено"


    # Обробляємо помилку "Помилка обробки даних"
    except Exception:
        return "Помилка обробки даних"


try:
    # Отримуємо загальну суму та середню зарплату з файлу зарплат
    total, average = total_salary("path/to/salary_file.txt")
    # Виводимо результат обчислення загальної та середньої зарплати
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

except Exception:
    # Якщо виникає помилка повернення даних, викликаємо функцію total_salary ще раз й виводим яка саме сталась помилка
    print(total_salary("path/to/salary_file.txt"))
