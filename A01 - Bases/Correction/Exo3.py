anneeHumaine=0
anneeCanine=0
anneeHum=int(input("Veuillez saisir votre age"))
if anneeHumaine > 0:
    if anneeHumaine > 2:
        anneeCanine=21+((anneeHumaine-2)*4)
    else:
        anneeCanine=anneeHumaine*10.5
    print("Votre age canin est de "+str(anneeCanine)+" ans")
else:
    print("L'age doit être positif")
