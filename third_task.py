import sys
from pathlib import Path
from colorama import init, Fore


def print_directory_structure(path, indent_level=0):
    # Ініціалізація бібліотеки colorama для роботи з кольорами
    init(autoreset=True)

    # Отримання шляху до директорії
    dir_path = Path(path)

    # Перевірка чи шлях є директорією
    if not dir_path.is_dir():
        print(Fore.RED + f"Шлях {path} не є директорією або не існує.")
        return

    # Проходження по всіх файлах та піддиректоріях
    for item in dir_path.iterdir():
        indent = ' ' * indent_level
        if item.is_dir():
            print(Fore.BLUE + indent + '📂 ' + item.name)
            print_directory_structure(item, indent_level + 4)
        else:
            print(Fore.GREEN + indent + '📜 ' + item.name)


if __name__ == "__main__":
    # Перевірка чи був переданий шлях як аргумент командного рядка
    if len(sys.argv) != 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії як аргумент.")
    else:
        path_to_directory = sys.argv[1]
        print_directory_structure(path_to_directory)
