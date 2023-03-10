import os
div_list=[]
file_list=[]
path_list=[]
for path,dirs,files in os.walk(os.getcwd()):
    file_list.append(files)
    div_list.append(dirs)
print(div_list)
print(file_list)