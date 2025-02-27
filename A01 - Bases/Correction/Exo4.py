
def pi_app(nb_approx=15):
    pi = 3
    PAS=4
    for i in range(0, nb_approx):
            pi += (4 / ((2 + PAS * i) * (3 + PAS * i) * (4 + PAS * i))) - (4 / ((4 + PAS * i) * (5 + PAS * i) * (6 + PAS * i)))
            print(pi)

if __name__ == "__main__":
    pi_app()