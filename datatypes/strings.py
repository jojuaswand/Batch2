
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


