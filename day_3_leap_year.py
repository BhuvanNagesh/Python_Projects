print("Welcome to Leap Year Checker.")
year = int(input("Enter the year to be checked: "))

d1 = year % 4 == 0
d2 = year % 400 == 0
d3 = year % 100 == 0  # Corrected (checking if divisible by 100)

if (d1 and not d3) or d2:  # Corrected condition
    print("Leap Year")
else:
    print("Not a Leap Year")

# print("Welcome to Leap Year Checker.")
# year = int(input("Enter the year to be checked: "))

# d1 = year % 4 == 0
# d2 = year % 400 == 0
# d3 = year % 100 == 0  # Corrected (checking if divisible by 100)

# if d1 :
#     if d3 :
#         if d2:
#             print("Leap year")
#         else:
#             print(" Not Leap year")
#     else:
#         print(" Leap year")
# else:
#     print(" Not Leap year"
