from random import sample
# формируем список из случайных 20 чисел (рост от 135 до 200 см)
list_a = sample(range(135, 200), 20)

# вводим с клавиатуры рост Пети
b=int(input())

# добавляем число в конец списка
list_a.append(b)

# сортируем список по убыванию
list_a.sort(reverse=True)

# узнаем предварительно номер элемента в списке (место Пети)
index = list_a.index(b)

# считаем количество повторений значения роста как у Пети
c=list_a.count(b)

# рассчитываем место
place=0
place=c+index
print ('место Пети в строю ',place)