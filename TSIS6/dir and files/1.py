import os
files=[]
dirs=[]
#suppose that this is not fast
for path in os.listdir(os.getcwd()):
    if path==".git":
        continue
    bigsmoke=os.path.join(os.getcwd(),path)
    if os.path.isfile(bigsmoke):
        files.append(path)
    else:
        dirs.append(path)
        for new_path in os.listdir(bigsmoke):
            smallsmoke=os.path.join(bigsmoke,new_path)
            if os.path.isfile(smallsmoke):
                files.append(new_path)
            else:
                dirs.append(new_path)
                for newest_path in os.listdir(smallsmoke):
                    tinysmoke=os.path.join(smallsmoke,newest_path)
                    if os.path.isfile(tinysmoke):
                       files.append(newest_path)
                    else:
                       dirs.append(newest_path)
print(files,dirs)