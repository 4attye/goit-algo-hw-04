def get_cats_info(path):
    try:
        # Відкриваємо файл для читання й читаємо рядки
        with open(path, "r", encoding='utf-8') as file:
            lines = file.readlines()

        list_of_dictionaries = []  # Створюємо список словників
        # Перебіраємо кожен рядок у списку lines
        for line in lines:
            # Розділяємо рядок на id та name та age
            cat_id, cat_name, cat_age = line.strip().split(",")
            # Додаємо отримані значення до словника
            dictionery = {
                "id": cat_id,
                "name": cat_name,
                "age": cat_age}
            list_of_dictionaries.append(dictionery)  # Додаємо словник до списку
        return list_of_dictionaries  # Повертаємо оброблений список

    except FileNotFoundError:  # Обробляємо помилку якщо файл незнайдено
        return "Файл не знайдено"

    except ValueError:  # Обробляємо помилку якщо файл пошкоджено
        return "Файл пошкоджено"


cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
