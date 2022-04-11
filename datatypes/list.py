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
l = ["hi", "hello", "hi", "he", "llo"]
l.extend("1") #same as append
print(l)
l.extend("2")
print(l)
l.extend([1, 2]) #it gives elements from the collection and extends the list
print(l)
l.append([1, 2]) #it takes the value itself without change and adds to the list
print(l)
l.extend([3, "hi"]) #values given should be in the form of collection
print(l)
l.extend(["12", 12]) #inside collection we can give any type of data
print(l)
l.extend("hello")
print(l)



