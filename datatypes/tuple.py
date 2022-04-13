# t = 1,2 #if we mention any value with comma without boundaries for a variable its considered as tuple
# print(t)
# print(type(t))

# t = "hi","bye"
# print(t)
# print(type(t))
#
# t = ["hi","bye"], ["hi","bye"]
# print(t)
# print(type(t))

# t = ["hi","bye"], ["hi","bye"], 1, "hi", 1+2j   #by default python consider comma separated values without boundaries as tuple
# print(t)
# print(type(t)) #tuple can have multiple types of data

# t = (1, 2.2, "hi", 1+2j, [4, 5], (6,7))
# print(t, type(t))


# t = tuple([1, 2.2, "hi", 1+2j, [4, 5], (6,7)]) #we are also typecasting
# print(t, type(t))

# t = tuple(1) #we cannot give individual data only accepts iterable
# print(t, type(t))

# t = (1)
# print(t, type(t)) # cannot consider single element inside boundaries () as tuple
# t = (1,)
# print(t, type(t)) #inorder to be considered or to create single elemnt tuple should mention ,comma after the element

# t = tuple()
# print(t, type(t)) #default value of tuple is ()

# t = (1, 2, 3)
# print(t)
# # t[0] = 5 #TypeError: 'tuple' object does not support item assignment
# # print(t) #tuples are not changeable
# print(t[0], id(t[0]))
# print(t[1], id(t[1]))
# print(t[1:])

t = (1, 2, 3, 4.4, 5+5j, "hi", "hello")
# print(dir(t))
# print(len(t))

#index
# print(t.index("hi"))
# # print(t.index("hi1")) #ValueError: tuple.index(x): x not in tuple if value doesnt exist
# print(str(t)) #typecasting to use find inoreder to check every value without error
# print(str(t).find("hi"))
# print(str(t).find("i")) #tuple doesnt have any method called find but we can typecaste to string to use it
# print(str(t).find("2,"))
# print(str(t).find("',"))

# t = (1, 2, 3, 4.4, 5+5j, "hi", "hello")
# print(t[t.index("hi")][0])
# print(t[5][0])

#count
# t = (1, 2, 3, 4.4, 5+5j, "hi", "hello")
# print(t.count("hi")) #counting the number of times a element is in the tuple
# t = (1, 2, 3, 1, 2, 1, 'hi', "hi")
# print(t.count(1))
# print(t.count("hi"))

