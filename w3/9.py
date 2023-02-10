#Write a function that computes the volume of a sphere given its radius
def volume(r):
    return 4/3*3.14*(r**3)

r = float(input())
print(volume(r))