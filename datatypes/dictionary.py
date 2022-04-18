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
# d.update(place = 'bamgalore', new = "newplace1") #its taking multiple key value pair
# print(d)
#
# d["place", "age"]= "bangalore", 20 #creating a tuple of key and value but not separately
# print(d)

