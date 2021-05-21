def makeVec(input_value):
    tmp = []
    for i in range(len(input_value)):
        if input_value[i] == "(":
            tmp.append(1)
        else:
            tmp.append(-1)
    return tmp

def decoding(input_vec):
    tmp = ""
    for i in input_vec:
        if i == 1:
            tmp += "("
        else:
            tmp += ")"
    return tmp

def isBalanced(vector):
    balance_value = 0
    for i in vector:
        balance_value += i
    if balance_value == 0:
        return True
    else:
        return False

def isCorrect(vector):
    if (vector[0] == 1) & (vector[-1] == -1):
        return True
    else:
        return False

def revise(vector):
    for i in range(len(vector)):
        vector[i] = -vector[i]
    return "".join(decoding(vector[1:-1]))

def correction(w, correct = ""):
    u = []
    v = makeVec(w)
    result = correct
    for i in range(len(w)):
        if w[i] == "(":
            u.append(1)
        else:
            u.append(-1)
        del v[0]
        if (isBalanced(u) == True):
            if (isCorrect(u) == True):
                result += decoding(u)
            else:
                result += "(" + revise(u) + ")"
            return correction(decoding(v),result)
    return result

def solution(p):
    answer = correction(p)
    return answer

#---------------------------------------------------------------------수정------------------------------------------------------#

def correction(w, correct = ""):
    u = ""
    reverse_u = ""
    v = w
    balanced_value = 0
    result = correct

    for i in range(len(w)):
        if w[i] == "(":
            balanced_value += 1
            u += "("
            reverse_u += ")"
        else:
            balanced_value -= 1
            u += ")"
            reverse_u += "("
        v = v[1:]
        if (balanced_value == 0):
            if (u[0] == "(") & (u[-1] == ")"):
                result += u
            else:
                result += "(" + reverse_u[1:-1] + ")"
            return correction(v,result)
    return result

def solution(p):
    answer = correction(p)
    return answer