# 1.
import re

def getFileName(filePath) -> None:
    arr = re.split("[/.]", filePath)
    ext = arr[-1]
    filename = arr[-2]
    path = filePath[0:len(filePath) - (len(filename + ext) + 1)]
    return path, filename, ext
filePath2 = "c:/folder1/folder2/filename.ext"
print(getFileName(filePath2))


# 2.
def task5(names: list[str], rate: list[int], bonus: list[str]) -> dict[str: float]:
    length = len(names)

    result = dict()

    for i in range(length):
        f1 = {names[i]: rate[i] + rate[i] * (float(bonus[i].replace('%', ' ')))/100}
        yield f1
    return result

n, s, b = ['Иванов', 'Петров', 'Сидоров'], [10000, 20000, 30000], ["10.25%", "2.5%", "5.5%"]
for i in task5(n, s, b):
    print(i)


# 3.
def fibonacci(n):
    f1, f2 = 0, 1
    for i in range(n):
        f1, f2 = f2, f1 + f2
        yield f1

for f in fibonacci(20):
    print(f, end =' ')
print() 
