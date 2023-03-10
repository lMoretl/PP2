import string
def islowere(a):
    if a.islower():
        return True
    else:
        return False
def isuppere(a):
    if a.isupper():
        return True
    else:
        return False
something=input()
lowers=len(list(filter(islowere,something)))
uppers=len(list(filter(isuppere,something)))
print(lowers,uppers,sep=" ")