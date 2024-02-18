#factorial func

def factorial(n):
    fact = 1
    if n < 0:
        raise ValueError("Please, input integer >= 0")
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            fact = fact * i
        print(fact)

def power_five(num):
    degree = 0
    while 5 ** degree <= num:
        if 5 ** degree == num:
            return True
        degree += 1

    return False

number = int(input("Введіть число: "))
result = power_five(number)

if result:
    print(f"{number} є степенем п'ятірки.")
else:
    print(f"{number} не є степенем п'ятірки.")