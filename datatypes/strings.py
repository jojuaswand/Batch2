
hello = "hello" #for getting oneline output
a = 'hi' #for getting oneline output
b = """hello bye 
    bye
    b"""    #for getting multiplelines
c = '''hello bye
    bye
    b'''

# print(hello)
# print(a)
# print(b)

d = str()   #empty string "" it is the default string
# print(d)
# print("hello", "", "bye")

s = str(123) #converting integer into string
# print(type(123))
s = str(1.23) #converting float into string
# print(type(1.23))
s = str(1+2j) #converting complex into string
# print(type(1+2j))
# s = str("bye")
# print(s)
# print(type(s))

gandhi = "gandhi1234@hadoob%4$[]()" #string can have alphabets, numbers, special symbols and spaces ,all are characters
# print(gandhi)
s = str("bye 1 + 2 j")
# print(s)
x = 1
# print(len(x)) #TypeError: object of type 'int' has no len()
x = str(x)
# print(len(x))
#raw string it will assign r or R before the string itself its purpose is to stop escape characters
# print("hello\n")
# print(r"hello\n")
# print("hello\\n")
# print(r"hello\\n")
# print(r"hello\\\n")
# print("hel\lo \wor\ld")
# print(r"hi \tha\nk you")

# print("\") #backslashes cannot be in odd number
# print(r"\") #either as normal string or raw string
# print("\n") #it should have a literal after or it should be of even number
# print("\\")

# print(r"hello \@")


# '',"",'''''',"""""", str()
a = 'hello "hello" '  #the same boundaries cannot be used inside a string
# print(a)
a = "hello"
# print(len(a)) #1-5 for hello
#index
index = len(a) - 1
# print(index) #0 - 4 for hello forwards
# 1  2  3  4  5 - length
# 0  1  2  3  4 - forward index
# -5 -4 -3 -2 -1- backward index
a = "hello"
# print(a[0]) #h using forward index
# print(a[-5]) #h using backward index because length is 5 and we use negative value to get index in backwards
# print(a[3]) #2nd l
# print(a[2]) #1st l
#slicing
# print(a[0], a[1], a[2]) #h,e,l taking each of the characters
# print(a[0:3]) #slicing start value : end value (required value + 1) because it is until end value and it wont consider the end value itself

s = "hello world"
# print(len(s))
# print(s[0:5]) #slicing will be using index values
# print(s[-1 : -6 : 1]) #step value by default is 1 meaning its moving forwards
# print(s[-1 : -6 : -1]) #step value here is -1 which represents moving forwards
# print(s[-5 : ])
# print(s[:5])
# print(s[5:])
# print(s[:])  #index not given because it will consider empty values at the start and at the end
# print(s[::-1])

# s = "sea shells on the sea shore"
# print(s[:3], s[4:10], s[-5 : ], s[-9 : -6])
# print(s[:10], s[-9: ])
# print(s[::-1]) #reversing a string using slicing

s = "she sells sea shells on the sea shore"
# print(s[14:24])
# print(s[:3], s[-5 :])

#replacing using index and replace method

#memory allocations
s = "hello"
# print(id(s))
# print(id(s[0]))
# print(id(s[1]))
# print(id(s[2]))
# print(id(s[3]))
# print(id(s[4]))

