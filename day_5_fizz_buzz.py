for numbers in range(1, 101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FIZZBUZZ")
    elif numbers % 5 == 0:
        print("Buzz")
    elif numbers % 3 == 0:
        print("FIZZ")
    else:
        print(numbers)
