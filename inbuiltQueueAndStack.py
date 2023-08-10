'''Python provide a inbuilt queue library to implement Queue, the same library has LifoQueue which provides functionality of Stack
put() - enters or push an element
get() - pops an element => Last element in Stack and First element in Queue
empty() - checks if queue of Lifoqueue is empty
'''

import queue


#Functionality of Queue
q = queue.Queue()
q.put(10)
q.put(20)
q.put(30)
q.put(40)

while q.empty() is False:
    print(q.get())

#Functionality of Stack
s = queue.LifoQueue()
s.put(10)
s.put(20)
s.put(30)
s.put(40)

while s.empty() is False:
    print(s.get())




