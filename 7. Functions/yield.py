def squares(n):
    for i in range(n):
        yield i**3  # this is like return + continue


for num in squares(5):
    print(num)
