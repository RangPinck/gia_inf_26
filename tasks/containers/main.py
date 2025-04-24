#получение данных
file = open('./containers/26_59853.txt').readlines()[1:]

# разделение данных по листам для удобства перебора
packages = []
containers = []
for item in file:
    item = [int(i) for i in item.split()]
    packages.append(item[0])
    containers.append(item[1])

# перебор с сравнением (проверка того, что для каждого товара есть контейнер)
counter = 0
maxPackage = -1
for package in packages:
    for i in range(len(containers)):
        if containers[i] > package:
            containers[i] -= package
            counter += 1
            maxPackage = max(maxPackage, package)
            break

# вывод результата
print(counter, maxPackage)
