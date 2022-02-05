"""#from functions import demander_age
nom = input("Quel est votre nom? ")
age = input("Quel est votre age? ")
# pour bien jouer au football
#age = 28
try:
    age_prochain = int(age) + 1
except ValueError:
    print("Vous devez rentrer un nombre")
else:
    print("Vous vous appelez " + nom + ", Vous avez " + str(age) + " ans")
    print("L'an prochain, vous aurez " + str(age_prochain) + " ans")"""

# boucle while
#from functions import *

"""n = 0

print("debut de la boucle")
while n < 10:
    print("Valeur de n: " + str(n))
    n = n + 2
print("Fin de la boucle")
"""

# mot de passe
"""mot_de_passe = ""
while not mot_de_passe == "toto":
    mot_de_passe = input("Quel est votre mot de passe? ")
    print("mot de passe incorrect")
print("Mot de passe correct")"""


# condition pour demander l'age
"""age_prochain = 0
while age_prochain == 0:
    age = input("Quel est votre age? ")
    try:
        age_prochain = int(age) + 1
        #print(age_prochain)
    except:
        print("Vous devez rentrer un nombre pour l'age")
    else:
        print("Vous avez " + str(age) + " ans," "l'annee prochaine vous aurez " + str(age_prochain) + " ans")
"""

# pour ne pas laisser le nom vide
"""nom = ""
while nom == "":
    nom = input("Quel est votre nom?: ")

print("Votre nom est: " + nom)"""

#demander_nom()
#demander_age(demander_nom()
#nom1 = demander_nom()
#nom2 = demander_nom()
#age1 = demander_age(nom1)
#age2 = demander_age(nom2)
#demander_age("Vieux")
#name = demander_nom()
#print(name)

#afficher_information_personne(nom1, age1)
#afficher_information_personne(nom2, age2)

"""from qcm import qcm
qcm()"""

#from tortue_project import *
#from escalier import escalier, carre, carres
#escalier(40,5)
#carres(45,4)

from nombre_magique import demander_nombre_magique, demander_nombre_magiques, recuperer_et_afficher_infos_personne, afficher_table_multiplication
#demander_nombre_magiques(1,10)

from qcm import questionnaires
"""recuperer_et_afficher_infos_personne(1)
recuperer_et_afficher_infos_personne(2)
recuperer_et_afficher_infos_personne(3)"""

#afficher_table_multiplication(10)
#questionnaires("quel?", "a", "b", "c","d", "a")
#questionnaires("quel?", "a", "b", "c","d", "c")

def list_new():
    noms = []
    reponse = " "
    while reponse != "":
        reponse = input("Quel est votre nom: ")
        if reponse != "":
            noms.append(reponse)
    print(noms)
    return noms
#list_new()

def distance_chauffeur():
    distance_chauf = [1.6, 1.2, 1.0, 7, 90]
    valeur_max = distance_chauf[0]
    for distance in distance_chauf:
        if valeur_max < distance:
            valeur_max = distance
            index_max = distance_chauf.index(valeur_max)
    print(valeur_max, index_max)
#distance_chauffeur()

from qcm import questionnaires_am
#question1 = [("quel"),("a","b","c","d"),"b"]
#(question1)

"""from detect_extension import detect_extension, get_definition_extension
fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT","vacances.jpeg","planning","data.dat")

definition_extension = (
    ("doc", "Document Word"),
    ("exe","Executable"),
    ("txt","Document texte"),
    ("jpeg", "Image JPEG")
)
for fichier in fichiers:
    ext = detect_extension(fichier)
    if ext:
        definition = get_definition_extension(ext, definition_extension)
        if not definition:
            definition = "extension non connue"
    else:
        definition = "Aucune extension"
    print(fichier + " (" + definition + ")")"""

from compter_caracteres import count_caract, count_with_completion, count_with_join, zip_function
nom = ["bakary", "salut", "tango", "Zoe"]
nom2 = ["bakary", "salut", "tango"]
nom3 = ["1", "2", "3"]
#count_caract(nom)
#count_caract(nom2)
zip_function(nom2,nom3)