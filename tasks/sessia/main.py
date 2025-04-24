# получение данных из файла
file = open('./sessia/demo_2025_26.txt')
# получение количества студентов
n = int(file.readline())
# получение данных студентов в виде списка [id,оценка1, оценка2, оценка3, оценка4]
a = [list(map(int,s.split())) for s in file]
# сортировка по студентов по id
a.sort(key = lambda x: x[0])
# получение сдавших студентов
offset = [x for x in a if x[1:].count(2)==0]
# получение не сдавших студентов
missing = [x for x in a if x[1:].count(2)!=0]
# сортировка по успеваемости (среднему баллу) сдавших студентов
offset.sort(key = lambda x: sum(x[1:]),reverse=True)
# сортировка студентов по количеству 2
missing.sort(key = lambda x: x[1:].count(2))
# получение общего рейтинга с правильной сортировкой
rating = offset+missing
# получение первого в рейтинге человека с 3 и более 2
for x in rating:
    if x[1:].count(2) > 2:
        idg22 = x[0]
        break
print(rating[n//4-1][0],idg22)


