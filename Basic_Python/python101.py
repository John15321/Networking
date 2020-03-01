#!/bin/python3

# Print a string
print("Strings and strings:")
print("Hi")
print('''Multi
line 
comment''')
print("This is"+" a string")
print("\nnew line \n")

# Maths
print("Math time:")
print(50+50)
print(50-50)
print(50*50)
print(50/50)
print(50**5)
print(50%4)
print(50//5.2)

print("\n\n") # new line

# Variables & Methods
print("Fun with variables and methods:")
quote = "All is fair in love and war"
print(len(quote)) #print length of a string
print(quote.upper()) # print in upper case
print(quote.lower()) # print in lower
print(quote.title()) # first letters of each word in upper

name = "John"
age = 20 # int 
gpa = 3.7 # flaot

print(int(age))
print(age)
print(int(29.9)) # does not round

print("My name is " + name + " and I am " + str(age) + " years old")


print("\n\n") # new line



# Now some functions 
def who_am_I(name="John", age=20):
    print("My name is " + name + " and I am " + str(age) + " years old")    

who_am_I("Reeee", 99)
who_am_I()

print("\n\n") # new line

# List 
print("Lists:")
movies = ["Finding Nemo", "Your mom lol", "The Expanse", "Kek"]
print(movies[0])
print(movies[0:2])
print(movies[1:])
print(movies[:3])
print(movies[-1])
print(len(movies))

movies.append("Jaws")
print(movies)
movies.pop()
print(movies)
movies.pop(0)
print(movies)




movies = ["Finding Nemo", "Your mom lol", "The Expanse", "Kek"]



person = ["John", "Jake", "Jeff"]
comnd = zip(movies, person)
print(list(comnd)) # there will be no "Kek"


# Tuples
print("Tuples have () and cannot change")

grades = ("A", "B", "C", "D", "F")
print(grades[0])




# Looping 
print("LOOOOOOOOOOPS * insert a fat kitty *")




for x in movies:
    print(x)


i = 0
while i<10:
    print(i)
    i+=1





# Importing 
print("Importing is important:")

import sys # system functions and parameters

from datetime import datetime
print(datetime.now())

from datetime import datetime as dt # importing with an alias
print(dt.now())

def new_line():
    print("\n")

new_line()

# Advanced Strings
print("Advanced strings:")
my_name = "John"
print(my_name[0])
print(my_name[-1])
print(my_name[-2])

sentence = "This is a sentance."

print(sentence[:4])
print(sentence[-9:-1])

# spliting sentances

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join+"\n")

quotes = "I like money"
print(quotes)
quotes = "'I like money'"
print(quotes)


print("A" in "Apple")


letter = "a"
word = "Apple"

print(letter.upper() in word.upper())



too_much_space = "                hello             "
print(too_much_space.strip())
full_name = "ohn B"
print(full_name.replace("ohn", "John"))
print(full_name)





movie = "Finding Nemo"

print("My fav movie is {}".format(movie))

def fav_book(title, auth):
    return "My fav books is \"{}\", which is written by {}".format(title, auth)
    
print(fav_book("Star Wars", "George Lucas"))

new_line()


# Dictionaries
print("Dictionaries are keys and values:")
drinks = {"White Russians" : 7, "Old Fashion" : 10, "Lemon Drop": 8, "Nipple": 6}
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy", "John"]}
print(employees)

employees["Legal"] = ["Mr. Ford"] # add a new key

print(employees)

employees.update({"Sales": ["Andy", "Ollie"]})
print(employees)

drinks["White Russians"] = 8

print(drinks)





print(drinks.get("White Russians"))
print(drinks.get("ASDASD"))
print(drinks["White Russians"])


movies = ["When Harry met Sally", "The Hangover", "Parks and recreation", "The Exorcist"]
person = ["John", "Heath", "Bob", "Jeff"]
combined = zip(movies, person)
movie_dict = {key: value for key, value in combined}
print(movie_dict)











