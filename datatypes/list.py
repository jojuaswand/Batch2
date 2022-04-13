# l = [1, 1.2, 1+2j, True, "hi"] #list is created when elements are inside []
# print(l)
# l1 = [1,2,3,4,5,6,7] #it can contain homogenous and hetrogenous data
# print(l1)
# l = list()  #default value of list is []
# print(l)
# l = []
# print(l)
# l = list(["hi", "hello"]) #if u want to give multiple values it should be in a collection format
# print(l)
# # l = list(123456) TypeError: 'int' object is not iterable but it will take only collections
# # print(l)
# l = list("123456")
# print(l)
# l = list([1,2,3,4,5,6])
# print(l)
# l = [1,2,3,4,5,6]
# print(l)
# l = list(int("123456"))
# print(l)

l = [1, 2, 3]
# print(l)
# print(len(l))
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3]) IndexError: list index out of range

l = [1,2,3,4,5,6]
# print(l[:3])
# print(l[3:])
# print(l[::-1]) #list in reverse and slicing
# l[0] = 7  #replacing list element using index
# print(l)
# print(dir(l))
#append
l.append(7) #adding new elements at the end of list
l.append("12") #it supports only one element of any type
# print(l)


# s = "hello"
# s[0] = "t" cannot
# print(s)
# s ="hello"
# a = s.replace("h", "t") #creates new string
# print(a)
# print(s)

#memory adress
# l = [1, 1.2, 1+2j, "hello", 45, "lion"]
# print(id(l))
# print(id(l[0]))   #each element has its own address
# print(id(l[1]))
# print(id(l[2]))
# print(id(l[3]))  #collections will have new address for each element inside it
# print(id(l[4]))
# print(id(l[5]))  #duplicate elements inside different collections can have same address
# print(l[3][2])
# print(l[5][0])
# print(id(l[3][2]))
# print(id(l[5][0]))

#clear()

# l = [1, 2, 3]
# print(l)
# a = l.clear() #removing elements from original list and returns none, it affects the original list
# print(a)
# print(l)

#count()
# l = [1, 2, 1, 2, 3, 4, 5]
# print(l.count(1)) #counting the number of occurance of the elements
# print(l.count(3)) #its taking base value as the original list and searching for an element
# print(l.count(10))  #it wont throw error if element does not exist , it will give 0

# l = ["hi", "hello", "hi", "he", "llo"]
# print(l.count("h"))
# print(l.count("hi"))

#extend
# l = ["hi", "hello", "hi", "he", "llo"]
# l.extend("1") #same as append
# print(l)
# l.extend("2")
# print(l)
# l.extend([1, 2]) #it gives elements from the collection and extends the list
# print(l)
# l.append([1, 2]) #it takes the value itself without change and adds to the list
# print(l)
# l.extend([3, "hi"]) #values given should be in the form of collection
# print(l)
# l.extend(["12", 12]) #inside collection we can give any type of data
# print(l)
# l.extend("hello")
# print(l)
#
# #[1, 2, 3, 1 ,1, 1 , 5] wap to count 1 from the list and append the count of 1 to the original list
# l = [1,1,1,1,2, 3 ,4 ,5 ,6]
# l.append(l.count(1))
# print(l)

#index()
l = [1, 1.2, 1+2j, "hello", "oh"]
# print(l.index(1+2j))
# # print(l.index("h")) Value error "h" element doesnt exist
# print(l.index("hello"))
# print(l[3].index("h"))

# #isinstance
# print(isinstance) #inbuilt function
# print(isinstance(l, list)) #to check if  a value belongs to a certain data type
# print(isinstance(l[3], list))
# print(isinstance(l[3], (list, str))) #we can mention multiple data types and even if 1 of them is true it returns true
# print(isinstance(l[0], (int, float, complex, str, list)))

#insert

