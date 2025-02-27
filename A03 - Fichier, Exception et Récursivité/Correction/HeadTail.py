import sys

try:
    
    if len(sys.argv) != 4: # Si on a pas tous les paramètres
        raise KeyError()
    
    if sys.argv[1].lower() not in ["head","tail"]:
        raise ValueError()
    
    if not sys.argv[2].isnumeric() or int(sys.argv[2]) < 0 :
        raise ValueError()
    
    with open(sys.argv[3], 'r', encoding='utf-8') as file:
        if sys.argv[1].lower() == 'head':
            for _ in range(int(sys.argv[2])):
                print(file.readline().rstrip()) #rstrip() pour enlever les \n donc non obligatoire
        
        if sys.argv[1].lower() == 'tail':
            for line in (file.readlines() [-int(sys.argv[2]):]):
                print(line.rstrip())
        
    
except ValueError:
    print("Un champs n'as pas le bon format, rappel : head/tail nbPositif PathToFile")

except IOError:
    print("Erreur dans la lecture du fichier")

except KeyError:
    print("Les paramètres ne sont pas correctes, rappel : head/tail nbPositif PathToFile")

