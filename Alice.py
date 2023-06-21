import numpy as np

# reads .txt file
Data = open("input.txt","r")
Encode = open("encoded.txt","w")

G = np.array([[1, 0, 0, 0, 0, 1, 1], 
              [0, 1, 0, 0, 1, 0, 1], 
              [0, 0, 1, 0, 1, 1, 0], 
              [0, 0, 0, 1, 1, 1, 1]], dtype=int)
M = np.zeros(4, dtype=int)

n=100000
for i in range(int(n/4)):
    for j in range(4):
        M[j]=int(Data.read(1))
    C = np.matmul(M,G)
    # C=np.bitwise_xor(M,G)
    # Encode.write(str(C%2))
    for j in range(7):
        Encode.write(str(C[j]%2))

Data.close()
Encode.close()