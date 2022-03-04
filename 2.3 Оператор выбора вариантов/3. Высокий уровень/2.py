# Написать программу, которая в зависимости от характера ветра выдает 
# сообщение о его скорости от 1до 4 м/с - слабый (1); от 5-10 м/c -
# умеренный (2); от 9-18 м/c - сильный (3); больше 19 м/c - ураганный (4).


def get_wind_speed_type(level: int):
    if 1 <= level <= 4:
        return "cлабый"
    elif 5 <= level <= 10:
        return "умеренный"
    elif 9 <= level <= 18:
        return "сильный"
    elif level >= 19:
        return "ураганный"
    else:
        return "норм"


print("Сегодня ветер",  get_wind_speed_type(8))
