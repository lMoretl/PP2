my_list=[67,34,345,345,345,345,34,5,67,6789]
with open("text.txt","a") as file:
    file.write("\n[")
    for i in my_list:
        file.write(str(i))
        if my_list[len(my_list)-1]!=i:
            file.write(",")
    file.write("]")