#LIST

#thislist = ["apple", "banana", "cherry"]
#print(thislist)

'''Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)'''

'''thislist = ["apple", "banana", "cherry"]
print(len(thislist))'''

'''list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]'''

'''list1 = ["abc", 34, True, 40, "male"]'''

'''mylist = ["apple", "banana", "cherry"]
print(type(mylist))'''


'''Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)'''

'''List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.'''

'''thislist = ["apple", "banana", "cherry"]
print(thislist[1])'''

'''thislist = ["apple", "banana", "cherry"]
print(thislist[-1])'''

'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])'''

'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])'''

'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])'''

'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])'''

'''thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")'''

'''thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)'''

'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)'''

'''thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
answer: ['apple', 'blackcurrant', 'watermelon', 'cherry']'''

'''thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
answer:['apple', 'watermelon']'''

'''thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)'''

'''thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)'''

'''Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)'''

#The extend() method does not have to append lists, you can add any iterable object

"""thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)"""

'''thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)'''

'''Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)'''

"""thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)"""

'''Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist'''

"""thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)"""

"""thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)"""

'''thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])'''

'''thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1'''

'''thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]'''


'''fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
answer:['apple', 'banana', 'mango']'''


'''fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)'''

#newlist = [expression for item in iterable if condition == True]
#newlist = [x for x in fruits if x != "apple"]

#newlist = [x for x in range(10)]

#newlist = [x for x in range(10) if x < 5]

#newlist = [x.upper() for x in fruits]

#newlist = ['hello' for x in fruits]
#answer = ['hello', 'hello', 'hello', 'hello', 'hello']

#newlist = [x if x != "banana" else "orange" for x in fruits]
#answer = ['apple', 'orange', 'cherry', 'kiwi', 'mango']

'''thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)'''

'''thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)'''

'''thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)'''

'''thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)'''

'''By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)'''

'''thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)'''

'''thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)'''

'''thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)'''

'''list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)'''

'''list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)'''





#WHILE

'''i = 1
while i < 6:
  print(i)
  i += 1'''

'''i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1'''

'''i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)'''

'''i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")'''



#FOR

'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)'''

'''for x in "banana":
  print(x)'''

'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break'''

'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)'''

'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)'''

'''for x in range(6):
  print(x)'''

'''for x in range(2, 6):
  print(x)'''

'''for x in range(2, 30, 3):
  print(x)'''

'''for x in range(6):
  print(x)
else:
  print("Finally finished!")'''

'''adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)'''

'''for x in [0, 1, 2]:
  pass'''





#TUPLE

'''thistuple = ("apple", "banana", "cherry")
print(thistuple)'''

'''Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)'''

'''thistuple = ("apple", "banana", "cherry")
print(len(thistuple))'''


'''thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))'''


'''tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)'''

#tuple1 = ("abc", 34, True, 40, "male")

'''mytuple = ("apple", "banana", "cherry")
print(type(mytuple))'''

'''Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)'''

'''thistuple = ("apple", "banana", "cherry")
print(thistuple[1])'''

'''thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])'''

'''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])'''

'''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])'''

'''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])'''

'''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])'''

'''thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")'''

'''Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)'''

'''thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)'''

'''thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)'''

'''thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)'''

'''thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists'''

"""fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)"""

'''Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)'''

'''fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
answer = apple
        ['mango', 'papaya', 'pineapple']
        cherry'''

'''thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)'''

'''thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])'''

'''thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1'''

'''tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)'''

'''fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)'''

#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found

 




#SET
# Set items are unchangeable, but you can remove items and add new items.

'''thisset = {"apple", "banana", "cherry"}
print(thisset)'''

'''Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)'''

'''thisset = {"apple", "banana", "cherry"}
print(len(thisset))'''

#set1 = {"abc", 34, True, 40, "male"}

"""myset = {"apple", "banana", "cherry"}
print(type(myset))"""

'''thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)'''

'''thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)'''

'''thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)'''

'''Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)'''

#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
"""thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)"""

#If the item to remove does not exist, remove() will raise an error.
#If the item to remove does not exist, discard() will NOT raise an error.
"""thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)"""

'''thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)'''

#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
'''thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)'''

'''thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)'''

'''The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)'''

'''thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)'''

'''The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)'''

'''set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)'''

"""Keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)"""

"""x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)"""

'''x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)'''

'''issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not'''

'''isdisjoint()	Returns whether two sets have a intersection or not'''






#DICTIONARY

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)"""


"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])"""


'''Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)'''

#print(len(thisdict))

'''thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}'''

'''thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)'''

#x = thisdict.get("model")

'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]'''

'''Get a list of the keys:
x = thisdict.keys()'''
#dict_keys(['brand', 'model', 'year'])

'''car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change'''

#x = thisdict.values()
#dict_values(['Ford', 'Mustang', 1964])

#x = thisdict.items()
#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")'''

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})"""

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})"""

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)"""

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)"""

'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)'''

"""for x in thisdict:
  print(x)"""

'''for x in thisdict:
  print(thisdict[x])'''

'''for x in thisdict.values():
  print(x)'''

'''for x in thisdict.keys():
  print(x)'''

'''for x, y in thisdict.items():
  print(x, y)'''

'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)'''
'''myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
answer = {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}'''

"""Get the value of the "model" item:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)"""