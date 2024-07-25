# Исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Расчет среднего балла
srednee = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
# Переводим множество в список
students = list(students)
# Сортируем список по алфавиту
list.sort(students)
# Создаем словарь
dict = {}
# Заполняем словарь
dict.update({students[0]:srednee[0], students[1]:srednee[1], students[2]:srednee[2], students[3]:srednee[3], students[4]:srednee[4]})
print(dict)