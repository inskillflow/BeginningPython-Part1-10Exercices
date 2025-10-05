numbers = []
strings = []
names = ["mark", "john", "peter"]

#Adding numbers to the list which we named numbers
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

#Adding some names to the list which we named strings
strings.append("Yves")
strings.append("Mark")
strings.append("Catherine")
strings.append("Yannick")
strings.append("Sarah")

#displing the lists
print (numbers)
print (strings)

#displaying elements of the lists
print (numbers[0])
print (strings[0])

#How to access to the List elements
second_name=strings[1]
print("The second name in the names list is %s" % second_name)