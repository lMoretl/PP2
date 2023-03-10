import os
import shutil
pantherfaust="C:/Users/User/Desktop/python/text.txt"
if os.path.exists(pantherfaust):
    if os.access(pantherfaust,os.R_OK|os.W_OK):
        os.remove(pantherfaust)
    else:
        print("access denied")
else:
    print("not exists")