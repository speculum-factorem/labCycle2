A = float(input("Введите длину отрезка A: "))
B = float(input("Введите длину отрезка B: "))

if A < 0 or B < 0:

    print("Длины отрезков не могут быть отрицательными")

else:

    total_length = 0

    while total_length + B <= A:
        total_length += B

    remaining_length = A - total_length

    print("Длина незанятой части отрезка A:", remaining_length)