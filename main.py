import random

MIN_FACILE = 1
MAX_FACILE = 10
MIN_MOYEN = 10
MAX_MOYEN = 40
MIN_DIFFICILE = 30
MAX_DIFFICILE = 100

FNB_QUESTONS = 10
MNB_QUESTONS = 20
DNB_QUESTONS = 30


def calcul_mixte(minimum, maximum):
    nb_aleatoire1f = random.randint(minimum, maximum)
    nb_aleatoire2f = random.randint(minimum, maximum)
    choix_operateur = random.randint(0, 4)
    operateur = "+"
    if choix_operateur == 1:
        operateur = "-"
    elif choix_operateur == 2:
        operateur = "*"
    elif choix_operateur == 3:
        operateur = "/"
    elif choix_operateur == 4:
        operateur = "%"
    rep_mixte = 0.10201
    while rep_mixte == 0.10201:
        try:
            rep_mixte = float(input(f"Calculer: {nb_aleatoire1f} {operateur} {nb_aleatoire2f} = "))
        except ValueError:
            print("\t\t\tERREUR: Vous devez saisir un nombre !")
    calcul = nb_aleatoire1f + nb_aleatoire2f
    if choix_operateur == 1:
        calcul = nb_aleatoire1f - nb_aleatoire2f
    elif choix_operateur == 2:
        calcul = nb_aleatoire1f * nb_aleatoire2f
    elif choix_operateur == 3:
        calcul = round(nb_aleatoire1f / nb_aleatoire2f, 2)
    elif choix_operateur == 4:
        calcul = nb_aleatoire1f % nb_aleatoire2f
    if rep_mixte == calcul:
        return True
    return False


def calcul_addition(minimum, maximum):
    nb_aleatoire1f = random.randint(minimum, maximum)
    nb_aleatoire2f = random.randint(minimum, maximum)
    rep_addition = 0.10201
    while rep_addition == 0.10201:
        try:
            rep_addition = int(input(f"Calculer: {nb_aleatoire1f} + {nb_aleatoire2f} = "))
        except ValueError:
            print("\t\t\tERREUR: Vous devez saisir un nombre entier !")
    if rep_addition == int(nb_aleatoire1f + nb_aleatoire2f):
        return True
    return False


def calcul_soustration(minimum, maximum):
    nb_aleatoire1f = random.randint(minimum, maximum)
    nb_aleatoire2f = random.randint(minimum, maximum)
    rep_soustration = 0.10201
    while rep_soustration == 0.10201:
        try:
            rep_soustration = int(input(f"Calculer: {nb_aleatoire1f} - {nb_aleatoire2f} = "))
        except ValueError:
            print("\t\t\tERREUR: Vous devez saisir un nombre entier !")
    if rep_soustration == nb_aleatoire1f - nb_aleatoire2f:
        return True
    return False


def calcul_multiplication(minimum, maximum):
    nb_aleatoire1f = random.randint(minimum, maximum)
    nb_aleatoire2f = random.randint(minimum, maximum)
    rep_multiplication = 0.10201
    while rep_multiplication == 0.10201:
        try:
            rep_multiplication = int(input(f"Calculer: {nb_aleatoire1f} * {nb_aleatoire2f} = "))
        except ValueError:
            print("\t\t\tERREUR: Vous devez saisir un nombre entier !")
    if rep_multiplication == nb_aleatoire1f * nb_aleatoire2f:
        return True
    return False


def calcul_division(minimum, maximum):
    nb_aleatoire1f = random.randint(minimum, maximum)
    nb_aleatoire2f = random.randint(minimum, maximum)
    rep_division = 0.10201
    while rep_division == 0.10201:
        try:
            rep_division = float(input(f"Calculer: {nb_aleatoire1f} / {nb_aleatoire2f} = "))
        except ValueError:
            print("\t\t\tERREUR: Vous devez saisir un nombre !")
    if rep_division == round(nb_aleatoire1f / nb_aleatoire2f, 2):
        return True
    return False


