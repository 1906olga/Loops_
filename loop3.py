from random import sample

list_a = sample(range(1, 10), 5)
list_b = sample(range(1, 10), 5)
list_c = list_a+list_b
list_c.sort()
sum=0
for chislo in range(len(list_c)):
    if list_c[chislo] != list_c[chislo-1] and list_c[chislo] != list_c[chislo+1]:
        sum+=1
print('количество уникальных элементов в списках ', sum)
