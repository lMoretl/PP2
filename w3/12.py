#Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
def histogram(a):
    for i in a:
        print('*'*i)
        end=''
a = [int(x) for x in input().split()]
histogram(a)