def calcul_modulo(minimum, maximum):
    nb_aleatoire1f = random.randint(minimum, maximum)
    nb_aleatoire2f = random.randint(minimum, maximum)
    rep_modulo = 0.10201
    while rep_modulo == 0.10201:
        try:
            rep_modulo = int(input(f"Calculer: {nb_aleatoire1f} % {nb_aleatoire2f} = "))
        except ValueError:
            print("\t\t\tERREUR: Vous devez saisir un nombre entier !")
    if rep_modulo == nb_aleatoire1f % nb_aleatoire2f:
        return True
    return False


def appreciation():
    if choix_niveau == 1:
        if nb_points == FNB_QUESTONS:
            print("\t\t\tExcélent niveau en maths !")
        elif nb_points == 0:
            print("\t\t\tRévisez vos maths !")
        elif nb_points == int(FNB_QUESTONS / 2):
            print("\t\t\tJuste la moyenne, Peut mieux faire !")
        elif nb_points < FNB_QUESTONS / 2:
            print("\t\t\tEn bas de la moyenne, Doit mieux faire !")
        else:
            print("\t\t\tBon niveau en maths !")

    elif choix_niveau == 2:
        if nb_points == MNB_QUESTONS:
            print("\t\t\tExcélent niveau en maths !")
        elif nb_points == 0:
            print("\t\t\tRévisez vos maths !")
        elif nb_points == int(MNB_QUESTONS / 2):
            print("\t\t\tJuste la moyenne, Peut mieux faire !")
        elif nb_points < MNB_QUESTONS / 2:
            print("\t\t\tEn bas de la moyenne, Doit mieux faire !")
        else:
            print("\t\t\tBon niveau en maths !")
    elif choix_niveau == 3:
        if nb_points == MNB_QUESTONS:
            print("\t\t\tExcélent niveau en maths !")
        elif nb_points == 0:
            print("\t\t\tRévisez vos maths !")
        elif nb_points == int(MNB_QUESTONS / 2):
            print("\t\t\tJuste la moyenne, Peut mieux faire !")
        elif nb_points < MNB_QUESTONS / 2:
            print("\t\t\tEn bas de la moyenne, Doit mieux faire !")
        else:
            print("\t\t\tBon niveau en maths !")


