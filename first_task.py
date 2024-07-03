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
            total_salarys += int(salary)    # Додаємо зарплату до загальної зарплати
            count += 1                      # Збільшуємо кількість рядків на 1

        average_salary = total_salarys / count   # Рахуємо середню заробітню плату
        return total_salarys, int(average_salary)  # Повертаємо загальну та середню зарплати

    # Обробляємо помилку "Файл не знайдено"
    except FileNotFoundError:
        print("Файл не знайдено")
        return 0, 0

    # Обробляємо помилку "Помилка обробки даних"
    except Exception:
        print("Помилка обробки даних")
        return 0, 0


# Отримуємо загальну суму та середню зарплату з файлу зарплат
total, average = total_salary("path/to/salary_file.txt")
# Виводимо результат обчислення загальної та середньої зарплати
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
