a = int(input())
li1 = []
for i in range(a):
    li1.append(int(input()))
dic1 = {}
dic1[1] = 1
for i in range(2,li1[-1]+1):
    if(i%2==0):
        dic1[i] = dic1[i-1]*2
    else:
        dic1[i] = dic1[(i+1)//2]+dic1[(i-1)//2]
print(dic1)