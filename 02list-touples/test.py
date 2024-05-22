cars_list = ['toyota', 'honda', 'suzuki', 'volkswagan']

print(type(cars_list))

print(cars_list[-1]) # - is used to access the list from last 
#print(cars_list[-5]) # IndexError: list index out of range
#cars_list[4] = 'maruti' #IndexError: list assignment index out of range


#append
cars_list.append("Aulto")
#print(cars_list)
#cars_list.append('audi','bmw') #TypeError: list.append() takes exactly one argument (2 given)

#insert
cars_list.insert(5,'ford')
#cars_list.insert(cars_list.__len__(),'audi')
print(cars_list)

#extend
cars_list.extend(['audi','bmw']) # to insert multiple value in list use list_name.extent(['','',''])
print(cars_list)

#index
print(cars_list.index('ford'))
#print(cars_list.index('Ford')) # .index is case sensitive 

#remove
#print(cars_list.remove('sfdvs')) #ValueError: list.remove(x): x not in list
#print(cars_list.remove(cars_list[3])) # remove the element in the index 3 in the list
print(cars_list)

#----------------------------------------------
# = vs copy.copy vs deepcopy
import copy




# Using the assignment operator
a = [1, 2, [3, 4]]
b = a  # b is just another reference to the same list that a refers to
b[0] = 10  # This will change the list that both 'a' and 'b' refer to
print(a)  # Output will be [10, 2, [3, 4]]

# Using copy.copy()
a = [1, 2, [3, 4]]
b = copy.copy(a)  # b is now a shallow copy of 'a'
b[0] = 10  # This will change only 'b', not 'a'
b[2][0] = 30  # This will change the inner list that both 'a' and 'b' refer to
print(a)  # Output will be [1, 2, [30, 4]]

#Using copy.deepcopy()
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)  # b is now a deep copy of 'a'
b[0] = 10  # This will change only 'b', not 'a'
b[2][0] = 30  # This will change only 'b', not 'a'
print(a)  # Output will be [1, 2, [3, 4]]


