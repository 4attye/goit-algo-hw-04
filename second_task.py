def get_cats_info(path):
    try:
        # filtered_list = ""
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
            # Додаємо словник до списку
            list_of_dictionaries.append(dictionery)

        return list_of_dictionaries  # Повертаємо оброблений список
        # Або. Переносимо кожен словник в новий рядок
        # for dictionary_from_list in list_of_dictionaries:
        #      filtered_list += f"{dictionary_from_list}\n"
        # return filtered_list

    except FileNotFoundError:  # Обробляємо помилку якщо файл незнайдено
        return "File not found"

    except ValueError:  # Обробляємо помилку якщо файл пошкоджено
        return "Data processing error"


cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
