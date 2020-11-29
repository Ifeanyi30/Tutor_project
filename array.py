import numpy as np
from functools import reduce
from collections import Counter
import numpy as np
from scipy import stats

list1 = [1,2,3]
list2 = [4,5,6]
my_array = np.array([list1, list2])

print(my_array)
print(my_array.shape)

mydict = {'john': [45,54,56], 'yolanda':[98,78,87], 'Joshua':[67,78,87]}

new_item = []
for items in mydict.items():
    print(items)
    reducer = reduce(lambda x,y: x + y, items[1])/3
    new_item.append((items[0], reducer))

newdict = Counter(dict(new_item))

print(newdict.most_common(1))

total = 0.0

lister = ['gtwye', 'dsgugsd', 4, True, 3.34, 34, False, 736]

for x in lister:
    if x == str(x):
        total += 1
    elif x is bool:
        total += 2 if x is True else total-3
    else:
        total += x
print( total )

def find_item(listed, item):
    listed.sort()
    #Returns True if the item is in the list, False if not.
    if len(listed) == 0:
        return False

    middle = int(len(listed)/2)

    #Is the item in the first half of the list?
    if item < listed[middle]:
    #Call the function with the first half of the list
        return find_item(listed[:middle], item)
    
    #Is the item in the center of the list?
    if listed[middle] == item:
        return True

    else:
    #Call the function with the second half of the list
        return find_item(listed[middle+1:], item)

    return False

#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False


def prolog(mylist):

    for x in range(2):
        del mylist[0]
        del mylist[-1]
    return mylist

scores = [23, 23,45, 45, 65, 65]

result = prolog(scores)

print(result)