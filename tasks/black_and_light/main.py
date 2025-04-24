f = open('./black_and_light/26.txt').readlines()[1:]
# создание словаря
Sl = {i: [] for i in range(1, 10**5 + 1)}
# запись данных в словарь по типу ключ - значение (x - y координаты)
for i in f:
    ind, v = map(int, i.split())
    Sl[ind] += [v]

def func(v):
    st = ''
    for x, y in zip(v, v[1:]):
        st += '*' if x + 1 == y else '* '
    return len([1 for s in (st + '*').split() if len(s) >= 3])

Sl = {i: func(sorted(set(v))) for i, v in Sl.items()}
print((t:=max(Sl.values())),list(Sl.keys())[::-1][list(Sl.values())[::-1].index(t)])
