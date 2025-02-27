import collections


def ajoutecoefficient(polynome, coef):
    poly = collections.deque(polynome)  # vérification que l'on a bien une deque
    if len(poly) >= 3:
        print("Erreur polynome invalide")
    else:
        poly.append(coef)
    return poly


def saisiePolynome():
    coef = -1
    n = 0
    polynome = collections.deque()
    while n < 3:
        coef = int(input("Veuillez saisir le coefficient" + str(n) + "(0 pour ne pas valoriser un coefficient)"))

        polynome.append(coef)
        n = n + 1
    return polynome


def affiche_polynome(polynome):
    signe = ""

    for i in range(0, len(polynome)):
        if i == 1 or i == 2:  # gestion des signes uniquement pour les deuxieme et troisieme monomes
            if polynome[i] > 0:
                signe = "+"
            else:
                signe = ""

        if i == 0 and polynome[i != 0]:  # avec le signe X2
            print(signe + str(polynome[i]) + "X²", end='')
        elif i == 1 and polynome[i != 0] and signe == "-":  # X signe -
            print(signe + str(polynome[i]) + "X", end='')
        elif i == 1 and polynome[i != 0] and signe == "+":  # X signe +
            print(str(polynome[i]) + "X", end='')
        elif polynome[i] != 0 and polynome[i - 1] != 0:  # dernier monome avec existence de X
            print(signe + str(polynome[i]), end='')
        elif polynome[i] != 0 and polynome[i - 1] == 0:  # dernier monome sans existence de X
            print(str(polynome[i]), end='')


def addition(polynome1, polynome2):

    polyaddition = collections.deque()
    for i in range(0, len(polynome1)):
        polyaddition.append(polynome1[i]+polynome2[i])
    return polyaddition


def destruction(polynome):
    poly = collections.deque()
    poly.clear()
    return poly


def derivation(polynome):
    polynome[0] *= 2
    if polynome[1] is not None:
        polynome[2] = polynome[1]
    polynome[1] = polynome[0]
    polynome[0] = 0
    return polynome

def multiplication(polynome,monome):
    for i in range(0,len(polynome)):
        polynome[i]*=monome
    return polynome




# ***************************test ajout coefficients***************************
# queue = collections.deque()
# queue = [2]
# print(ajoutecoefficient(queue, 1))
# *************************test saise polynome**********************************
# print(saisiePolynome())
# **************************test affichage polunome******************************
# affiche_polynome(saisiePolynome())
# ***************************derivation d'un polynome*****************************
# affiche_polynome(derivation(saisiePolynome()))
# ****************************addition de deux polynome*****************************
#affiche_polynome(addition(saisiePolynome(), saisiePolynome()))
#******************************multiplication par un monome*************************/
affiche_polynome(multiplication(saisiePolynome(),3))
