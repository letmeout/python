def Factorial (number):
    if (number < 2):
        return number
    else:
        return number * Factorial(number - 1)


print (Factorial(100))

def Sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(Sum([1, 2, 3, 4]))