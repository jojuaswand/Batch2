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

# #rindex
# s = "1a2b3c1a32b3c"
# # print(s[0 : 10])
# a = s.rindex("3") #from reverse we are searching for the 1st occurance
# a = s.rindex("3", 0, 10) #slicing to get second occurance of "3"
# a = s.rindex("3", 5)
# s = "123456789"
# a = s.rindex("9", 3) #ValueError: substring not found
# # a = s.rindex("10")
# # print(a)
#
# #rfind
# s = "1a2b3c1a32b3c"
# print(s[3: 10])
# a = s.rfind("3") #from reverse we are searching for the 1st occurance
# a = s.rfind("3", 3, 10) #slicing to get second occurance of "3"
# a = s.rfind("10")  #-1 if string does not exist
# print(a)

#replace is replacing the 1st occurance then replaces next and continues until the count
s = "superman"
a = s.replace("super", "bat") #its going to take string which is to replaced with new string
# print(s)
# print(a)
s = "hello"
a = s.replace("l", "t")
a = s.replace("l", "t", 1) #count is given inorder to replace the required number of strings
a = s[::-1].replace("l", "t", 1)
a = s.replace("l", "t", -1) #count is replaced with step value
# print(a[::-1])

#startswith
s = "hello world bye world"
a = s.startswith("h") #checking whether the given string is starting in the base string
a = s.startswith("h", 3)
a = s.startswith("l", 3, 10) #using index to slice and find
a = s.startswith("hello") #searching whether the group of characters are there at the start
a = s.startswith("helo")
# print(a)

#endswith
s = "hello world bye world"
a = s.endswith("d") #checking whether the given string is the end value for the base string
a = s.endswith("ld")
a = s.endswith(" world")
a = s.endswith("world", 0, 11)
a = s.endswith("world", 0, 10)
# print(a)

#split
s = "hello world bye world"
a = s.split() #splits string and returns a list having string as elements, this string is from base string
#spaces were removed
# a = s.split("") ValueError: empty separator
a = s.split(" ") #split() is same as split(" "), default value of split() is " "
s = "hello-bye-hello"
a = s.split() #because no spaces are there
a = s.split("-")
a = s.split("e")
a = s.split("-", 1) #we can give the number of times we require to split the string
a = s.split("hello")
# a = "hello"
# print(a)

#join

s = "-"
a = "hello"
# print(s.join(a)) #joins the string characters by using a separater as the base value
#
# print("".join(a))
#
# print(" ".join(a))
#
# print("e".join(a))

#strip
s = "helloh dworld"
# print(s.strip())
# print(s.strip("h")) #its checking if the given string is present on both ends then removes them
# print(s.strip("hd"))
# print(s.strip("held"))
# print("  hi  ".strip()) #by default the strip value will be spaces, so spaces will get removed from both ends
# print("$hi#".strip("$#"))
# print("$hi#".strip("$"))
# print("#$hi#".lstrip("$#"))  #its going to check or remove only from the left side or from the beginning
# s = "@#$HI#"
# print(s.strip("#$@")) #it is not based on the order
# print("$$#hi$$#".rstrip("$#")) #its going to from the right side or from the reverse
#



