somelist = []
input = int(input())

for i in range(1, input+1):
    if (31 % (i+1) == 1):
        somelist.append(i)
for i in somelist:
    print(i)
