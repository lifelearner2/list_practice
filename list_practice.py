#This program doubles a list.
#each iteration of i will be equal to the correlating index position and then stored in the numbers variable.
#once it's stored then we multiple that index by 2 and repeat until each index position of list is done



numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    elem_at_index = numbers[i]
    numbers[i] = 2 * elem_at_index

print(numbers) #prints [2,4,6,8]

#adding to a list/empty list with the append method/function
my_list = []
my_list.append(42)
print(my_list) #prints [42]

#remove from list
x = my_list.pop()
print(x) #pop func removes the element from the end of a list adn then returns that number to be stored in the variable x - so x = 42. You will get an error if you try to remove an element from an empty list.

#check if list contains elements or certain elements
my_new_list = [42, 100, 10]
if 42 in my_new_list:
        print("List has element!")
else: 
    print("Element not present")
    
    
if -3 in my_new_list:
    print("list has negative 3 element")
else: 
    print("Element not present")
    
  