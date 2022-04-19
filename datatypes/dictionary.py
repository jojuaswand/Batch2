# d = {} #empty dictionary is the default value {}
# print(d, type(d))
# d = dict()
# print(d, type(d))
# # d = dict(1)TypeError: 'int' object is not iterable
# # d = dict("hi") ValueError: dictionary update sequence element #0 has length 1; 2 is required
# # d = dict(["hi", 1]) TypeError: cannot convert dictionary update sequence element #1 to a sequence
# # d = dict(("hi", 1))TypeError: cannot convert dictionary update sequence element #1 to a sequence
# d = dict(name = "1")
# # d = dict(("name") = "1") #dict() only takes string as a key
# print(d)
# #dictionary has elements in the form of key value pair
# d = {"name":1, (1,): 2}
# print(d)
# d = dict(name = "hi", age = 20, x = 7889)
# print(d)
# d = {"name": "steve", "age": 56, (1,2): 1 }
# print(d)
# # d = {{"name"} : "hi"} #TypeError: unhashable type: 'set' only for keys
# d = {"name": {1,2}} #it will take any data type as value
# print(d)

# d = dict(name="hi", age=20, x=7889)
# # d[0] = "bye" #we created a key value pair while trying to change value based on index
# d["age"] = 23 #we can change value with key
# d["name"] = "bye"
# d[1] = 10
# print(d)

# d = dict({"name": 1})
# # d = dict([("a", 1), ("b", 2)])
# d = {"name" : "hi"}
# d = dict(name = 1)
# d = dict(age = 20)
# print(d)

#accessing
# d = dict(name="hi", age=20, x=7889)
# print(d)
# print(d['name']) #to access values we have to mention the key
# print(d['age']) #key is storing the value
# print(d['x'])
# print(id(d)) #dictionary is having an address
# print(id(d["name"])) #the key is having another address different from the original dictionary
# # d = {"name": "hi", "name": "bye"} #we cannot use same key
# d = {"name": "hi", "age": "hi"} #we can use same values
# print(id(d["name"]), id(d["age"]))
# # print(d["hi"]) KeyError: 'hi' #we cannot access values directly
# # print(d["y"]) KeyError: 'y' if that key is not in existence

# d ={"name": "steve", "age": 23}
# print(d)
# print(d.items()) #returns all the key value pair in the form of list of tuples
# print(d.keys()) #returns a list of all keys
# print(d.values()) #returns a list all values

# #update()
# d ={"name": "steve", "age": 23}
# d.update(place = "bangalore") #this update() is creating new key value pair
# print(d)
# d.update(place = "chennai") #overriding key value
# print(d)
# d.update(place = 'bangalore', new = "new_place_1") #its taking multiple key value pair
# print(d)
#
# d["place", "age"]= "bangalore", 20 #creating a tuple of key and value but not separately
# print(d)

#clear()
# d = {"name": "steve", "age": 23}
# print(d.clear()) #it removes all the key value pairs from the dictionary and returns none
# print(d) #its affecting the original dictionary

#copy()
# d = {"name": "steve", "age": 23}
# d1 = d
# print(d, id(d))
# print(d1, id(d1))
# d.update(new=1)
# print(d)
# print(d1)
# d = {"name": "steve", "age": 23}
# d1 = d.copy()
# print(d, id(d))
# print(d1, id(d1))
# d.update(new=1)
# print(d)
# print(d1)

#pop
# d = {"name": "steve", "age": 23}
# # print(d.pop()) #TypeError: pop expected at least 1 argument, got 0
# # print(d.pop(0)) KeyError: 0
# print(d.pop("age")) #pop takes key as value for dictionary and it returns popped value but not key
# print(d) #its affecting key value pair in the original dictionary

#popitem()
d = {"name": "steve", "age": 23, "new": 1, "place": "bangalore"}
# print(d.popitem())  #its removing the last key value pair of the dictionary and doesnt take any specific value to remove and its returning the removed key value pair
# print(d) #its affecting the original value
# print(d.popitem("new")) #TypeError: dict.popitem() takes no arguments (1 given)

#get()
# d = {"name": "steve", "age": 23, "new": 1, "place": "bangalore"}
# print(d.get("name")) #its returning the value inside a key
# print(d.get("name", "place")) #its returning only one value even though two keys were mentioned but its not throwing any error
# # print(d.get("name", "place", "age")) TypeError: get expected at most 2 arguments, got 3
# print(d.get("new1")) #it returns none when the mentioned key is not in existence

#fromkeys
# d = {"name": "steve", "age": 23, "new": 1, "place": "bangalore"}
# print(d.fromkeys(d,d))
# l = ["name", "age"]
# l1 = ["steve", 23]
# s = "steve"
# a = "add_value"
# d = {}
# print(d.fromkeys(l)) #generates key for a dictionary
# print(d.fromkeys(l1))
# print(d.fromkeys(l, l1)) #generated key value pair but value remains same for every key
# print(d.fromkeys(l, s))
# print(d.fromkeys(l,a))
#
#setdefault()
# d = {"name": "steve", "age": 23, "new": 1, "place": "bangalore"}
# print(d["name"])
# # print(d["bangalore"])
# # d.setdefault("bangalore")
# # print(d)
# # print(d["bangalore"])
# # d["bangalore"] = 10
# # print(d)
# d.setdefault("bangalore", "city") #its generates a a key which has no value with some value but by default its going to be none
# print(d)
# print(d["bangalore"])
# d["bangalore"] = "urban" #we can update default key with any value required
# print(d)

d = {"name": "steve", "age": 23, "new": 1, "place": "bangalore"}
# x = str(d) #converts everything into a character and makes it a collection of characters
# print(x)
# i = int(d) #TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
# print(i)
l = list(d) #list takes all the keys from dictionary by default
l = list(d.values()) #list of values
l = list(d.items()) #list of tuples with key and value
# f = float(d) #TypeError: float() argument must be a string or a number, not 'dict'
# print(l)
# print(f)
# x ="a" , "b"
# print(x)
t = tuple(d) #by default its going to give only key values
t = tuple(d.values()) #only values from dictionary
t = tuple(d.items()) #key value pair in thr form of tuples inside a tuple
# print(t)
# c = complex(d) #TypeError: complex() first argument must be a string or a number, not 'dict'
b = bool(d) #gives true because dictionary is not empty
# print(b)
s = set(d) #gives keys of the dictionary by default
s = set(d.values()) #returns the value of dictionary
s = set(d.items()) #returns a set of tuples having key value pair of dictionary
# print(s)

d1 = dict(d)
print(d1)
