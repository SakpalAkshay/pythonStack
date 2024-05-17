#reverse a string using stack
str = "Geekforgeekz"   # o/p = zkeegrofkeeG
stack = []

newStr = ""

for i in str:
    stack.append(i)


while len(stack) !=0:
    e = stack.pop()
    newStr+=e

print(newStr)