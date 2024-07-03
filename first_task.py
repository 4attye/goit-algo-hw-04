
def total_salary(salary_file):
    try:
        with open(salary_file, "r") as file:
            lines = file.readline()

        total_salarys = 0
        count = 0

        for line in lines:
            name, salary = line.strip().split(',')
            total_salarys += int(salary)
            count += 1

        average_salary = total_salarys / count if count > 0 else 0

        return total_salarys, average_salary

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None


path_to_file = "salary_file.txt"
total, average = total_salary(path_to_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")