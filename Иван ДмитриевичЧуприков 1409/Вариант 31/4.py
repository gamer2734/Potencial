a = open('history_mirror.csv', encoding='utf-8')#открываем Файл
b = a.readlines()
c = []
d = []
f = []
for i in b: #преобразовываем файл
    if i.count('\n') == 1:
        i = i.replace('\n', '')
        c.append(i.split(','))
for k in c: # получаем года использования
    e = k[0].split('-')
    d.append(e[0])
d.remove(d[0]) #удаляем ненужные элементы
count = 0
for j in range(2000, 2025): #сортируем года 
    for n in d:
        if int(n) == j:
            count+=1
    f.append(count)
    count = 0
for g in range(len(f)):
    print(f' В {2000+g} году зеркало было использовано {f[g]} раз')
            
