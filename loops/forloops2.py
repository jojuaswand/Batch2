s = "hello"
# for i in s:
#     if i in "aeiouAEIOU":
#         print(i, "vowel")
#     else:
#         print(i, "not vowel")

vowels = []
not_vowels = []
# for i in s:
#     if i in "aeiouAEIOU":
#         vowels.append((i, "vowels"))
#     else:
#         not_vowels.append((i, "not vowels"))
#
# print(vowels, not_vowels)

# for i in s:
#     if i in "aeiouAEIOU":
#         vowels.append((i, "vowels", s.index(i)))
#     else:
#         not_vowels.append((i, "not vowels", s.index(i)))
#
# print(vowels, not_vowels)


# for i in s:
#     if i in "aeiouAEIOU":
#         a = s.index(i)
#         vowels.append((f"position of {i} is {a} and {i} is a vowel"))
#     else:
#         b = s.index(i)
#         not_vowels.append((f"position of {i} is {b} and {i} is not a vowel"))
#
# print(vowels, not_vowels)

# l = [(1,1), (2,2), (3,3)]
# for i in l:
#     print(i)
#     for j in i:
#         print(j)
#

#question 1
# print("python is easy") 10 times
# print(range) #range is a class
# print(range("a","z")) #range is having only integer as parameter
# print(range(-1, 10))
# print(list(range(-1,10))) #range is returning integers starting from -1 to 9
# print(list(range(10))) #range is returning integers starting from 0 till 9, but we have mentioned only 10 as parameter
#range by default starts at 0  and moves towards the end value and returns until the end value mentioned
#if given with 1 arguement it is considered as end value
#if given with 2 arguements 1st one will be start and 2nd will be end
#since range is a class it returns class object and we have to typecast or iterate through it to get the values inside class object
# count = 0
# for i in range(10):
#     count += 1
#     print(count, "python is easy")



#question 2
#iterate through a string using range
s = "hello world"
l = []
for i in range(len(s)):
    # print(s[i])
    l.append(s[i])
    # print(l)
# print(l)


#question 3
#print alternate characters of string
s = "hello world Bye world"
l = []
for i in range(0, len(s), 2):
    # print(s[i])
    l.append(s[i])

# print(l)

#question 4
l= [1, 2, 3, 4, 5, 6]
# if it is odd power it else multiply it with 10
# for i in l:
#     if i %2 != 0:
#         print(i ** 2)
#     else:
#         print(i * 10)
#





#question 5
s = "hhhhelllo worldd bye thanks"
# count the number of character occurance and insert into a dictionary with character and its count
d = {}
for i in s:
    d[i] = s.count(i)
print(d)

