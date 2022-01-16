from random import sample

list_a = sample(range(0, 100), 10)
print (list_a)
sum=0
for chislo in range(1, len(list_a)):
    if list_a[chislo] > list_a[chislo-1] and list_a[chislo]>list_a[chislo+1]:
         sum+=1
print('количество элементов, которые больше двух своих соседей (слева и справа)= : ', sum)
