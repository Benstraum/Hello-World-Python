# this is how you comment

# this declares a variable
string = 'Hello World'
print(string)

# Similar to let in js you can redefine
string = 'Now im Redeclared'
print(string)



# class is creating a cronstructor for objects
class Person:
    # def __init__() is a function to assign object properties
    # this is the proper way to initialize an object and is bad to skip this process like how we 
    # have been in 

    # self is not a keyword in python BUT it is generally considered best practice for readability
    # first slot is used to define how to target the properties inside object?
     def __init__(self, name, age):
        self.name = name
        self.age = age

me=Person('Ben',26)
p2=Person('Ollie', 100)
p3=Person('Barbara', 74)
#doesn't like printing an object
print(me)
#instead dot notation to call properties
print('this is me inside python', me.name, me.age)




#create lists (taco)
listOne = []
#append into list similar to push
listOne.append(me)
listOne.append(p2)
listOne.append(p3)

# can also loop through arrays
for el in listOne:
    print(el.name, el.age)

#again they hate calling just objects
taco=['can', 'create', 'list', 'on', 'the', 'fly']
print(taco)

# this calls the final thing!!! called negative indexing
print(taco[-1])


#Tuples are type of lists/arrays that cannot be modified


#Sets are unordered chaos of arrays with no indexing. written with curly brackets
thisset = {"apple", "banana", "cherry"}
print(thisset)

#dictionaries are kind of like object arrays?  indexed and have key/value pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["year"])