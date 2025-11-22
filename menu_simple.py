import random

def is_int(s):
    if s.startswith('-'):
        return s[1:].isdigit()
    return s.isdigit()

def enter_valid_int(prompt):
    while True:
        value = input(prompt).strip()
        if is_int(value):
            return int(value)
        print("Ошибка: введите целое число.")

def input_data():
    print("\nВыберите способ ввода данных:")
    print("1. Вручную")
    print("2. Случайная генерация")
    choice = input("Ваш выбор: ").strip()

    n = enter_valid_int("Введите размер квадратной матрицы N: ")
    if n <= 0:
        print("Размер матрицы должен быть положительным. Установлено N = 1.")
        n = 1

    if choice == "1":
        matrix = []
        print("Введите элементы матрицы построчно (через пробел):")
        for i in range(n):
            while True:
                row_input = input(f"Строка {i + 1}: ").strip()
                row = row_input.split()
                if len(row) != n:
                    print(f"Ошибка: должно быть ровно {n} чисел.")
                    continue
                # Проверка, что все элементы — целые числа
                try:
                    row = [int(x) for x in row]
                    break
                except ValueError:
                    print("Ошибка: все элементы должны быть целыми числами.")
            matrix.append(row)
    else:
        min_val = enter_valid_int("Минимальное значение: ")
        max_val = enter_valid_int("Максимальное значение: ")
        if min_val > max_val:
            min_val, max_val = max_val, min_val
        matrix = [
            [random.randint(min_val, max_val) for _ in range(n)]
            for _ in range(n)
        ]
        print("Сгенерирована матрица:")
        for row in matrix:
            print(row)

    return matrix

def algorithm(data):
    print("algorithm \n")

def out_res():
    print("out_res \n")

def exit_prog():
    print("exit_prog \n")

def main():
    data = None
    result = None

    while True:
        print("\n=== МЕНЮ ===")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы")
        choice = input("Выберите пункт: ").strip()

        match choice:
            case "1":
                data = input_data()
                result = None
            case "2":
                if data is None:
                    print("Ошибка: сначала введите данные!")
                else:
                    algorithm(data)
                    result = "done"
            case "3":
                if result is None:
                    print("Ошибка: сначала выполните алгоритм!")
                else:
                    out_res()
            case "4":
                exit_prog()
                break
            case _:
                print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()