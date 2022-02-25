from random import randint


hit = randint(1, 3)
hit_points = [10, 5, 2]

print(f"Выстрел в {hit_points[hit-1]} очков")
