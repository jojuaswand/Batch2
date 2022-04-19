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

# s = {1, 2, "hi", 3}
# s1 = s.copy() #we are having same elements as s but the set itself is changed
# print(s, id(s))
# print(s1, id(s1))
# s.clear() #when we modify the original set this copied set is not affected
# print(s, id(s))
# print(s1, id(s1))

#difference
s = {1, 2, 3}
s1 = {1, 2, 3, 4}
s2 = {1, 2, 3, 4, 5, 6}
x = s.difference(s1) #base set is compared with another set and it checks if base set elements are different from another set
a = s1.difference(s)
y = s2.difference(s, s1)
# print(s2 - s1 - s) #subtracted value
# print(s - s1) #subtraction is similar to difference
# print(x)
# print(a)
# print(y)
# print(s)  #difference is not affecting original set
# print(s1)
# print(s2)

#difference_update
# s = {1, 2, 3}
# s1 = {1, 2, 3, 4}
# s2 = {1, 2, 3, 4, 5, 6}
# # x = s.difference_update(s1) #base set is compared with another set
# # and it checks if base set elements are different from another set
# #it updates the base set with the difference value
# # a = s1.difference_update(s) #returns none but updates base set
# y = s2.difference_update(s, s1) #it doesnt update any other set other than base set
# # print(x)
# # print(a)
# print(y)
# print(s)
# print(s1)
# print(s2)

#discard()
# s = {1, 2, 3, "hi"}
# print(s)
# print(s.discard(1)) #removes the specified value from the set and it affects the original set
# # print(s.discard("hi", 2)) #only takes one value
# # print(s.discard()) #minimum one value we should assign
# print(s.discard("hello")) #returns nothing if value doesnt exist and its not affecting original set
# print(s)

#remove
# s = {1, 2, 3, "hi"}
# print(s)
# print(s.remove(1)) #removes the specified value from the set and its affecting original set
# print(s.remove("hello")) #KeyError: 'hello' remove gives error and discard gives none
# print(s)

#pop
# s = {1, 2, 3, "hi"}
# print(s)
# print(s.pop()) #by default it removes random element from set and returns the value which we removed
# print(s) #and it affects the original set
# a = s.pop()
# b = s.pop()
# c = s.pop()
# print(a, b, c)
# d = s.pop() #KeyError: 'pop from an empty set' #no element exists in empty set
# print(s.pop(0)) #TypeError: set.pop() takes no arguments (1 given) #pop doesnt take any values for set
# print(s)

#union
s = {1, 2, 3, "hi"}
s1 = {4, 5, 6, "hello"}
# print(s.union(s1)) #combines all the elements and creates a new set, union can combine n number of sets
# print(s) #it doesnt affect the base set or the another set in use
# print(s1)
#update
# print(s.update(s1)) #returns none but updates the base value with union value
# print(s) #base set affected and is now having union of base set and another set
# print(s1)

#intersection
# s = {1, 2, 3, "hi"}
# s1 = {4, 5, 6, "hello"}
# s2 = {1, 4}
# # print(s.intersection(s1)) #intersection checks for common value
# # print(s.intersection(s2)) #and it returns the common value
# # print(s1.intersection(s2))
# # print(s) #it doesnt affect original value
# # print(s1) #or the another set
#
# print(s.intersection_update(s1)) #it checks for common value
# print(s) #updates the base set with common value and it returns none
# print(s1)

#isdisjoint()
# s = {1, 2, 4, "hi"}
# s1 = {4, 3, 5, "hello"}
# s2 = {"bye", 5}
# print(s.intersection(s1))
# #disjoint is just checking if there is common element or not
# print(s.isdisjoint(s1)) #if there is a common element its going to return False
# print(s.isdisjoint(s2)) #if there are no common element its going to return True
# print(s) #its not affecting the original set
# print(s1)

#issubset()
# s = {1, 2, 3}
# s2 = {7}
# s1 = {1, 2, 3, 4, 5, 6}
# print(s.issubset(s1)) #checking if base set exists in another set
# print(s2.issubset(s1)) #if the base set is not there it gives false
# print(s)
# print(s1)

#issuperset()
# s = {1}
# s1 = {1, 2, 3}
# s2 = {4, 5, 6, 1, 2}
# print(s1.issuperset(s)) #checking if base set contains other set
# print(s2.issuperset(s1)) #if base doesnt contain other set it gives false
# #even if the base set doesnt have one value from other set it is not considered as superset
# print(s)
# print(s1)

#symmetric_difference()
# s = {1, "hi", 10}
# s1 = {10, "bye", 20}
#
# # print(s.difference(s1)) #it gives difference between two sets and returns values from base set
# # print(s.symmetric_difference(s1)) #it removes difference between base set and other set
# # # and returns the different values from both the sets
# # print(s) #it doesnt affect original sets
# # print(s1)
# #symmetric_difference_update()
# print(s.symmetric_difference_update(s1)) #does symmetric_difference and returns none but updates value to base set
# print(s) #it affects original base set and not the other one
# print(s1)
#
#
# s = {[1,2,3], 1}
# print(s)

