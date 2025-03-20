print("Welcome to the Love Calculator !")

name1 = input("What is your name ? \n ")
name2 = input("What is their name ? \n")
name = (name1+name2).lower()

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

first = str(t+r+u+e)

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
second = str(l+o+v+e)

if int(first+second) < 10 or int(first+second) > 90:
    print(
        f"Your love score is {first+second+" "+"%"}, you go together like coke and mentos.")
elif int(first+second) > 40 and int(first+second) < 50:
    print(
        f"Your love score is {first+second+" "+"%"}, you are alright together")
else:
    print(f"Your love score is {first+second+" "+"%"}")
