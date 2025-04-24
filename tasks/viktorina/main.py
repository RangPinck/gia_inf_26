# считывание всей информации с файла
f = open("./viktorina/26.txt").readlines()
# разбиаение информации с перестройкой шаблона
f = [x.replace("\n", "").split() for x in f]

f = [list(map(int, x)) for x in f]

round_1 = []

for i in f:
    summ = sum(i[1:])
    id_ = i[0]

    x = 0 #сумма +
    c = 0 #кол-во ответов
    for elem in i[1:]:
        if elem > 0:
            x += elem

        if elem != 0:
            c +=1

    if summ > 0:
        round_1.append((summ,x,c,id_))

round_1 = sorted(round_1, key=lambda x: [x[3]])
round_1 = sorted(round_1, key=lambda x: [x[0], x[1], x[2]],reverse = True)

round_2 = round_1[:len(round_1)//4]

a = round_1[len(round_1)//4]

for elem in round_1[len(round_1)//4:]:
    if elem[0] == a[0] and elem[1] == a[1] and elem[2] == a[2]:
        round_2.append(elem)


b = round_1[1808:((len(round_1)-len(round_2))//10)+1808]

final_round = b

for elem in round_1[((len(round_1)-len(round_2))//10)+1808:]:
    if elem[0] == 12 and elem[1] == 16 and elem[2] == 8:
        final_round.append(elem)

print(final_round[0][3],len(final_round))
