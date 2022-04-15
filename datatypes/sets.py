# s = {}
# print(s, type(s)) #it is not a empty set its considered as dictionary
# s1 = {1, 2, 3, 5, 4, 6}
# print(s1, type(s1))  #it is considered as set because we have assigned some values and it is shuffling or unordered
# s2 = set()
# print(s2, type(s2)) #constructor for set and also default value of set if set() is empty it is empty set
# s3 = set([1, 2, 3])
# print(s3, type(s3)) #constructing set data out of list and we are doing type casting

s = {1, 2, "hello", 3, "hi", "hi"}  #changes element position
# print(s) #removes duplicates but keeps one of them
# print(s[0]) #TypeError: 'set' object is not subscriptable so its considering whole set and not elements itself

#add()
# s.add("h") #adding new element to the set
# print(s)
# s.add("h")
# print(s) #duplicates are not allowed in set
# # s.add([11,12]) #TypeError: unhashable type: 'list'
# # s.add({11, 12})  #TypeError: unhashable type: 'set'
# s.add((11, 12))
# print(s)
# a = s.add("bye") # its is affecting original data and returns none value
# print(a) and returns none value
# print(s)

# in set we can have only individual data types, strings and tuples because they are having hash values

#clear()
# s = {1, 2, 3}
# # s.clear() #its removing all the elements from the set
# # print(s) #its returning empty set which is set()
# # s.clear(1) #it doesnt take in any value for any other purpose
# a = s.clear() #its affecting the original data
# print(a) #and its returning none
# print(s) #original value modified

#copy()
# s = {1, 2, "hi", 3}
# s1 = s
# print(s, id(s))
# print(s1, id(s1))
# s.clear()
#
# print(s, id(s))
# print(s1, id(s1))

s = {1, 2, "hi", 3}
s1 = s.copy() #we are having same elements as s but the set itself is changed
print(s, id(s))
print(s1, id(s1))
s.clear() #when we modify the original set this copied set is not affected
print(s, id(s))
print(s1, id(s1))
