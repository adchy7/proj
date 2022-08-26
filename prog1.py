
#lists are ordered, mutable, allows duplicate elements

list1 = ['banana', 'cherry', 'apple']
print(list1)

list2  = list()
print(list2)       # will print empty list

list3 = [5, True, "apple","apple"]
print(list3)

print('\n')
print('###############')
print('list1 is:',list1)
print('First element:',list1[0])
print(list1[1])
print(list1[2])
# print(list1[3]) # there is no 4th member

print('###############')
item = list1[0]
print(item)

item = list1[1]
print(item)

item = list1[2]
print(item)

#  item = list1[5]  # IndexError: list index out of range
#  print(item)

print('###############')
item = list1[-1]  # show last item
print(item)

item = list1[-2]  # show 2nd last item
print(item)

item = list1[-3]  # show 3rd last item
print(item)



