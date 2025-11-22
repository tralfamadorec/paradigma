import random
from menu_template import is_int, enter_valid_int

""" ОСНОВНЫЕ ФУНКЦИИ МЕНЮ """

def input_data(): # ввод исходных данных
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
                parts = row_input.split()
                if len(parts) != n:
                    print(f"Ошибка: должно быть ровно {n} чисел.")
                    continue
                row = []
                for x in parts:
                    if is_int(x):
                        row.append(int(x))
                    else:
                        print("Ошибка: все элементы должны быть целыми числами.")
                        row = None
                        break
                if row is not None:
                    break
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
    print("Алгоритм выполняется...")
    matrix = data
    n = len(matrix)
    if n == 0:
        return {"result": None}
    min_elements = []
    for k in range(-n + 1, n):
        diagonal = []
        for i in range(n):
            j = n - 1 - i - k  # формула для побочной диагонали со смещением k
            if 0 <= j < n:
                diagonal.append(matrix[i][j])
        if diagonal:
            min_elements.append(min(diagonal))

    result_value = max(min_elements) if min_elements else None
    return {"result": result_value}

def out_res(result):
    value = result["result"]
    if value is not None:
        print(f"\nРезультат: {value}")
    else:
        print("\nРезультат не определён.")

def exit_prog():
    print("Выход из программы... \n")

""" ГЛАВНАЯ ФУНКЦИЯ """

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
                    result = algorithm(data)  # сохраняем реальный результат
            case "3":
                if result is None:
                    print("Ошибка: сначала выполните алгоритм!")
                else:
                    out_res(result)
            case "4":
                exit_prog()
                break
            case _:
                print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()