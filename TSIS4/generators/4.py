def squares(a,b):
    for i in range(a,b+1):
        yield i**2
        i+=1
for i in squares(5,9):
    print(i)