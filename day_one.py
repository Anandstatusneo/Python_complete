#### Introduction To Lists
"""- Lists are ordered, mutable collections of items.
- They can contain items of different data types."""
lst=[]
print(type(lst))

#Diff data type
names=["Krish","Anand","Jacob",1,2,3,4,5]
print(names)

#Mixed list 
mixed_list=[1,"Hello",3.14,True]
print(mixed_list)

### Accessing List Elements

fruits=["apple","banana","cherry","kiwi","gauva"]

print(fruits[0])
print(fruits[2])
print(fruits[4])
print(fruits[-1])

print(fruits[1:])
print(fruits[1:3])


## Modifying The List elements
fruits

fruits[1]="watermelon"
print(fruits)

################################################################
##############################################################

fruits[1:]="watermelon"

fruits

################################################################
##############################################################

fruits=["apple","banana","cherry","kiwi","gauva"]

fruits.append("orange") ## Add an item to the end
print(fruits)

################################################################
##############################################################

fruits.insert(1,"watermelon")
print(fruits)
################################################################
##############################################################

fruits.remove("banana") ## Removing the first occurance of an item
print(fruits)

################################################################
##############################################################

## Remove and return the last element
popped_fruits=fruits.pop()
print(popped_fruits)
print(fruits)

################################################################
##############################################################

index=fruits.index("cherry")
print(index)
################################################################
##############################################################

fruits.insert(2,"banana")
print(fruits.count("banana"))

################################################################
##############################################################

fruits.sort() ## SSorts the list in ascending order
fruits

numbers=[1,2,3,4,5,5,6,7,8,9,10]

for number in numbers :
   print(numbers)



markes=[50,20,35,86,53,44,68,71,82,94,66]
for index,number in enumerate(markes):
    print(index,markes)


## List comprehension
lst=[]
for x in range(10):
    lst.append(x**2)

print(lst)

#we can do this way also 
[x**2 for x in range(10)]

""" List Comprehension

Basics Syantax            [expression for item in iterable]

with conditional logic    [expression for item in iterable if condition]

Nested List Comprehension [expression for item1 in iterable1 for item2 in iterable2]
"""

### Basic List Comphrension

sqaure=[num**2 for num in range(10)]
print(sqaure)


### List Comprehension with Condition
lst=[]
for i in range(10):
    if i%2==0:
        lst.append(i)

print(lst)

#example 2
new_lst = lst.copy()  # Copy the previous list
for i in range(10):
    new_lst.append(i)

print(new_lst)





even_numbers=[num for num in range(10) if num%2==0]
print(even_numbers)


## Nested List Comphrension

lst1=[1,2,3,4]
lst2=['a','b','c','d']

pair=[[i,j] for i in lst1 for j in lst2]

print(pair)


## List Comprehension with function calls
words = ["hello", "world", "python", "list", "comprehension"]
lengths = [len(word) for word in words]
print(lengths)  # Output: [5, 5, 6, 4, 13]