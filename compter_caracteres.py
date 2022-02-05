
#with for and len moins lourd en mémoire
def count_caract(nom):
    sum = 0
    for i in nom:
        #print(len(i))
        sum = sum + len(i)
    print("le nombre de caractères est: " +str(sum))
    return sum


#With completion prend plus de mémoire
def count_with_completion(nom):
    sumb = [len(nom) for nom in nom]
    print("le nombre de caractères est: " +str(sum(sumb)))

#with join/len la meilleure

def count_with_join(nom):
    nom_joined = "".join(nom)
    print("le nombre de caractères est: " + str(len(nom_joined)))

#la fonction zip
def zip_function(a,b):
    chaine = list(zip(a,b))
    #print(chaine)
    for (nom, numero) in chaine:
        #print(f"{nom} - {numero}")
        chaine = list(zip(*chaine)) # for unzip
        print(chaine2)

