from string import ascii_uppercase
import random

def get_plaque():
    plaque = ""
    good_char = [x for x in ascii_uppercase if x not in ['U','I','O'] ]
    for i in range(9):
        if i in [2,6]:
            plaque = f"{plaque}-"
        elif i in [3,4,5]:
            plaque = f"{plaque}{random.randint(0,9)}"
        else:
            plaque = f"{plaque}{random.choice(good_char)}"

    # Façon récursive de traiter le SS, si on en trouve un, on regen la plaque
    if 'SS' in plaque:
        plaque = get_plaque()
    return plaque

if __name__ == '__main__':
    for i in range(20):
        print(get_plaque())