
def syraccuse(n):
    print(int(n))
    if n ==1 :
        return 1
    else:
        if n%2 == 0:
            syraccuse(n/2)
        else:
            syraccuse(3*n +1)

syraccuse(15)