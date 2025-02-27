
def dectobin(nb_dec):
    res = ""
    q = nb_dec
    while q > 0 :
        r = q % 2
        res = f"{res}{str(r)}"
        q = q//2
    return res[::-1]

if __name__ == "__main__":
    print(dectobin(17))
    print(dectobin(6))