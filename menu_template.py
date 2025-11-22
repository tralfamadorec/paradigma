def is_int(s): # проверяет, можно ли преобразовать строку в целое число
    if not s:
        return False
    if s[0] == '-':
        return len(s) > 1 and s[1:].isdigit()
    return s.isdigit()

def enter_valid_int(prompt): # запрашивает у пользователя целое число с проверкой
    while True:
        value = input(prompt).strip()
        if is_int(value):
            return int(value)
        print("Ошибка: введите целое число.")