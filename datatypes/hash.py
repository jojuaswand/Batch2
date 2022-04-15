#hash() gives us the hash value of a certain data
i = 1
i = 100001
print(i, hash(i)) #for integer hash value will be the integer itself
f = 1.1
print(f, hash(f)) #for float there is a hash value but its not the float value itself and the hash value is not a float type
c = 1+2j
print(c, hash(c)) #for complex there is a hash value and its not a complex value its hash value is of integer
print(True, hash(True)) # for boolean values hash value is there but its the integer value of boolean
#until individual values hash value didnt change every time
s = "hi"
print(s, hash(s)) #for string some hash value is there and its not in string its of integer
#and it can be btoth negative and +ve integer value and its changing everytime
l = [1, 2, 3]
# print(l, hash(l)) TypeError: unhashable type: 'list' #list doesnt hash value
t = (1, 2, 3)
print(t, hash(t)) #tuple has integer hash value but it is not changing
s = {1, 2, 3}
# print(s, hash(s)) TypeError: unhashable type: 'set' #set doesnt have hash value
d = {1 : 1, 2 : 3, 4 : 4 }
# print(d, hash(d)) #TypeError: unhashable type: 'dict' #dictionary doesnt have hash value


