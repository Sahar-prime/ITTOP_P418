while True:
    # Числа
    num_1 = input("Введите первое число:  ")
    if num_1.isdigit():
        num_1 = int(num_1)
    else:
        print("Введите число!!!")
        continue
    num_2 = input("Введите второе число:  ")
    if num_2.isdigit():
        num_2 = int(num_2)
    else:
        print("Введите число!!!")
        continue
    if num_1 == 0:
        print("Введите другое число!")
        continue
    elif num_2 == 0:
        print("Введите другое число!")
        continue
    # Операции
    a = input("Выберите операцию:\n")
    if a == "*":
        num_3 = num_1 * num_2
        print("Ответ:", num_3)
    elif a == ":":
        num_3 = num_1 / num_2
        print("Ответ:", num_3)
    elif a == "+":
        num_3 = num_1 + num_2
        print("Ответ:", num_3)
    elif a == "-":
        num_3 = num_1 - num_2
        print("Ответ:", num_3)
    else:
        print("Вводите элементарные операции.\nНапример: +, -, *, :")
        continue
