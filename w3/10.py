#Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set

def dup(a):
    x = []
    for i in a:
        if i not in x:
            x.append(i)
    return x
a = [int(x) for x in input().split()]
print(dup(a))

