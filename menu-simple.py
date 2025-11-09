def input_data():
    text = input("Введите текст: ")
    return text


def algorithm(data):
    words = data.split()
    palindromes = []
    for word in words:
        # убираем знаки припенания
        clean_word = ""
        for char in word:
            if char.isalpha():  # оставляем только буквы
                clean_word += char
        # проверка на палиндром
        if len(clean_word) > 1:
            lower_word = clean_word.lower()
            if lower_word == lower_word[::-1]:
                palindromes.append(word)  # сохраняем оригинальное написание
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
    data = None
    result = None

    while True:
        print("\n" + "=" * 40)
        print("МЕНЮ:")
        print("1. Ввод данных")
        print("2. Выполнить алгоритм")
        print("3. Вывести результат")
        print("4. Выход")
        print("=" * 40)
        choice = input("Выберите пункт меню: ").strip()

        match choice:
            case "1":
                data = input_data()
                result = 0  # сброс результата при новых данных
                print("Данные успешно введены!")

            case "2":
                if data is None:
                    print("Ошибка: сначала введите данные (пункт 1)!")
                else:
                    result = algorithm(data)
                    print("Алгоритм выполнен!")

            case "3":
                if result is None:
                    print("Ошибка: сначала выполните алгоритм (пункт 2)!")
                else:
                    out_res(result)

            case "4":
                exit_prog()

            case _:
                print("Неверный пункт меню! Выберите от 1 до 4.")

if __name__ == "__main__":
    main()