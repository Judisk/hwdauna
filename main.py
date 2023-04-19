import random

N=15
array=[]
i=0
for i in range(0,N):
    array.append(random.randrange(0,101))
    i+=1
array_sum=[]
j=0
for j in array:
    if j%10==7:
        array_sum.append(j)
if array_sum != []:
    k=0
    result=0
    for k in array_sum:
        result+=k

    answer=result/len(array_sum)
    print(answer)
else:
    print("В массиве нет нечетных чиcел заканчивающихся на 7")

