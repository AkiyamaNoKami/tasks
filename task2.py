def find_com_div(numbers):
    if not numbers:
        return []

    min_number = min(numbers)
    common_div = []

    for i in range(1, min_number + 1):
        if all(number % i == 0 for number in numbers):
            common_div.append(i)

    return common_div
