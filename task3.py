M = 80
m1 = 400
g = 9.81

m2_values = range(100, 301, 20)

for m2 in m2_values:
    a = ((m2 - m1) / (m1 + m2 + M / 2)) * g
    print(f"Для m2 = {m2} кг: Ускорение a = {a:.2f} м/с²")