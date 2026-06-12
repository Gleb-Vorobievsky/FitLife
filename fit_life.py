# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
MILL_IN_LITER = 1000
SMALL_AGE = 10
MIDDLE_AGE = 20
SMAAL_AGE_LIST = (1, 2, 3, 4)

# Знакомство
user_name = input('Привет! Напиши свое имя:')
while True:
    try:
        user_age = int(input('А теперь напиши свой возраст:'))
        break
    except ValueError:
        print("Напиши возраст целым числом")


# Сбор данных
def input_user_weight():
    """Функция для корректного ввода веса пользователя"""
    while True:
        try:
            user_weight = float(input('Напиши свой вес в кг (например: 64):'))
            return user_weight
        except ValueError:
            print("Напиши свой вес числом с плавающей точкой, либо без нее")


def input_user_height():
    """Функция для корректного ввода роста пользователя"""
    while True:
        try:
            user_height = float(input('Напиши свой рост в м (например: 1.7):'))
            return user_height
        except ValueError:
            print("Напиши свой рост числом с плавающей точкой, либо без нее")


def bmi(user_weight, user_height):
    """Рассчет Индекса массы тела"""
    """Функция будет возвращать либо целые числа либо дробные"""
    index = round(user_weight / (user_height ** 2), 1)
    if index % 1 == 0:
        index = int(index)
    return index


def water_normal(user_weight):
    """Подсчет нормы воды"""
    """Функция будет возвращать либо целые числа либо дробные"""
    user_normal_water = (user_weight * WATER_PER_KG) / MILL_IN_LITER
    if user_normal_water % 1 == 0:
        user_normal_water = int(user_normal_water)
    return user_normal_water


def symbol(user_age):
    """Объявим функцию для вычисления"""
    """корректного отображения возраста в 'годах' или 'лет'"""
    if user_age < SMALL_AGE:
        if user_age in SMAAL_AGE_LIST:
            return "г."
        return "л."
    elif SMALL_AGE <= user_age < MIDDLE_AGE:
        return "л."
    elif user_age >= MIDDLE_AGE:
        if user_age % 10 in SMAAL_AGE_LIST:
            return "г."
        return "л."


total_user_weight = input_user_weight()
total_user_height = input_user_height()
index_user_weight = bmi(total_user_weight, total_user_height)
water_for_user = water_normal(total_user_weight)
symbol_for_age = symbol(user_age)

# Вывод красивого результата
print(f'Расчет для пользователья {user_name} ({user_age} {symbol_for_age})!')
print(f'Твой Индекс Массы Тела: {index_user_weight}')
print(f'Рекомендуемая норма воды: {water_for_user} л. в день')
print("Расчет окончен. Будьте здоровы!")
