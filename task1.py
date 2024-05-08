def computer(number):
    if number % 10 == 1 and number % 100 != 11:
        return f"{number} компьютер"
    elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
        return f"{number} компьютера"
    else:
        return f"{number} компьютеров"