l = [1, 2, 3, 4, 5, 6]
# print(l)
# a = l.insert(0, 5) #inserting a new value to specified index
# print(a) #it returns none
# print(l) #it modifies original value
# l.insert(3, "middle")
# print(l)
# l.insert(0, l)
# print(l)
# print(l[0])
# print(l[0][0])
# [l, 5, 1,2 ,"middle", 3,4,5,6]   [l, 5, 1,2 ,"middle", 3,4,5,6]
#  0   1  2 3   4       5 6 7 8     0   1  2 3   4       5 6 7 8

#pop
# l = [1, 2, 3, 4, 5, 6]
# print(l.pop()) #pop removes a element from original list and it returns the popped item
# print(l.pop(0)) #we can specify the index to pop, but by default it pops the last element
# print(l)
# l = ["hi", 1 , 2, 3]
# # print(l[0].pop()) #AttributeError: 'str' object has no attribute 'pop'
# # print(l.pop("h"))#only accepts index value
# print(l)
# l = [["hi"], 1]
# print(l[0].pop(), l)

#remove

# l = [1, 2, 3, "hi", 4, 5, 6]
# print(l.remove(1), l) #remove removes the specified value from original list and returns none and affects original list
# l.remove("hi")
# print(l)
# l.remove("hi") ValueError: list.remove(x): x not in list if element not in list
# print(l)

#reverse
# l = [1,2,5,3,4]
# print(l[::-1])
# print(l.reverse()) #it reverses the original list and returns none
# print(l) #it wont change the values it just doese reverse
# l.reverse()
# # l.reverse(0) #it takes no value

#sort
l = [10, 5, 9, 4, 7, 2, 8, 1, 6, 3]
# print(l)
# print(l.sort()) #sort is sorting the list in ascending order by default and returns none and it affects original value
# print(l)
# l.sort(reverse= True) #sorted but in descending order because we have mentioned reverse is true
#sorts the list and then reverses it
# print(l)
l = ["hi", "apple", "cat", "zebra"]
# print(l)
# l.sort() #for strings it is based on the 1st character by default and sorts bsed on alphabetical order
# l.sort(reverse= True) #by default reverse will be false
# l.sort(reverse= False, key= len) #key takes function names and based on that it sorts
# l.sort(key=len) #key takes function names not function call
# l.sort(reverse=True , key=len)
# print(l)
# l = ["2hi", "1apple", "4cat", "3zebra"]
# l.sort()
# print(l)

#copy

# l = [1, 2, 4, 3]
# l1 = l #l1 is the same as l
# print(l)
# print(id(l))
# print(l1)
# print(id(l1))
# l.sort()
# print(l)  #if changes are made to l
# print(l1) #it affects l1 too

# l = [1, 2, 4, 3]
# l1 = l.copy() #l1 is copying the value of l
# print(l)
# print(id(l))
# print(l1)
# print(id(l1)) #l and l1 have different addresses even when they have same value
# print(l[0], id(l[0]))
# print(l1[0], id(l1[0])) #address of list remains different but the elements will be having same object address
# l.sort()
# print(l) #changes made to l
# print(l1) #are not affecting l1

#
# a = "hello"
# b = a[::-1]
# print(a, id(a))
# print(b, id(b))
# print(a[0], id(a[0]))
# print(b[-1], id(b[-1]))

#shallow copy we are copying the original list but not the elements, the elements will have same address
# l = [1, 2, 4, 3]
# l1 = l.copy()
# print(l, id(l))
# print(l1, id(l1))
# print(l[0], id(l[0]))
# print(l1[0], id(l[0]))
# l[0] = 5
# print(l, id(l))
# print(l1, id(l1))
# print(l[0], id(l[0]))
# print(l1[0], id(l[0]))

#deepcopy
# from copy import deepcopy   #copy module from this module we import deepcopy function
# l = [1, 2, 4, 3]
# l1 = deepcopy(l)
# # print(l, id(l))
# # print(l1, id(l1))
# # print(l[0], id(l[0]))
# # print(l1[0], id(l[0]))
# l[0] = 5
# # print(l, id(l)) #the list address are different
# # print(l1, id(l1))
# print(l[0], id(l[0]))
# print(l1[0], id(l1[0]))
# print(l[1], id(l[1]))
# print(l1[1], id(l1[1]))







