# проверяет корректность ввода пользователя
def validate_menu_choice(choice, valid_choices):
    return choice in valid_choices

# отображение меню
def get_menu_choice(menu_title, options):
    while True:
        print(f"\n{'=' * 40}")
        print(menu_title)
        print('=' * 40)
        for key, description in options.items():
            print(f"{key}. {description}")
        print('=' * 40)
        choice = input("Выберите пункт меню: ").strip()
        if validate_menu_choice(choice, options.keys()):
            return choice
        else:
            print(f"Ошибка: введите один из вариантов {list(options.keys())}")

# запуск меню
def run_menu(menu_title, menu_options):
    display_options = {key: description for key, (description, _) in menu_options.items()}
    while True:
        choice = get_menu_choice(menu_title, display_options)
        # получаем и выполняем выбранную функцию
        description, function = menu_options[choice]
        should_exit = function()
        if should_exit:
            break