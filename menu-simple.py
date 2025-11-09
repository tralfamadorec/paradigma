import random

def input_data():
    print("1. Ввести текст вручную")
    print("2. Сгенерировать случайный текст")
    choice = input("Выберите способ ввода (1 или 2): ").strip()
    match choice:
        case "1":
            text = input("Введите текст: ")
        case "2":
            text = rand_text()
            print(f"Сгенерированный текст: {text}")
        case _:
            print("Неверный выбор, используется ручной ввод.")
            text = input("Введите текст: ")

    return text

def rand_text():
    # случайный текст с палиндромами и обычными словами
    palindromes = [
        'топот', 'заказ', 'шалаш', 'Анна', 'комок', 'потоп', 'ротор',
        'дед', 'казак', 'мадам', 'поп', 'кабак', 'ракетар', 'наган'
    ]
    regular_words = [
        'программа', 'компьютер', 'алгоритм', 'текст', 'данные', 'меню',
        'функция', 'разработка', 'приложение', 'консоль', 'интерфейс',
        'палиндром', 'система', 'код', 'тестирование', 'пользователь',
        'выполнение', 'результат', 'обработка', 'поиск', 'анализ'
    ]
    text_words = []
    for _ in range(random.randint(8, 12)):
        if random.choice([True, False]):  # 50% шанс на попадение палиндрома в текст
            word = random.choice(palindromes)
            if random.choice([True, False, False]):  # 33% шанс на добавление знаков препинания в текст
                word += random.choice(['.', ',', '!', '?'])
            text_words.append(word)
        else:
            text_words.append(random.choice(regular_words))

    return ' '.join(text_words)

def algorithm(data):
    words = data.split()
    palindromes = []
    for word in words:
        # убираем знаки препинания
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