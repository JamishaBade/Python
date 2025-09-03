start = int(input("enter start value="))
stop = int(input("enter stop value="))

skip = int(input("number you want to skip"))

for i in range(start, stop):
    if i == skip:
        continue
    print(i)
