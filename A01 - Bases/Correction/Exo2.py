import statistics

lst = []
n = int(input("Ajouter un nombre (-1 pour quitter) : "))
while(n >= 0):
    lst.append(n)
    n = int(input("Ajouter un nombre (-1 pour quitter) : "))
    

print(lst.sort())

print(min(lst))

print(max(lst))

print(sum(lst)/len(lst))
# OU
print(statistics.mean(lst))