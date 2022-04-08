# s = "hello WORLD"
# # print(dir(s))
# a = s.upper() #converting lowercase alphabets into uppercase only for alphabets
# print(a)
# b = a.lower() #converting uppercase alphabets to lowercase only for alphabets
# print(b)

#count
s = "she sells sea shells on the sea shore"
a = s.count("s") #counting the number of occurance for the given string inside the base string
# print(a)
b = s.count("sea")
# print(b)
c = s.count("i") #trying to count a string which does not exist so it gives in return 0
# print(c)
# d = s.count
s = '12345678901'
a = s.count("1", 1, 5) #we can use start index and end index and its optional
a = s.count("1", 5 , -1)
a = s.count("1", 5)
# print(a)
# a = s.count("1")  # we should give string a s value even though it is numeric
# print(a)
# i = 12345
# b = str(i).count("1")
# print(b)

#index()
s = "1a2b3c1a2b3c"
a = s.index("3",0,5) #the index number of the given string but only if it exists
# a = s.index("5")#ValueError: substring not found
a = s.index("3") #index() returns the index value of the string for the first occurance
a = s.index("3",5) #use start and end index to slice and find the next occurance
# print(a)

#find()
s = "1a2b3c1a2b3c"
a = s.find("3") #returns index value of the first occurance
a = s.find("5") #returns -1 if string not found and wont throw error
a = s.find("3",5) #using slicing we can get second occurance
# print(a)



