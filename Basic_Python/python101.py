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

















