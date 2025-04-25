# Получение данных с файла
a=open('26.txt').readlines()
boxes=[]
# компановка данных в лист типа: размер - цвет
for s in a:
    d,type=s.split()
    boxes.append([int(d),type])
# сортировка по размеру
boxes.sort()
count_block=0
maxdepth=0
# цикл по всем контейнерам
while len(boxes)>0:
    # создание нового блока (с первым контейнером)
    block=[boxes[0]]
    boxes.remove(boxes[0])
    i=0
    # создание блока с контейнером (исследование оставшихся контейнеров на то, подходят ли они)
    while i < len(boxes):
        box=boxes[i]
        # если разница текущего контейнера и последнего контейнера блока больше 5 и разные цвета
        if box[0]-block[-1][0] >= 5 and box[1] != block[-1][1]:
            # контейнер добавляется в блок
            block.append(box)
            boxes.remove(box)
        else:
            # переход к следующему контейнеру
            i += 1
    # подсчёт максимальной вложенности и сравнение с прошлой
    maxdepth=max(len(block),maxdepth)
    # подсчёт количества блоков
    count_block+=1
print(maxdepth,count_block)
