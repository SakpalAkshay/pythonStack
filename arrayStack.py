class Stack:

    def __init__(self):
        self.__data = []   #a private variable for array


    def push(self,item):
        self.__data.append(item)
    
    def pop(self):

        if self.isEmpty():
            print("Empty Stack !!!")
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            print("Empty Stack !!!")
        return self.__data[len(self.__data) - 1]

    def size(self):

        return len(self.__data)
    
    def isEmpty(self):
        return self.size() == 0



stack = Stack()
stack.push(10)
stack.push(11)
stack.push(12)
top = stack.top()
print(top)
while stack.isEmpty() is False:
    print(stack.pop())