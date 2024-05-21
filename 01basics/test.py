print("4",7) #print seperately

print(type("12"))

print("""use triple quotes for 
multiple lines""")

print('I\'m learning python') # \ is used as to escape the next character so in this case single qoute is accepted as it is without having any extra meaning.

my_var = "barks"
print("A dog {my_var}")
print(f"A dog {my_var}") # when we use f string it will consider anything within a {} as an expression
print("A dog {}".format(my_var)) 

print("Hello \t world") # \t is uesd for tab space

print("C:\\user\\test") #if you want to print \ you have to use double \ for that
print("C:\user\test")# this will throw SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape