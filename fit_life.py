# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
MILL_IN_LITER = 1000

# Знакомство
user_name = input('Привет! Напиши свое имя:')
while True:
    try:
        user_age = int(input('А теперь напиши свой возраст:'))
        break
    except ValueError:
        print("Напиши возраст целым числом")

# Сбор данных
while True:
    try:
        user_weight = float(input('Напиши свой вес в кг (например: 64):'))
        break
    except ValueError:
        print("Напиши свой вес числом с плавающей точкой, либо без нее")

while True:
    try:
        user_height = float(input('Напиши свой рост в м (например: 1.7):'))
        break
    except ValueError:
        print("Напиши свой рост числом с плавающей точкой, либо без нее")


def bmi(user_weight, user_height):
    """Рассчет Индекса массы тела"""
    """Функция будет возвращать либо целые числа либо дробные"""
    index = round(user_weight / (user_height ** 2), 1)
    if index % 1 == 0:
        return int(index)
    else:
        return index


def water_normal(user_weight):
    """Подсчет нормы воды"""
    """Функция будет возвращать либо целые числа либо дробные"""
    user_normal_water = (user_weight * WATER_PER_KG) / MILL_IN_LITER
    if user_normal_water % 1 == 0:
        return int(user_normal_water)
    else:
        return user_normal_water


def symbol(user_age):
    """Объявим функцию для вычисления"""
    """корректного отображения возраста в 'годах' или 'лет'"""
    if user_age < 10:
        if user_age in [1, 2, 3, 4]:
            return "г."
        else:
            return "л."
    elif 10 <= user_age < 20:
        return "л."
    elif user_age >= 20:
        if user_age % 10 in [1, 2, 3, 4]:
            return "г."
        else:
            return "л."


# Вывод красивого результата
print(
    f'Расчет для пользователья {user_name} '
    f'({user_age} '
    f'{symbol(user_age)})!'
       )
print(f'Твой Индекс Массы Тела: '
      f'{bmi(user_weight, user_height)}'
      )
print(f'Рекомендуемая норма воды: '
      f'{water_normal(user_weight)} л. в день'
      )
print("Расчет окончен. Будьте здоровы!")
