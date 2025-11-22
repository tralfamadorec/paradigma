def input_data():
    print("input_data \n")

def algorithm():
    print("algorithm \n")

def out_res():
    print("out_res \n")

def exit_prog():
    print("exit_prog \n")

def main():
    data_entered = False
    algorithm_done = False

    while True:
        print("\n=== МЕНЮ ===")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы")
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            input_data()
            data_entered = True
            algorithm_done = False  # сброс
        elif choice == "2":
            if not data_entered:
                print("Ошибка: сначала введите данные!")
            else:
                algorithm()
                algorithm_done = True
        elif choice == "3":
            if not algorithm_done:
                print("Ошибка: сначала выполните алгоритм!")
            else:
                out_res()
        elif choice == "4":
            exit_prog()
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()