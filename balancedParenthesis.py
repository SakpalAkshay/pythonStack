def isBalanced(string):

    for char in string:
        s=[]
        if char in "({[":
            s.append(char)
        
        elif(char is ")"):
            if(not s or s[-1]!="("):
                return False
            s.pop()
        elif(char is "}"):
            if(not s or s[-1]!="{"):
                return False
            s.pop()
        elif(char is "]"):
            if(not s or s[-1]!="["):
                return False
            s.pop()
    if (not s):
        return True
    return False


inputStr = input()
print(isBalanced(inputStr))