sentence = input("Enter sone white space seperaated words:")

words = sentence.split(" ")
print(words) #['what', 'lies', 'behind', 'us', 'and', 'what', 'lies', 'before', 'us', 'are', 'tiny', 'matters', 'ccompared', 'to', 'what', 'lies', 'within', 'us']

set_of_words = set(words)
print(set_of_words) #{'and', 'behind', 'to', 'matters', 'ccompared', 'what', 'lies', 'within', 'are', 'tiny', 'before', 'us'}

sorted_set_of_words = sorted(set_of_words)
print(sorted_set_of_words) #['and', 'are', 'before', 'behind', 'ccompared', 'lies', 'matters', 'tiny', 'to', 'us', 'what', 'within']

print(" ".join(sorted_set_of_words)) #and are before behind ccompared lies matters tiny to us what within
