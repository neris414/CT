class Prepare:
    inputstr = ""
    splitted = []
    def __init__(self,input_str):
        self.splitted = []
        self.inputstr = input_str
        for i in range(len(self.inputstr)-1):
            self.splitted.append(self.inputstr[i:i+2].upper())
    
    def makeDict(self):
        tempDict = {}
        sett = set(self.splitted)
        for i in range(len(sett)):
            tempDict[list(sett)[i]] = self.splitted.count(list(sett)[i])
        keyarray = list(tempDict.keys())
        for i in keyarray:
            if i.isalpha() == False:
                del tempDict[i]
        return tempDict
    
class Jaq:
    dict1 = {}
    dict2 = {}
    interSet = set()
    unionSet = set()
    def __init__(self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2
        self.interSet = set(dict1.keys()) & set(dict2.keys())
        self.unionSet = set(dict1.keys()) | set(dict2.keys())
    def calc(self):
        intersection = 0
        union = 0
        for i in self.interSet:
            intersection += min(self.dict1[i], self.dict2[i])
        for i in self.unionSet:
            try:
                try:
                    union += max(self.dict1[i], self.dict2[i])
                except:
                    union += self.dict1[i]
            except:
                union += self.dict2[i]
        try:
            return int((intersection / union) * 65536)
        except:
            return 65536
                

def solution(str1, str2):
    answer = 0
    str1_dict = Prepare(str1).makeDict()
    str2_dict = Prepare(str2).makeDict()
    answer = Jaq(str1_dict, str2_dict).calc()
    return answer
