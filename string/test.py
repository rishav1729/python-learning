text = "Hello, Stack Abuse!"
print(text[0:5])


## split() Method 
## sybtax => string.split(separator=None, maxsplit=-1)

text = "Computer science is fun"
split_text = text.split()
print(split_text)  # Output: ['Computer', 'science', 'is', 'fun']

text = "Python,Java,C++"
split_text = text.split(',')
print(split_text)  # Output: ['Python', 'Java', 'C++']

text = "one two three four"
split_text = text.split(' ', maxsplit=2)
print(split_text)  # Output: ['one', 'two', 'three four']

#.join
split_text = ('apple', 'banana')
text = ' '.join(split_text)
print(text) 

split_text = {'apple', 'banana'}
text = ' '.join(split_text)
print(text) 

split_text = ['apple', 'banana']
text = ' '.join(split_text)
print(text) 

# replace() Method

text = "Hello, World"
replaced_text = text.replace("World", "Stack Abuse")
print(replaced_text)  # Output: Hello, Stack Abuse

text = "cats and dogs and birds and fish"
replaced_text = text.replace("and", "&", 2)
print(replaced_text)  # Output: cats & dogs & birds and fish

## startswith
filename = "Example-report.pdf"
if filename.startswith(".pdf"):
    print("The file is a PDF document.")

# count
quote = "To be, or not to be, that is the question."
# Count occurrences of 'be' in the substring from index 10 to 30
count = quote.count("be", 10, 30)
print("'be' appears", count, "times between index 10 and 30")


# isspace
text = "\n"
if text.isspace():
    print("The string contains only whitespace characters.")






