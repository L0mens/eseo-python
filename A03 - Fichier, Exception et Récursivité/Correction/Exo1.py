
def factorielle(n):
    if n < 0 : # Pour éviter de calculer une factiorielle négative
        raise ValueError()
    if n == 1 :
        return 1    
    else:
        return n * factorielle(n-1)

try:
    print(factorielle(10))
    print(factorielle(-10))
except ValueError as ve :
    print("N ne peut être négatif")