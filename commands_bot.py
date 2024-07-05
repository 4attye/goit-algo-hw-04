# Розбиваємо введений рядок на команду та аргументи,
# приводимо команду до нижнього регістру і видаляємо зайві пробіли,
# повертаємо команду і список аргументів
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


# Створюємо функцію "add_contact" де перевіряємо,чи передано аргументи,чи існує контак,
# розпаковуємо аргументи та додаємо новий контакт у словник якщо контакта не існує
def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: please provide a name and a phone number."
    else:
        name, phone = args
        if not name in contacts:
            contacts[name] = phone
            return "Contact added."
        else:
            return "Such a contact already exists."


# Створюємо функцію "change_contact" де перевіряємо,
# чи передано аргументи, розпаковуємо аргументи
# та якщо контакт існує оновлюємо номер телефону
def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: please provide a name and a new phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: contact not found."


# Створюємо функцію "show_phone" що перевіряє, чи передано аргумент,
# отримуємо ім'я з аргументів,якщо контакт існує повертаємо номер телефону
def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: please provide a name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Error: contact not found."


# Створюємо функцію "show_all" яка створюємо рядок для збереження результату,
# перевіряє, чи є контакти в словнику, проходить через всі контакти і додає їх в result
def show_all(contacts):
    # Створюємо рядок для збереження результату
    result = ""
    if not contacts:
        return "No contacts found."
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()