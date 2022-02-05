#fonction pour demander age
def demander_age(nom_personne):
    age_prochain = 0
    while age_prochain == 0:
        age = input(nom_personne + "! Quel est votre age? ")
        try:
            age_prochain = int(age) + 1
            #print(age_prochain)
        except ValueError:
            print("Vous devez rentrer un nombre pour l'age")
        else:
            print("Vous avez " + str(age) + " ans," "l'annee prochaine vous aurez " + str(age_prochain) + " ans")

    return age

# fonction pour demander le nom
def demander_nom():
    nom = ""
    while nom == "" or nom.strip().isdigit():
        nom = input("Entrer votre nom: ")
    #print(" Votre nom est " + nom)
    return nom


def afficher_information_personne(nom, age):
    print("Votre nom est: " + nom , "Votre age est: " + str(age))
    if int(age) > 18 :
        print("Vous êtes majeur")
    elif int(age) == 17:
        print( "Vous êtes presque majeur")
    elif int(age) == 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")