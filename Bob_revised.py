import numpy as np

Encode = open("encoded.txt","r")
reconciled = open("reconciled_message.txt","w")

H=np.array([[0, 1, 1, 1, 1, 0, 0],
           [1, 0, 1, 1, 0, 1, 0],
           [1, 1, 0, 1, 0, 0, 1]],dtype=int)
Base = np.array([4, 2, 1], dtype=int)

n=100000
error=0
C=np.zeros(7,dtype=int)
corr=np.zeros(3,dtype=int)
for i in range(int(n/4)):
    for j in range(7):
        C[j]=Encode.read(1)
    S=(np.matmul(H,C))%2
    corr[0]=S[0]^S[1]^S[2]
    corr[1]=S[1]^S[2]
    corr[2]=S[0]^S[2]
    corrupt=np.dot(corr,Base)

    # # print(S)
    # print(corrupt)
    if corrupt!=0:
        C[corrupt-1]=(C[corrupt-1]+1)%2
        error=error+1
    for j in range(4):
        reconciled.write(str(C[j]))

reconciled.close()
Encode.close()
print(error/n)