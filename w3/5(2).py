#Write a function that accepts string from user and print all permutations of that string
from itertools import permutations
def per(s):
    p = [''.join(p) for p in permutations(s)]
    return p
s = str(input())

print(per(s))