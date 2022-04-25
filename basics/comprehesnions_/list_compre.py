
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


