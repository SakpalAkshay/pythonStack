# pythonStack 

A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.


Stack in python

The functions associated with stack are:

isEmpty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top()– Returns a reference to the topmost element of the stack – Time Complexity: O(1)
push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)


# Stack Using List

__init__(self): This is the constructor method that initializes a new instance of the Stack class. It creates an empty list named __data to store the elements of the stack. The double underscores before data indicate that it's a private variable, meaning it should not be directly accessed from outside the class.

push(self, item): This method is used to push an item onto the stack. It takes an item as an argument and appends it to the end of the __data list.

pop(self): This method is used to pop (remove and return) the top item from the stack. It first checks if the stack is empty using the isEmpty method. If the stack is not empty, it uses the pop() method of the __data list to remove and return the last item in the list.

top(self): This method returns the top item of the stack without removing it. It first checks if the stack is empty using the isEmpty method. If the stack is not empty, it retrieves the last item from the __data list using indexing.

size(self): This method returns the number of elements currently in the stack by using the len function on the __data list.

isEmpty(self): This method checks if the stack is empty by comparing the size of the stack (returned by the size method) with zero.


# Stack using Linked List
The linked list nodes hold the stack elements, with the __head attribute pointing to the top node.
 Node Class:
The Node class is defined with the following attributes and methods:
__init__(self, data): The constructor initializes a new instance of the Node class with a given data value. It also initializes the next attribute as None to represent that this node is not yet connected to another node.

Stack Class:
The Stack class is defined with the following methods:

__init__(self): The constructor initializes an instance of the Stack class. It initializes two attributes: __head, which represents the top node of the stack (initially set to None as the stack is empty), and __count, which keeps track of the number of elements in the stack.

push(self, element): This method is used to push an element onto the stack. It creates a new Node instance with the given element, sets its next attribute to the current __head (top of the stack), updates __head to the new node, and increments __count to reflect the addition of an element.

pop(self): This method is used to pop (remove and return) the top element from the stack. It first checks if the stack is empty using the isEmpty method. If not, it retrieves the data from the top node, updates __head to the next node, decrements __count to reflect the removal of an element, and returns the retrieved data.

top(self): This method returns the value of the top element of the stack without removing it. It first checks if the stack is empty using the isEmpty method. If not, it returns the data from the top node.

size(self): This method returns the number of elements currently in the stack (stored in __count).

isEmpty(self): This method checks if the stack is empty by comparing the size of the stack (returned by the size method) with zero. It returns True if the stack is empty, otherwise False.

# Stack and Queue inbuilt Libraries in Python
In Python, you can create and manage queues using the built-in queue module, which provides implementations of various queue data structures. The queue module offers three main classes for implementing different types of queues:

Queue: This class provides a basic FIFO (First-In-First-Out) queue implementation. It is a synchronized (thread-safe) queue and is typically used for communication between multiple threads.

LifoQueue: This class provides a LIFO (Last-In-First-Out) queue implementation. It is also synchronized and useful for implementing a stack-like behavior.

PriorityQueue: This class provides a priority queue implementation. Elements are dequeued based on their priority, which is determined by the order they were inserted or by a specific priority assigned during enqueue.

Queue module provides thread-safe implementations of these data structures. If you are working with multiple threads, you can use these queues to safely exchange data between threads. If you don't need thread safety, you can also consider using Python's built-in list data structure as a basic queue or stack.

# Checking Balanced Parenthesis
 Stack-based approach to check if the brackets in the input string are balanced or not. It iterates through each character in the string, maintains a stack of opening brackets encountered, and matches them with closing brackets. If at any point the brackets are not properly balanced, the function returns False, and if all brackets are balanced, it returns True.


 # Reverse a Stack using Recursion
 The function reverse is defined with two arguments, s1 and s2.

The base case of the recursion is defined: if the length of s1 is less than or equal to 1, the function returns immediately. This is because a single element or an empty list is already considered reversed.

A while loop is used to transfer elements from s1 to s2 until there is only one element left in s1. This loop is used to pop elements from the end of s1 (using the pop() method) and append them to s2.

The last remaining element in s1 is then popped and stored in the lastelement variable.

Another while loop is used to transfer elements from s2 back to s1. This loop is used to pop elements from the end of s2 and append them to s1.

Now, the reverse function is recursively called with the modified lists s1 and s2.

After the recursive call, the lastelement (which was the original last element of s1) is appended back to s1.
