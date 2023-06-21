import random
import numpy as np

Encode = open("encoded.txt","r")

n=100000
str_bit=Encode.read()
erroneous=np.zeros(int(n*7/4),dtype=int)

for i in range(int(n*7/4)):
    erroneous[i]=int(str_bit[i])

error=0
for i in range(int(n/4)):
    if random.randint(0,24)==0:
        bit=random.randint(0,6)
        if erroneous[i*7+bit]==1:
            erroneous[i*7+bit]=0
        else:
            erroneous[i*7+bit]=1
        error=error+1
        # print(i*7+bit)


Encode.close()
Encode = open("encoded.txt","w")
for i in range(int(n*7/4)):
    Encode.write(str(erroneous[i]))
# Encode.write(str_bit)
Encode.close()

# print(error)