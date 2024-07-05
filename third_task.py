import sys
from pathlib import Path
from colorama import Fore, Style



def print_directory_contents(path, indent=0):
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{" " * indent}{"📂"}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
                print_directory_contents(item, indent + 2)
            else:
                print(f"{" " * indent}{"📜"}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{" " * indent}{Fore.RED}Permission denied: {item.name}{Style.RESET_ALL}")


def main(received_directory):
    path = Path(received_directory)
    if not path.exists() or not path.is_dir():
        print(f"{Fore.RED}Error: The provided path is not a valid directory.{Style.RESET_ALL}")
        return
    else:
        print_directory_contents(path)


if __name__ == "__main__":
    directory = sys.argv[1]
    main(directory)
