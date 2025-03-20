print("welcome to the Tip Calculator")
amount = float(input("What was the total bill ? "))
percentage = int(
    input("What percentage tip would you give ? 10, 12, or 15 ? "))
number = int(input("How many people to split the bill with "))
tip = ((percentage/100)*amount)
total = (amount+tip)
each = round((total/number), 2)
print("Each person should pay: ", each)
# its is to be noted above that using round in some cased do not give the 2 decimal place in the end but only one decimal
# therefore we use the format method
print("Each person should pay {:.2f}".format(each))
print("Each person should pay {help:.2f}".format(help=each))
