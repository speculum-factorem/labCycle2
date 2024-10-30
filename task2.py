A = float(input("Введите длину отрезка A: "))
B = float(input("Введите длину отрезка B: "))

total_length = 0

while total_length + B <= A:
    total_length += B

remaining_length = A - total_length

print("Длина незанятой части отрезка A:", remaining_length)