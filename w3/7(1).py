# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def find_33(a):
    for i in range(len(a)):
        if a[i] == 3 and a[i+1] == 3:
            return True
    return False


a= [int(x) for x in input().split()]
print(find_33(a))
