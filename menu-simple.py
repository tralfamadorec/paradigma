def input_data():
    text = input("Введите текст: ")
    return text

def algorithm(data):
    # упрощенный алгоритм ищет слова, которые читаются одинаково с начала и конца
    words = data.split()
    palindromes = []
    for word in words:
        # пока что проверка без учета регистра и знаков препинания
        if len(word) > 1 and word.lower() == word.lower()[::-1]:
            palindromes.append(word)
    print(f"Найдено палиндромов: {len(palindromes)}")
    return palindromes

def out_res(result):
    print("РЕЗУЛЬТАТЫ ПОИСКА")
    if result:
        print("Найденные палиндромы:")
        i = 1
        for palindrome in result:
            print(f"  {i}. {palindrome}")
            i += 1
    else:
        print("Палиндромы не найдены")

def exit_prog():
    print("Выход из программы...")
    exit()

def main():
    data = 0
    result = 0

    while True:
        print("\n" + "=" * 40)
        print("МЕНЮ:")
        print("1. Ввод данных")
        print("2. Выполнить алгоритм")
        print("3. Вывести результат")
        print("4. Выход")
        print("=" * 40)
        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            data = input_data()
            result = 0  # сброс результата при новых данных
            print("Данные успешно введены!")

        elif choice == "2":
            if data == 0:
                print("Ошибка: сначала введите данные (пункт 1)!")
            else:
                result = algorithm(data)
                print("Алгоритм выполнен!")

        elif choice == "3":
            if result == 0:
                print("Ошибка: сначала выполните алгоритм (пункт 2)!")
            else:
                out_res(result)

        elif choice == "4":
            exit_prog()

        else:
            print("Неверный пункт меню! Выберите от 1 до 4.")

if __name__ == "__main__":
    main()