reprendre = True
while reprendre:
    reprendre = False
    print(f"""
                    ------------------------------------------------------------------------------------------------------------------
                    |   B I E N V E N U E    D A N S    L E    P R O G R A M M E     D E S    J E U X     M A T H E M A T I Q U E S  |
                    ------------------------------------------------------------------------------------------------------------------
-------------------------------
| MENU CHOIX DU NIVEAU DU JEU |
-------------------------------
Veuillez saisir:
         1 --> Facile:    {FNB_QUESTONS} questions  avec des combinaisons entre {MIN_FACILE}  et {MAX_FACILE}
         2 --> Moyen:     {MNB_QUESTONS} questions  avec des combinaisons entre {MIN_MOYEN}  et {MAX_MOYEN}
         3 --> Difficile: {DNB_QUESTONS} questions  avec des combinaisons entre {MIN_DIFFICILE} et {MAX_DIFFICILE}
         
         NB: Pour des calculs de divisions, en cas de réponse décimale, limitez-vous à deux chiffres après la virgule !
                                 ( Arrondir le résultat par défaut ou par excès selon les cas ) 
        """)

    choix_niveau = 0.20201
    while choix_niveau == 0.20201:
        try:
            choix_niveau = int(input("FAIRE UN CHOIX: "))
        except ValueError:
            print("\t\t\tERREUR: Mauvaise saisie ! Faire un choix entre: 1, 2 et 3 !")
        else:
            if choix_niveau < 1 or choix_niveau > 3:
                print('\t\t\tERREUR: Entrée invalide ! Faire un choix entre: 1, 2 et 3 !')
                choix_niveau = 0.20201

    print("""
----------------------------------------
| MENU DES DIFFERENTS TYPES DE CALCULS |
----------------------------------------
Veuillez saisir:
         1 --> Additions 
         2 --> Soustrations
         3 --> Multiplications
         4 --> Divisions
         5 --> Modulos
         6 --> Mixtes
        """)

    type_calcul = 0.10201
    while type_calcul == 0.10201:
        try:
            type_calcul = int(input("FAIRE UN CHOIX: "))
        except ValueError:
            print("\t\t\tERREUR: Mauvaise saisie ! Faire un choix entre: 1, 2, 3, 4, 5, et 6 !")
        else:
            if type_calcul < 1 or type_calcul > 6:
                print('\t\t\tERREUR: Entrée invalide ! Faire un choix entre: 1, 2, 3, 4, 5, et 6 !')
                type_calcul = 0.10201

    if choix_niveau == 1:

        nb_points = 0
        if type_calcul == 1:
            reprendre_addition = True
            while reprendre_addition:
                reprendre_addition = False
                print(f"""
                                 ---------------------------------
                                 | NIVEAU FACILE DU JEU DE MATHS |
                                 ---------------------------------
---------------------------------
| MODULE 1: CALCULS D'ADDITIONS |
---------------------------------
-->Une série de {FNB_QUESTONS} questions avec des combinaisons entre {MIN_FACILE} et {MAX_FACILE}.
""")
                for i in range(1, FNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {FNB_QUESTONS}")
                    if calcul_addition(MIN_FACILE, MAX_FACILE):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{FNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_addition = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False
        elif type_calcul == 2:
            reprendre_soustration = True
            while reprendre_soustration:
                reprendre_soustration = False
                print(f"""
                                 ---------------------------------
                                 | NIVEAU FACILE DU JEU DE MATHS |
                                 ---------------------------------
-------------------------------------
| MODULE 2: CALCULS DE SOUSTRATIONS |
-------------------------------------
-->Une série de {FNB_QUESTONS} questions avec des combinaisons entre {MIN_FACILE} et {MAX_FACILE}.
""")
                for i in range(1, FNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {FNB_QUESTONS}")
                    if calcul_soustration(MIN_FACILE, MAX_FACILE):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{FNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_soustration = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False
        elif type_calcul == 3:
            reprendre_multiplication = True
            while reprendre_multiplication:
                reprendre_multiplication = False
                print(f"""
                                 ---------------------------------
                                 | NIVEAU FACILE DU JEU DE MATHS |
                                 ---------------------------------
----------------------------------------
| MODULE 3: CALCULS DE MULTIPLICATIONS |
----------------------------------------
-->Une série de {FNB_QUESTONS} questions avec des combinaisons entre {MIN_FACILE} et {MAX_FACILE}.
""")
                for i in range(1, FNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {FNB_QUESTONS}")
                    if calcul_multiplication(MIN_FACILE, MAX_FACILE):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{FNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_multiplication = True if input("\nReprendre cette partie (o/n)??") == "o".lower() else False
        elif type_calcul == 4:
            reprendre_division = True
            while reprendre_division:
                reprendre_division = False
                print(
                    f"""
                                 ---------------------------------
                                 | NIVEAU FACILE DU JEU DE MATHS |
                                 ---------------------------------
----------------------------------
| MODULE 4: CALCULS DE DIVISIONS |
----------------------------------
-->Une série de {FNB_QUESTONS} questions avec des combinaisons entre {MIN_FACILE} et {MAX_FACILE}.
NB: Pour des calculs de divisions, en cas de réponse décimale, limitez-vous à deux chiffres après la virgule !
                         ( Arrondir le résultat par défaut ou par excès selon les cas )""")
                for i in range(1, FNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {FNB_QUESTONS}")
                    if calcul_division(MIN_FACILE, MAX_FACILE):
                        print("\t\t\tRéponse correcte !")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !")
                print(f"Votre note est: {nb_points}/{FNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_division = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False
        elif type_calcul == 5:
            reprendre_modulo = True
            while reprendre_modulo:
                reprendre_modulo = False
                print(f"""
                                 ---------------------------------
                                 | NIVEAU FACILE DU JEU DE MATHS |
                                 ---------------------------------
--------------------------------
| MODULE 5: CALCULS DE MODULOS |
--------------------------------
-->Une série de {FNB_QUESTONS} questions avec des combinaisons entre {MIN_FACILE} et {MAX_FACILE}.
""")
                for i in range(1, FNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {FNB_QUESTONS}")
                    if calcul_modulo(MIN_FACILE, MAX_FACILE):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{FNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_modulo = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False
        elif type_calcul == 6:
            reprendre_mixte = True
            while reprendre_mixte:
                reprendre_mixte = False
                print(f"""
                                 ---------------------------------
                                 | NIVEAU FACILE DU JEU DE MATHS |
                                 ---------------------------------
----------------------------
| MODULE 6: CALCULS MIXTES |
----------------------------
-->Une série de {FNB_QUESTONS} questions avec des combinaisons entre {MIN_FACILE} et {MAX_FACILE}.
NB: Pour des calculs de divisions, en cas de réponse décimale, limitez-vous à deux chiffres après la virgule !
                         ( Arrondir le résultat par défaut ou par excès selon les cas )
""")
                for i in range(1, FNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {FNB_QUESTONS}")
                    if calcul_mixte(MIN_FACILE, MAX_FACILE):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{FNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_mixte = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False

    elif choix_niveau == 2:

        nb_points = 0
        if type_calcul == 1:
            reprendre_addition = True
            while reprendre_addition:
                reprendre_addition = False
                print(f"""
                                 --------------------------------
                                 | NIVEAU MOYEN DU JEU DE MATHS |
                                 --------------------------------
---------------------------------
| MODULE 1: CALCULS D'ADDITIONS |
---------------------------------
-->Une série de {MNB_QUESTONS} questions avec des combinaisons entre {MIN_MOYEN} et {MAX_MOYEN}.
""")
                for i in range(1, MNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {MNB_QUESTONS}")
                    if calcul_addition(MIN_MOYEN, MAX_MOYEN):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{MNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_addition = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False
        elif type_calcul == 2:
            reprendre_soustration = True
            while reprendre_soustration:
                reprendre_soustration = False
                print(f"""
                                 --------------------------------
                                 | NIVEAU MOYEN DU JEU DE MATHS |
                                 --------------------------------
-------------------------------------
| MODULE 2: CALCULS DE SOUSTRATIONS |
-------------------------------------
-->Une série de {MNB_QUESTONS} questions avec des combinaisons entre {MIN_MOYEN} et {MAX_MOYEN}.
""")
                for i in range(1, MNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {MNB_QUESTONS}")
                    if calcul_soustration(MIN_MOYEN, MAX_MOYEN):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{MNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_soustration = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False
        elif type_calcul == 3:
            reprendre_multiplication = True
            while reprendre_multiplication:
                reprendre_multiplication = False
                print(f"""
                                 --------------------------------
                                 | NIVEAU MOYEN DU JEU DE MATHS |
                                 --------------------------------
----------------------------------------
| MODULE 3: CALCULS DE MULTIPLICATIONS |
----------------------------------------
-->Une série de {MNB_QUESTONS} questions avec des combinaisons entre {MIN_MOYEN} et {MAX_MOYEN}.
""")
                for i in range(1, MNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {MNB_QUESTONS}")
                    if calcul_multiplication(MIN_MOYEN, MAX_MOYEN):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{MNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_multiplication = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False
        elif type_calcul == 4:
            reprendre_division = True
            while reprendre_division:
                reprendre_division = False
                print(f"""
                                 --------------------------------
                                 | NIVEAU MOYEN DU JEU DE MATHS |
                                 --------------------------------
----------------------------------
| MODULE 4: CALCULS DE DIVISIONS |
----------------------------------
-->Une série de {MNB_QUESTONS} questions avec des combinaisons entre {MIN_MOYEN} et {MAX_MOYEN}.
NB: Pour des calculs de divisions, en cas de réponse décimale, limitez-vous à deux chiffres après la virgule !
                         ( Arrondir le résultat par défaut ou par excès selon les cas )""")
                for i in range(1, MNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {MNB_QUESTONS}")
                    if calcul_division(MIN_MOYEN, MAX_MOYEN):
                        print("\t\t\tRéponse correcte !")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !")
                print(f"Votre note est: {nb_points}/{MNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_division = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False
        elif type_calcul == 5:
            reprendre_modulo = True
            while reprendre_modulo:
                reprendre_modulo = False
                print(f"""
                                 --------------------------------
                                 | NIVEAU MOYEN DU JEU DE MATHS |
                                 --------------------------------
--------------------------------
| MODULE 5: CALCULS DE MODULOS |
--------------------------------
-->Une série de {MNB_QUESTONS} questions avec des combinaisons entre {MIN_MOYEN} et {MAX_MOYEN}.
""")
                for i in range(1, MNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {MNB_QUESTONS}")
                    if calcul_modulo(MIN_MOYEN, MAX_MOYEN):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{MNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_modulo = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False
        elif type_calcul == 6:
            reprendre_mixte = True
            while reprendre_mixte:
                reprendre_mixte = False
                print(f"""
                                 --------------------------------
                                 | NIVEAU MOYEN DU JEU DE MATHS |
                                 --------------------------------
----------------------------
| MODULE 6: CALCULS MIXTES |
----------------------------
-->Une série de {MNB_QUESTONS} questions avec des combinaisons entre {MIN_MOYEN} et {MAX_MOYEN}.
NB: Pour des calculs de divisions, en cas de réponse décimale, limitez-vous à deux chiffres après la virgule !
                         ( Arrondir le résultat par défaut ou par excès selon les cas )
""")
                for i in range(1, MNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {MNB_QUESTONS}")
                    if calcul_mixte(MIN_MOYEN, MAX_MOYEN):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{MNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_mixte = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False

    elif choix_niveau == 3:

        nb_points = 0
        if type_calcul == 1:
            reprendre_addition = True
            while reprendre_addition:
                reprendre_addition = False
                print(f"""
                                 ------------------------------------
                                 | NIVEAU DIFFICILE DU JEU DE MATHS |
                                 ------------------------------------
---------------------------------
| MODULE 1: CALCULS D'ADDITIONS |
---------------------------------
-->Une série de {DNB_QUESTONS} questions avec des combinaisons entre {MIN_DIFFICILE} et {MAX_DIFFICILE}.
""")
                for i in range(1, DNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {DNB_QUESTONS}")
                    if calcul_addition(MIN_DIFFICILE, MAX_DIFFICILE):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{DNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_addition = True if input("\nReprendre cette partie (o/n)??") == "o".lower() else False
        elif type_calcul == 2:
            reprendre_soustration = True
            while reprendre_soustration:
                reprendre_soustration = False
                print(f"""
                                 ------------------------------------
                                 | NIVEAU DIFFICILE DU JEU DE MATHS |
                                 ------------------------------------
------------------------------------
| MODULE 2 CALCULS DE SOUSTRATIONS |
------------------------------------
-->Une série de {DNB_QUESTONS} questions avec des combinaisons entre {MIN_DIFFICILE} et {MAX_DIFFICILE}.
""")
                for i in range(1, DNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {DNB_QUESTONS}")
                    if calcul_soustration(MIN_DIFFICILE, MAX_DIFFICILE):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{DNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_soustration = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False
        elif type_calcul == 3:
            reprendre_multiplication = True
            while reprendre_multiplication:
                reprendre_multiplication = False
                print(f"""
                                 ------------------------------------
                                 | NIVEAU DIFFICILE DU JEU DE MATHS |
                                 ------------------------------------
----------------------------------------
| MODULE 3: CALCULS DE MULTIPLICATIONS |
----------------------------------------
-->Une série de {DNB_QUESTONS} questions avec des combinaisons entre {MIN_DIFFICILE} et {MAX_DIFFICILE}.
""")
                for i in range(1, DNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {DNB_QUESTONS}")
                    if calcul_multiplication(MIN_DIFFICILE, MAX_DIFFICILE):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{DNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_multiplication = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False
        elif type_calcul == 4:
            reprendre_division = True
            while reprendre_division:
                reprendre_division = False
                print(
                    f"""
                                 ------------------------------------
                                 | NIVEAU DIFFICILE DU JEU DE MATHS |
                                 ------------------------------------
----------------------------------
| MODULE 4: CALCULS DE DIVISIONS |
----------------------------------
-->Une série de {DNB_QUESTONS} questions avec des combinaisons entre {MIN_DIFFICILE} et {MAX_DIFFICILE}.
NB: Pour des calculs de divisions, en cas de réponse décimale, limitez-vous à deux chiffres après la virgule !
                         ( Arrondir le résultat par défaut ou par excès selon les cas )""")
                for i in range(1, DNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {DNB_QUESTONS}")
                    if calcul_division(MIN_DIFFICILE, MAX_DIFFICILE):
                        print("\t\t\tRéponse correcte !")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !")
                print(f"Votre note est: {nb_points}/{DNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_division = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False
        elif type_calcul == 5:
            reprendre_modulo = True
            while reprendre_modulo:
                reprendre_modulo = False
                print(f"""
                                 ------------------------------------
                                 | NIVEAU DIFFICILE DU JEU DE MATHS |
                                 ------------------------------------
--------------------------------
| MODULE 5: CALCULS DE MODULOS |
--------------------------------
-->Une série de {DNB_QUESTONS} questions avec des combinaisons entre {MIN_DIFFICILE} et {MAX_DIFFICILE}.
""")
                for i in range(1, DNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {DNB_QUESTONS}")
                    if calcul_modulo(MIN_DIFFICILE, MAX_DIFFICILE):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{DNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_modulo = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False
        elif type_calcul == 6:
            reprendre_mixte = True
            while reprendre_mixte:
                reprendre_mixte = False
                print(f"""
                                 ------------------------------------
                                 | NIVEAU DIFFICILE DU JEU DE MATHS |
                                 ------------------------------------
----------------------------
| MODULE 6: CALCULS MIXTES |
----------------------------
-->Une série de {DNB_QUESTONS} questions avec des combinaisons entre {MIN_DIFFICILE} et {MAX_DIFFICILE}.
NB: Pour des calculs de divisions, en cas de réponse décimale, limitez-vous à deux chiffres après la virgule !
                         ( Arrondir le résultat par défaut ou par excès selon les cas )
""")
                for i in range(1, DNB_QUESTONS + 1):
                    print(f"Question N°{i} sur {DNB_QUESTONS}")
                    if calcul_mixte(MIN_DIFFICILE, MAX_DIFFICILE):
                        print("\t\t\tRéponse correcte !\n")
                        nb_points += 1
                    else:
                        print(f"\t\t\tRéponse incorrecte !\n")
                print(f"Votre note est: {nb_points}/{DNB_QUESTONS}")
                appreciation()
                nb_points = 0
                reprendre_mixte = True if input("\nReprendre cette partie (o/n) ?") == "o".lower() else False

    reprendre = True if input("\nReprendre le programme général (o/n)??") == "o".lower() else False
print("""\n
            ------------------------------------------------------------------------------------------------------------------
            |     A        M         E         S         C         O         V         I         T         C         H       |
            ------------------------------------------------------------------------------------------------------------------
                                             |      F I N    D U    P R O G R A M M E      |
                                             -----------------------------------------------
        """)
