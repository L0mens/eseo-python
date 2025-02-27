
poids = float(input("Quel est votre poids en kg : "))
taille = float(input("Quel est votre taille en mètres : "))

imc = poids / (taille*taille)

print(f"Votre IMC est de {round(imc)}")