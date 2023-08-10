# pythonStack
A repo to record my learning of Stack in Python 

A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.


Stack in python

The functions associated with stack are:

empty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)


# Stack Using List
The Stack class is defined with several methods for managing a stack data structure.

__init__(self): This is the constructor method that initializes a new instance of the Stack class. It creates an empty list named __data to store the elements of the stack. The double underscores before data indicate that it's a private variable, meaning it should not be directly accessed from outside the class.

push(self, item): This method is used to push an item onto the stack. It takes an item as an argument and appends it to the end of the __data list.

pop(self): This method is used to pop (remove and return) the top item from the stack. It first checks if the stack is empty using the isEmpty method. If the stack is not empty, it uses the pop() method of the __data list to remove and return the last item in the list.

top(self): This method returns the top item of the stack without removing it. It first checks if the stack is empty using the isEmpty method. If the stack is not empty, it retrieves the last item from the __data list using indexing.

size(self): This method returns the number of elements currently in the stack by using the len function on the __data list.

isEmpty(self): This method checks if the stack is empty by comparing the size of the stack (returned by the size method) with zero.
