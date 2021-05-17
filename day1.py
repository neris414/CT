class User:
    def __init__(self, uid, nickname):
        self.uid = uid
        self.nickname = nickname
        self.virtual_nickname = nickname
    def setNickname(virtual_nickname):
        self.virtual_nickname = virtual_nickname
        
class AdminInterface:
    box = []
    def enterRoom(self, someone):
        message = "Enter %s %s"%(someone.uid, someone.virtual_nickname)
        self.box.append(message)
        
    def changeNickname(self, someone, virtual_nickname):
        someone.virtual_nickname = virtual_nickname
        message = "Change %s %s"%(someone.uid, someone.virtual_nickname)
        self.box.append(message)
        
    def leaveRoom(self, someone):
        message = "Leave %s"%(someone.uid)
        self.box.append(message)
    
class MessageBox:
    command = []
    uid = []
    nickname = []
    new_nickname = []
    result = []
    def __init__(self, box):
        for i in box:
            self.command.append(i.split()[0])
            self.uid.append(i.split()[1])
            try:
                self.nickname.append(i.split()[2])
            except:
                self.nickname.append(self.nickname[-1])
        self.new_nickname = self.nickname.copy()
        
    def setNickname(self, index):
        for i in range(len(self.new_nickname)):
            if self.uid[i] == self.uid[index]:
                self.new_nickname[i] = self.nickname[index]
    
    def display(self):
        for i in range(len(self.command)):
            if self.command[i] in ["Enter","Change"]:
                self.setNickname(i)
        for i in range(len(self.command)):
            if self.command[i] == "Enter":
                self.result.append(self.new_nickname[i]+"님이 들어왔습니다.")
            elif self.command[i] == "Leave":
                self.result.append(self.new_nickname[i]+"님이 나갔습니다.")
            else:
                pass
def solution(record):
    answer = []
    m = MessageBox(record)
    m.display()
    answer = m.result

    return answer


