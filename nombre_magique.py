NOMBRE_MAGIQUE = 4
def demander_nombre_magique(nb_max, nb_min):
    number = input(f"Donnez le nombre magique entre {nb_max} et {nb_min}: ")
    if number == NOMBRE_MAGIQUE:
        print("bravo")
    else:
        print("Désolé! le nombre magique est:" + str(NOMBRE_MAGIQUE))
    return NOMBRE_MAGIQUE

def demander_nombre_magiques(nb_max, nb_min):
    number = 0
    while not number == NOMBRE_MAGIQUE:
        demander_nombre_magique(nb_max, nb_min)
        if number == NOMBRE_MAGIQUE:
            print("bravo")
        elif number > NOMBRE_MAGIQUE:
            print("Désolé! le nombre magique est plus petit")
        else:
            print("Désolé! le nombre magique est plus grand")

def recuperer_et_afficher_infos_personne(numero_personne):
    nom = input("Quel est le nom de la personne" + str(numero_personne) + ": ")
    age = input("Quel est l'age de la personne" + str(numero_personne) + ": ")
    print("la personne" + str(numero_personne) + " est " + nom + " son age est: " + str(age) + "")
    nombre_de_personnes = 5
    for i in range(nombre_de_personnes):
        recuperer_et_afficher_infos_personne(i + 1)


def afficher_table_multiplication(n):
    for i in range(1 ,11,3):
        print(str(n) + "*" +str(i) + "=" + str(n*i) + "")
        print(n, "*", i, "=", n * i)



