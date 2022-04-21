# a = 10
# b = 11
# print(a == b) #returning false because a is not equal to b
# print(a != b) #returns true because a not equal to b
# print(a < b)    #returns true because a is having 10 and b is having 11 which means a is less than 10
# print(a > b)    #returns false because a is less than b
# print(a <= b)   #returns true because satisfies less than statement even though it doesnt satisfy equal to statement
# print(a >= b)   #returns false because both condition statement not satisfied

# print(isinstance(10, (str, int, float, complex)))
# print(10)
a = 10
b = 20
if a * 2 == b: #its checking the condition if condition is true it enters the true block for further process
    print(a, b) #true block starts after ":" in a new line with a tabspace or atleast 4 normal space


if a + b == 25: #its does not enter the true block because condition is false
    print(a, b)

if a - b == 10: #here condition is false so doesnt enter true block
    print(a, b)
else:   #when if condition is false it enters to else if mentioned and else will be having false block
    print(a - b) #false block with some process

#true block and false block are inside some kind of code block and here its if else keywords which represents a kind of syntax
# if conditional statement:
#     process
# else:
#     process

#nested if
if a == b: #if condition true it enters true block
    print(a)
    if isinstance(a, int): #again another condition if true then it enters another true block
        print(a + b)
    # else: #if condition of 2nd true block is false its enters the else with false block inside the 1st if
    #     print(type(a))
# else: #if 1st if statement is false it enters else outside that if
#     print(b, type(b))

#in nested if the 1st true block when it returns false it doesnt enter the true block for performing other conditions
# print(help("keywords"))

# elif
a = 20
b = 10

# if a == b:
#     print(a)
# # else isinstance(a, int): #else doesnt take conditions
# elif isinstance(a, int): #elif is checked when if condition is not satisfied so elif will be having false block but with condition
#     print(a + b) #false block process
# else:
#     print(b, type(b))


# if a == b:
#     print(a)
#     if isinstance(a, int):
#         print(a + b)
# # else isinstance(a, int): #else doesnt take conditions
# elif a != b: #elif is checked when if condition is not satisfied so elif will be having false block but with condition
#     print(a + b) #false block process
#     if isinstance(b, int):
#         print(a - b)
# else:
#     print(b, type(b))


if 10 + 10 == 20 or 20 == 10 * 2 or 20 * 2 == 50 : #or is a keyword even if one condition becomes true it returns true
    print("20")

if 10 + 10 == 20 and 20 == 10 * 2 and 20 * 2 == 50: #and is a keyword even if one condition is false it returns false
    print("20")
else:
    print("not entered true block")

# or = 0 + 0 + 0+ 1 = 1
# and = 1 * 1 * 1 * 0 = 0

#palindrome
# s = "mom"
# s = "hello"
# s = "malayalam"
# if s[::-1] == s:
#     print("palindrome")
# else:
#     print("not palindrome")

#starts with s then first word else reverse string
# s = "she sells sea shells on the sea shore "
# s = "is she sells sea shells on the sea shore "
# if s.startswith("s"):
#     l = s.split()
#     print(l[0])
# else:
#     print(s[::-1])

# question 1
# check whether the given string is having alphabets only if yes print the string else reverse it
# s = "shesellsseashellsontheseashore"
# s = "she se1lls s@ea shells on the sea shore "
# if s.isalpha():
#     print("yes")
# else:
#     print(s[::-1])



#question 2
# check whether the given number is even or odd
# n = 111
# n = 1110
# if n %2 == 0:
#     print("even")
# else:
#     print("odd")

#question 3
#check if entered character is vowel or not
# c = "e"
# c = "u"
# c = "t"
# if c in "aeiouAEIOU":
#     print("it is vowel")
# else:
#     print("not a vowel")




#question 4
#check whether the given string starts with a vowel or not
# s = "a is apple"
# s = "hello world"
# if s[0] in "aeiouAEIOU":
#     print("starts with vowel")
# else:
#     print("not starting with vowel")



#question 5
#check whether a number is starting with even or not and also ending with even or not
# n = 12345667
# n = 84667965
# n = 1456
# if int(str(n)[0]) % 2 == 0:
#     print("even at start")
#     if int(str(n)[-1]) % 2 == 0:
#         print("even at end")
#     else:
#         print("odd at end")
# elif int(str(n)[-1]) % 2 == 0:
#     print("even at end")
#     print("odd at start")
# else:
#     print("odd at both position")

# if int(str(n)[0]) % 2 == 0 and int(str(n)[-1]) % 2 == 0:
#         print("even at starting and ending")
# else:
#     print(" starting and ending odd")



