def makeVec(inputString):
    tmp = []
    for i in range(len(inputString)):
        if inputString[i] == "(":
            tmp.append(1)
        else:
            tmp.append(-1)
    return tmp

def decoding(inputVec):
    tmp = ""
    for i in inputVec:
        if i == 1:
            tmp += "("
        else:
            tmp += ")"
    return tmp

def isBalanced(inputString):
    balance_value = 0
    for i in makeVec(inputString):
        balance_value += int(i)
    if balance_value == 0:
        return True
    else:
        return False

def isCorrect(inputString):
    balance_value = 0
    for i in makeVec(inputString):
        balance_value += int(i)
        if balance_value == -1:
            return False
    return True

def splitter(inputString):
    left = []
    right = list(inputString)
    for i in inputString:
        left.append(i)
        right.pop(0)
        if isBalanced("".join(left)):
            return ("".join(left),"".join(right))
    return ("".join(left),"".join(right))

def reverse(inputString):
    tmp = ""
    for i in inputString:
        if (i == "("):
            tmp += ")"
        else:
            tmp += "("
    return tmp

def revise(inputString):
    result = ""
    left, right = splitter(inputString)
    while(True):
        if (isCorrect(left)):
            result += left
            left, right = splitter(right)
        else:
            result = result + "(" + reverse(left[1:-1]) + ")"
            left, right = splitter(right)
        if (right == ""):
            return result + left
def solution(p):
    return revise(p)
