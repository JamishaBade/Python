age = int(input("enter you age ="))
if age >= 18 and age < 101:
    print("you are an adult")

elif age >= 101:
    print("man u too old")
else:
    print("you are a minor")


"""
if
elif
else
"""


num_1 = float(input("enter number 1 ="))
num_2 = float(input("enter number 2 ="))

choice = input("Enter you choice of symbol (+,-,/,*)")

if choice == "+":
    print(num_1 + num_2)
elif choice == "-":
    print(num_1 - num_2)
elif choice == "*":
    print(num_1 * num_2)
else:
    print(num_1 / num_2)

choice = input("")
