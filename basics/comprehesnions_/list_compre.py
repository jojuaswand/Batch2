
s = "hello world"
# print(list(s))
# l = list(s)
# print(l)
# l = []
# for i in s:
#     if i not in " ":
#         l.append(i)
#         # print(l)
# print(l)
# l = [i for i in s]
# l = [i for i in s if i not in " "] #comprehension shortens the codeblock
# print(l)
# list comprehension
# list = [return value for loop]
# list = [return if value for loop if condition]
# list = [return value (of if) if condition else return value(of else) for loop]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l1 = []
# for i in l:
#     if i % 2 == 0:
#         l1.append(i ** 2)
#     else:
#         l1.append(i * 2)
#
# l1 = [i**2 for i in l if i % 2 == 0]
# l1 = [i**2 for i in l if i % 2 == 0 else i * 2] syntax error
# l1 = [i**2 if i % 2 == 0 else i * 2 for i in l]
# print(l1)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = []
# for i in range(len(l)):
#     if l[i] % 2 == 0:
#         l1.append((i, l[i]))
# for i in enumerate(l):
#     if i[1] % 2 == 0:
#         l1.append(i)
# l1 = [i for i in enumerate(l) if i[1] % 2 == 0]
# print(l1)
# print(enumerate) #enumerate is a class
# print(enumerate(l)) #class object returned
#class objects either should be typecasted or should be iterated
#enumerate will have a tuple of index with the value

# l = enumerate(l)
# l2 = list(enumerate(l)) #it returns index value along with values in the form of tuples
# print(l2)

l = ["hello", "hi", "malayalam", "mom", "elephants", "item", "good"]
l1 = []
# for i in l:
#     if len(i) % 2 == 0:
#         l1.append(i)
#     else:
#         l1.append(i[:: -1])
# l1 = [i if len(i) % 2 == 0 else i[::-1] for i in l]
# l1 = [i[::-1] if len(i) % 2 == 1 else i for i in l]
# print(l1)


# question 1
# check even or odd in the range of 1 - 50 if it is even multiply by two or else power it and store these inside a new list
leven = []
lodd = []
# for i in range(1, 51):
#     if i % 2 == 0:
#         leven.append(i)
#     else:
#         lodd.append(i)
# leven = [i for i in range(1, 51) if i % 2 == 0]
# lodd = [i for i in range(1, 51) if i % 2 == 1]
# print(leven)
# print(lodd)


# question 2
l = ["python", "hello", "people", 1, "hi", "person", 2, "last", "personality"]
# if the string starts with p append it to a new list
l1 = []
for i in l:
    if isinstance(i, str):
        if i[0] in "pP":
            l1.append(i)
# print(l1)
c = [i for i in l if isinstance(i, str) if i[0] in "pP"]
print(c)

# question 3
l = ["python", "hello", "people", 1, "hi", "person", 2, "last", "personality"]
# in a new list append the elements with their index values
l1 = []
for i in enumerate(l):
    l1.append(i)

l1 = [i for i in enumerate(l)]
# print(l1)

# question 4
l = ["apple", "google", "yahoo", "gmail", "elephant"]
# append the names starting with vowels into new list
l1 = []
for i in l:
    if i[0] in "aeiouAEIOU":
        l1.append(i)
l1 = [i for i in l if i[0] in "aeiouAEIOU"]
# print(l1)

# question 5
l = ["apple", "google", "yahoo", "gmail", "elephant"]
# create a new list with all the words starting with consonants reversed and words starting with vowels as same
l1 = []
for i in l:
    if i[0] in "aeiouAEIOU":
        l1.append(i)
    else:
        l1.append(i[::-1])

l1 = [i if i[0] in "aeiouAEIOU" else i[::-1] for i in l]

# print(l1)
