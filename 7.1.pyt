#escolher um número aleatorio de 10000 até 99999

#transforma o número em uma lista

import random as rd

num=rd.choice(range(10000,100000))
print(f"numero: {num}")
num_list=list(str(num))
print(num_list)
"num_inverso*'"
for i in range(len(num_list)):
    num_inverso=str(num_inverso)+str(num_list[4-i])

print("Inverso! {num_inverso}")