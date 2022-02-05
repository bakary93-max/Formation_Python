def qcm():
    print("""
    a = "paris"
    b = "dakar""")
    response = input("\tQuelle est la capitale de la France? Faites votre choix en tapant la lettre correspondante ")
    if response.lower() == "a":
        print("\tbravo")
    else:
        print("\tDésolé, la réponse était Paris")
    return

def questionnaire():
    print("Quelle est la capitale de la France? ")
    print(
    """
    a) Paris
    b) Montpellier
    c) Nice
    d) Clermont
        """)
    reponse = input("Votre reponse: ")
    if reponse.lower() == "a":
        print("bonne réponse!")
    else:
        print("mauvaise reponse!")

#factoriser code

def questionnaires(titre_question, r1, r2, r3, r4, bonne_reponse):
    score = 0
    print("question :", titre_question)
    print("(a)",r1)
    print("(b)",r2)
    print("(c)",r3)
    print("(d)",r4)

    response = input("Votre réponse: ")
    if response.lower() == bonne_reponse.lower():
        print("bonne reponse")
        score += 1
    else:
        print("mauvaise réponse")
    print(score)

def questionnaires_am(question):
    print(question[0])
    for i in range(len(question[1])):
        print(i+1,")", question[1][i])
    response = input("Votre réponse entre 1 et " + str(len(question[1])) +":" + " ")
    response_int = int(response)
    if (question[1][response_int-1]).lower() == (question[-1]).lower():
        print("bonne reponse")
    else:
        print("mauvaise réponse")