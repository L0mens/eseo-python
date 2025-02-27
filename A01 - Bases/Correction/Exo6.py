def calcul():
    out = "o"
    while out.lower() != "n":
        ope = input("type d'opération souhaité : (a)ddition, (s)oustraction, (m)ultiplication et (d)ivision : ")

        if ope in ["a","s","m","d"]:
            num1 = input("Saisir un chiffre 1 : ")
            num2 = input("Saisir un chiffre 2 : ")
            calc = ""
            if ope == "a":
                calc = f"{num1} + {num2}"
            if ope == "s":
                calc = f"{num1} - {num2}"
            if ope == "d":
                calc = f"{num1} / {num2}"
            if ope == "m":
                calc = f"{num1} * {num2}"

            print(f"Résultat : {calc} = {eval(calc)}")

            out = input("Un autre calcul ? o/n ")
        
        else:
            print("calcul non compris !!")
            out = input("Un autre calcul ? o/n ")

if __name__ == "__main__":

    calcul()