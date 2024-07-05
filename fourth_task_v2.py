from commands_bots import (
    parse_input, add_contact,
    change_contact, show_all,
    show_phone)


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
    # Запускаємо головну функцію
    main()
