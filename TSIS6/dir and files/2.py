import os
path=input()
with open(path,'w') as f:
   print( f.writable())
if os.path.exists(path):
    print("this path exists")
else:
    print("doesnt exist")
try:
    f=open(path)
    print("openable")
    try:
        g=f.read()
        print("readable")
    except:
        print("not readable")
    try:
        h=open(path,'w')
        h.write(" ")
        print("writable")
    except:
        print("not writable")
except:
    print("not openable")
finally:
    f.close()