def calculate(number):
    number = int(number)
    count = 0
    while number > 0:
        number = number // 10
        count += 1
        number = number + (number % (10 ** count))