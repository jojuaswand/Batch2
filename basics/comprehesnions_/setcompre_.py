# s = "hellohiworld"
# l = [(i, s.count(i)) for i in s]
# print(l)
# s = set((i, s.count(i)) for i in s) #set comprehension is similar to list comprehension
# print(s) #but duplicate values will be removed and it will be not in order

# s = {1, 2, 3, 4, 5}
# s1 = {i**2 if i % 2 == 0 else i*10 for i in s}
# print(s1)
# print(s)
# print(sorted(s))
# s2 = {i**2 if i % 2 == 0 else i*10 for i in sorted(s)}
# print(s2)
# print(sorted(s2))
# print(sorted(s2, reverse=True))

# s = {"hello", "hi", "bye", "world"}
# s1 = set(i for i in s if len(i) % 2 != 0)
# print(s1)
# print(sorted(s1, key=len))


# s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# s1 = {i for i in s if i % 2 == 0}
# s2 = {i for i in s if i % 2 != 0}
# print(s1)
# print(s2)

# s = {"apple", "yahoo", "google", "microsoft", "elephant", "ole"}
# s1 = {i for i in s if i[0] in "aeiouAEIOU"}
# print(s1)
# print(sorted(s1))
# print(sorted(s1, key=len))

# s = {1, "hi", "hello", 2}
# s1 = {i for i in enumerate(s)}
# print(s1)
# print(sorted(s1))
# s2 = {(i, s[i]) for i in range(len(s))}TypeError: 'set' object is not subscriptable
# print(s2) #set is unorder so cannot use index to get value but can use enumerate to get the index values
# s3 = {i: v for i, v in enumerate(s)}
# print(s3)

# s = {"apple", "yahoo", "google", "microsoft", "elephant", "ole"}
# # s1 = set(i[::-1] if len(i) % 2 == 0 else i for i in s)
# # print(s1)
# s2 = set(i[::-1] if len(i) % 2 == 0 else i + i for i in s)
# print(s2)
#
#
