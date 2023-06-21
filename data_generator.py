import random
# creates .txt file

Data = open("input.txt","w")

# number of bit to be generated
n=100000
for i in range(n):
    Data.write(str(random.randint(0,1)))

Data.close()