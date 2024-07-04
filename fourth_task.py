def parse_input(user_input):
    # Розбиваємо введений рядок на команду та аргументи
    cmd, *args = user_input.split()
    # Приводимо команду до нижнього регістру і видаляємо зайві пробіли
    cmd = cmd.strip().lower()
    # Повертаємо команду і список аргументів
    return cmd, args


def add_contact(args, contacts):
    # Перевіряємо,чи передано аргументи
    if len(args) != 2:
        return "Error: please provide a name and a phone number."
    # Розпаковуємо аргументи в змінні name та phone
    name, phone = args
    # Додаємо новий контакт у словник
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    # Перевіряємо,чи передано аргументи
    if len(args) != 2:
        return "Error: please provide a name and a new phone number."
    # Розпаковуємо аргументи в змінні name та phone
    name, phone = args
    # Якщо контакт існує, оновлюємо номер телефону
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: contact not found."


def show_phone(args, contacts):
    # Перевіряє, чи передано аргумент name
    if len(args) != 1:
        return "Error: please provide a name."
    # Отримує ім'я з аргументів
    name = args[0]
    # Якщо контакт існує, повертаємо номер телефону
    if name in contacts:
        return contacts[name]
    else:
        return "Error: contact not found."


def show_all(contacts):
    # Створюємо рядок для збереження результату
    result = ""
    # Перевіряє, чи є контакти в словнику
    if not contacts:
        return "No contacts found."
    # Проходить через всі контакти і додає їх в result
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    # Повертаємо результат
    return result.strip()


def main():
    # Створюємо порожній словник для контактів
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        # Отримує від данні користувача
        user_input = input("Enter a command: ")
        # Парсить введення користувача на команду та аргументи
        command, args = parse_input(user_input)

        # Якщо ввели команду "close" або "exit", програма завершує роботу
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        # Якщо ввели команду "hallo", виводяться привітання
        elif command == "hello":
            print("How can I help you?")
        # Якщо ввели команду "add", додається контакт
        elif command == "add":
            print(add_contact(args, contacts))
        # Якщо ввели команду "change", змінюєтьса існуючий номер
        elif command == "change":
            print(change_contact(args, contacts))
        # Якщо ввели команду "phone", виводяться номер телефону
        elif command == "phone":
            print(show_phone(args, contacts))
        # Якщо ввели команду "all", виводяться всі контакти
        elif command == "all":
            print(show_all(contacts))
        # Якщо команда не розпізнана, виводить повідомлення про помилку
        else:
            print("Invalid command.")


if __name__ == "__main__":
    # Запускає головну функцію
    main()

