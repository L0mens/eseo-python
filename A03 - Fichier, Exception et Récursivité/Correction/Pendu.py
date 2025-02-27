import unicodedata, random
from LettreDejaJoueException import LettreDejaJoueException 

# Gère les accents
def strip_accents(s):
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )

# Permet de récupérer un mot au hasard du fichier dict
def get_one_word():
    words = []
    with open("dic.txt", "r", encoding="utf-8") as dic:
        words = dic.readlines()
    return strip_accents(words[random.randint(0, len(words))].rstrip()).lower()


final_word = get_one_word()
print(final_word)

attemps = 7
display = ""
found_l = final_word[0]
letter_attempted = []

for ind, l in enumerate(final_word):
    if ind == 0:
        display = l + " "
    else:
        display = display + "_ "


print("Pendu")

while attemps > 0:
    print("\nMot à deviner : ", display)
    proposition = input("proposez une lettre : ")[0:1].lower()
    # On insère le bloc try/excpt pour gérer notre exception
    try:

        if proposition in final_word:
            #Si on a déjà proposer la lettre, on lève notre custom exception
            if proposition in letter_attempted:
                raise LettreDejaJoueException
            #Sinon on ajoute la proposition aux lettres tenté et validé
            found_l = found_l + proposition
            letter_attempted.append(proposition)

        else:
            #Si la lettre n'est pas bonne, on ajouté un essai
            attemps = attemps - 1
            print("Fail\n")
            if attemps == 0:
                print(" ==========Y= ")
            if attemps <= 1:
                print(" ||/       |  ")
            if attemps <= 2:
                print(" ||        0  ")
            if attemps <= 3:
                print(" ||       /|\ ")
            if attemps <= 4:
                print(" ||       / \ ")
            if attemps <= 5:
                print("/||           ")
            if attemps <= 6:
                print("==============\n")
    except LettreDejaJoueException as ldje:
        print("Lettre déjà joué")

    # Gestion de l'affichage des trou
    display = ""
    for x in (final_word):
        index = final_word.index(x)
        if index == 0 :
            display += x + " "
        elif x in found_l:
            display += x + " "
        else:
            display += "_ "

    # Si l'affichage n'as plus de trou, c'est qu'on a tout trouvé ! Bien joué 
    if "_" not in display:
        print(">>> GGGGGGGGG <<<")
        break
