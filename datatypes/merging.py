s = "hello"
s1 = "bye"
# print(s + s1) #1st way to merge combines s with s1
# a = *s, *s1
# print(a, type(a))
# print(*s, *s1)#2nd way to merge combines s with s1 but there will be spaces in between
#

l = [1, 2, 3]
l1 = [4, 5, 6]
# print(l + l1) #merging list
# print(*l, *l1) #merging the values
# s = *l, *l1
# print(s, type(s))

t = (1, 2, 3)
# t1 = (4, 5, 6)
# print(t + t1) #merging tuple
# print(*t, *t1) #merging the values

s = {1, 2, 3}
s1 = {4, 5, 6}
# print(s + s1) set doesnt support concartination or add operator
# print(*s, *s1) #merging sets but only the values

d = {"name": "steve", "age": 21}
d1 = {"name": "harvey", "age": 23}
d2 = {"place": "bangalore", "bangalore":"city"}
d4 = {"a": 1, "b": 2}
d5 = {"c": 3, "d": 4}
# print(d + d1) #dict doesnt support concartination or add operator
print(*d, *d1) #merging the keys of both the dictionary
# print(**d, **d1 #same key with multiple values not possible to merge)
# print(**d, **d2) #we were trying top get key value pair without mentioning dictionary
print({**d4, **d5}) #merged key value pairs of both the dictionaries
print(d4 | d5) #merged key value pair of both dictionaries with only using pipe
