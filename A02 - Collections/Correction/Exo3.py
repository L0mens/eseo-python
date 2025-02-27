import random

def isAllUniq(collect):
    return len(set(collect)) == len(collect)

lst = []
lst_test = [1,1,2,3]
for i in range(random.randint(2,100)):
    lst.append(random.randint(0,500))

print(isAllUniq(lst_test))
print(isAllUniq(lst))