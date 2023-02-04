
#list- is a collection which is ordered and changeable. Allows duplicate members.
'''#1 example
thislist=["apple","banana","cherry"]
print(thislist)
'''

'''#2 example
thislist=["apple","banana",'cherry',"apple","cherry"]
print(thislist)
'''

'''#3 example
thislist=["apple","banana","cherry"]
print(len(thislist))
'''

'''#4 example
list1=["apple","banana","cherry"]
list2=[1,5,9,8,7]
list3=[True,False,False]
list4=['apple',1,3,'banana',True]
print(list1)
print(list2)
print(list3)
print(list4)
print(type(list4))
'''

'''#7 example
thislist=list(("apple","banana","cherry"))
print(thislist)
'''



#list methods:

'''#1.append()-Adds an element at the end of the list:
l=input()
list1=['apple','banana','cherry']
list2=[1,2,3,4]
list1.append(l)
list1.append(list2)
print(list1)
'''

'''#2.clear()-Removes all the elements from the list:
list=["apple","banana","cherry"]
list.clear()
print(list) #print empty list
'''

'''#3.copy()-Returns a copy of the list:
list=["apple","banana","cherry"]
x=list.copy()
print(x)
'''

'''#4.count()-Returns the number of elements with the specified value:
list=["apple","banana","apple","cherry"]
x=list.count("apple")
print(x)
'''

'''#5.extend()-Add the elements of a list (or any iterable), to the end of the current list:
list1=["apple","banana","cherry"]
list2=["orange","waremelon"]
list1.extend(list2)
print(list1)
'''

'''#6.index()-Returns the index of the first element with the specified value:
list=["apple","banana","cherry"]
x=list.index("apple")
print(x)
'''

'''#7.insert()-Adds an element at the specified position:
list=["apple","banana","cherry"]
list.insert(2, "orange")
print(list)
'''

'''#8.pop()-Removes the element at the specified position:
list=['apple','banana','cherry']
list.pop(1)
print(list)
'''

'''#9.remove()-Removes the first item with the specified value:
list=["apple","banana","cherry"]
list.remove("apple")
print(list)
'''

'''#10.reverse()-Reverses the order of the list
list=["apple","cherry","banana"]
list.reverse()
print(list)
'''

'''#11.sort()-Sorts the list:
list=["cherry","apple","banana"]
list.sort()
print(list)
'''