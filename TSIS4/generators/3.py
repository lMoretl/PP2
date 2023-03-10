def divis(n):
    iterator=0
    while iterator<n+1:
        if (iterator%3==0) or (iterator%4==0):
            yield iterator
            iterator+=1
            print(end=',')
        else:
            yield ''
            iterator+=1
for i in divis(16):
    print(i,end='')