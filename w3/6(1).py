#Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
def reversing(x):
    x.reverse()
        
s = str(input())
x = s.split()
reversing(x)
r = ' '.join(str(x) for x in x)
print(r)
