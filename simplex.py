"""
        ----------Objectif du Programme ""

 ce programme permet de résoudre des problèmes de maximisation ou minimisation et aussi 
 de déterminer la valeur de la fonction objectif (fonction économique Z ) 
 en utilisant la méthode simplex .

                   #Dépendance #

               python 3.X ,numpy , installer numpy en ouvrant un terminal

                  pip install nump

                    # utilisation #

           python simplex.py       windows

           python3 simplex.py     GNU/LINUX                         
"""
import sys #on va intéragir avec le système,donc on importe le système
import numpy as np # numpy librairie destinée à manipuler des matrices ou des tableaux ainsi que des fonctions mathématiques opérant sur des tableaux..
                   # numpy va retourner un array (une variable spéciale pouvant contenir plusieurs valeurs à la fois donc un tableau ) --- np

#  on démarre une liste vide [], puis  on utilise la fonction append() ou extend() pour y ajouter des éléments:
# le programme utilise que des boucles for,while ...aucune fonction spécial à part append(),range()
noms_des_produits = []      
noms_des_contraintes = []
valeurs_des_colones = []
equation_de_z = []         
final_rows = []
solutions = []
x = 'X'                # x= X pour ne pas utiliser x,y ainsi que e ,donc nous aurons X1,X2 .......Xn
equation_de_z2 = []
variables_suprimer = []

def main():                  
    global nombre_des_produits, nombre_des_contraintes 
    print("""
               #######################################################################|
               |     Coding By Hakanonymos                                            |
               |     sous la direction du  Professeur X  :                            | 
               |                                                                      |   
               |             département informatique , Réseaux et Télécommunication. |
               |                                                                      |
               ########################################################################

 Avant de commencer,quel type de problème voulez-vous résoudre ?	
    1 :maximisation ( <= ).
    2 :minimisation ( >= ).
 
    0 : Aide.

    """)
       
    try:        # try permet de gérer les erreurs au cas où l'utilisateur ne respecte pas les normes du programme
        type_du_problem = int(input(" Entrez le numéro du problème: >")) # l'utilisateur doit tapper un nombre entier positif
    except:                                                             # exception pour les erreurs puis afficher un message à l'utilisateur
        print("s'il vous plaît choisissez un numéro ")
        type_du_problem = int(input(" Entrez le numéro du problème: >")) # on lui donne une chance de choisir un numéro
  
    if type_du_problem != 2 and type_du_problem != 1 and type_du_problem != 0:  # si l'utilisateur n'a pas choisit le numéro 0 ou 1 ou 2
        sys.exit("vous avez choisi un mauvais choix du problème ->" + str(type_du_problem)) #le programme s'arrete avec ce message + le numéro choisi  
    if type_du_problem == 0: # si l'utilisateur a choisi la valeur de 0, il verra un méssage d'aide
        print(r"""
        --Aide:
        Résolution de n'importe quel problème par la méthode simplex
        
        ----- Exemple d'1 Problème -----
           
       Une entreprise E1 a la faculté de fabriquer  n biens de coût unitaire Cj ; j=1...n, à partir de m ressources
      de disponibilités respectives b1 , b2 , .., bm . Pour fabriquer une unité du bien numéro j on a besoin de :
        a1j de la ressource numéro 1 , a2j de la ressource numéro 2
            .
            .
            .amj de la ressource numéro m

        * Question : L’entreprise E1 se demande comment organiser sa production ( quantité de bien à fabriquer de manière à maximiser son revenu )
               
                       
         ----------Résolution par le programme python-------

         1) combien des produits voulez-vous fabriquer ? 2 ou 3.......N à vous d'écrire le nombre
         2) combien de contraintes avez-vous ? , 2 ou 3 .......N à vous d'écrire le nombre de contrainte
         3) définissez les noms de contrainte pour mieux organiser les données,exemple nom1,nom2 ......nomM
         4) cette étape, nous allons écrire l'équation de la fonction économique (Z fonction objéctive )
             Soit X1 la quantité du bien numéro 1 à fabriquer
                  X2 la quantité du bien numéro 2 à fabriquer
                  Xn  la quantité du bien numéro N à fabriquer

                Z = C1X1 + C2X2 + ... + CnXn          
             
              vous allez écrire le coût unitaire associé au bien numéo 1 , C1
                                                 associé au bien numéro 2, C2
                                                 associé au bien numéro N , Cn
               ai1x1 + ai2x2 + ... + ainxn

          5) l'équation donne combien ?

                ici il s'agit de déterminer la disponibilité de chaque réssource

              ici vous allez déterminer b1, pour l'équation 1
                                         b2, pour l'équation 2
                                         bm, pour l'équation m
            ai1X1 + ai2X2 + ... + ainXn ,

           D’où les contraintes :

          somme de (ai1X1 + ai2X2 + ... + ainXn ) <= b1
                   .
                  am1X1 + am2X2 + ........ +amnXn ≤ bm

        6) Vous aurez votre tableau simplex avec les solutions admissibles .
                 
        """)
        sys.exit() # le programme s'arrete et on sort de la condition if type_problème = 0

    print('\n##########################################')
    nombre_des_produits = int(input("combien des produits voulez-vous fabriquer ?: >")) # combien des produits fabrique l'entreprise ?
    nombre_des_contraintes = int(input("combien de contraintes avez-vous ?: >")) 

    #Lorsque l’on souhaite répéter un nombre donné de fois la même instruction ou le même bloc d’instructions,
    # la commande for est la plus appropriée.
    for i in range(1, nombre_des_produits + 1): 
        val = x + str(i)                         
        noms_des_contraintes.append(val)        #la fonction append() a été défini en haut

    for i in range(1, nombre_des_contraintes + 1): #
        valeur_produit = input("le nom du contrainte numéro %d : >" % i)
        noms_des_produits.append(valeur_produit)
    print("_______________________________________________________________")

   # Soit xj la quantité du bien numéro j, j= 1....n, à fabriquer. Soit z le revenu de l’entreprise.
   # Alors Z = C1x1 + C2x2 + ... + Cnxn ( fonction objective )
  
    if type_du_problem == 1:    # l'utlisateur choisit la maximisation
        for i in noms_des_contraintes:
            try:
                val = float(input("le coût unitaire associé à %s dans la fonction objectif( Z ): >" % i)) 
            except:                # le coût unitaire de la resssource numéro j, j allant de 1......n
                print("s'il vous plaît entrez un numéro")
                val = float(input("le coût unitaire associé à %s dans la fonction objectif( Z ): >" % i))
            equation_de_z.append(0 - float(val))
        equation_de_z.append(0)

        while len(equation_de_z) <= (nombre_des_produits + nombre_des_contraintes):
            equation_de_z.append(0)
        print("________________________________________________________________")
        
        """
   Quelle est la contribution de la ressource numéro i, i=1....m ?

  ai1x1 + ai2x2 + ... + ainxn ,

   D’où les contraintes :

     somme de ai1x1 + ai2x2 + ... + ainxn <= bi
"""      
        for prod in noms_des_produits:
            for const in noms_des_contraintes:
                try:
                    val = float(input("quelle est la contrainte de %s dans %s ? >" % (const, prod)))
                except:
                    print("Assurez-vous d'avoir entré un numéro")
                    val = float(input("quelle est la contrainte de %s dans %s ? >" % (const, prod)))
                valeurs_des_colones.append(val)
            equate_prod = float(input('Equation donne combien ? %s : >' % prod)) #le système d'équation somme de ai1x1 + ai2x2 + ... + ainxn <= bi
            valeurs_des_colones.append(equate_prod)
  
        colones_final = stdz_rows(valeurs_des_colones) # on démare la méthode simplex et on insère des valeurs
        i = len(noms_des_contraintes) + 1
        while len(noms_des_contraintes) < len(colones_final[0]) - 1:
            noms_des_contraintes.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' Z')
        noms_des_contraintes.append('Solution')
        colones_final.append(equation_de_z)
        cols_vals = np.array(colones_final) # np a été défini en haut
        a = 0
        for _ in equation_de_z:
            row = cols_vals[:, a]
            row = row.tolist()
            final_rows.append(row)
            a += 1
        print('\n##########################################')
        maximization(colones_final, final_rows)



    elif type_du_problem == 2:    # l'utilisateur choisit la minimisation 
        for i in noms_des_contraintes:
            try:
                val = float(input("la valeur de %s dans l'équation de Z (fonctiction objectif): >" % i))
            except:
                print("s'il vous plait entrez un numéro")
                val = float(input("la valeur de %s dans l'equation de Z (fonction objectif ): >" % i))
            equation_de_z.append(val)
        equation_de_z.append(0)

        while len(equation_de_z) <= (nombre_des_produits + nombre_des_contraintes):
            equation_de_z.append(0)
        print("________________________________________________________________")
        for prod in noms_des_produits:
            for const in noms_des_contraintes:
                try:
                    val = float(input("quelle est la contrainte de %s dans --> %s ? >" % (const, prod)))
                except:
                    print("s'il vous plaît Assurez-vous d'avoir entré un numero")
                    val = float(input("le cout unitaire associé à %s dans %s: >" % (const, prod)))
                valeurs_des_colones.append(val)
            equate_prod = float(input('Equation donne combien ? %s : >' % prod))
            valeurs_des_colones.append(equate_prod)

        # on démare le tableau de simplex  
       #on peut distinguer trois blocs. 
       #D’abord la fonction objective sur la première ligne.
       #Ensuite, un système d’équation linéaire (de type Ax = b) correspondant à l’ensemble des contraintes du
      #programme, finalement les contraintes de positivités des variables. Remarquons ensuite que les variables
      #sont indexées de 1 à n et qu’on a mis chacune sur une colonne néanmoins la première colonne est réservée
      #aux variables de la base (J + (X0 )). De plus la dernière colonne du tableau est réservée aux valeurs des
      #variables dans la base et la dernière ligne du tableau aux coefficients de la fonction objectives(δj ). Ainsi,
      #on peut garder uniquement le coefficient et la colonne sans mentionner la variable sur chaque ligne. On
      #obtient ainsi le tableau du simplexe correspondant .


        colones_final = stdz_rows2(valeurs_des_colones)
        i = len(noms_des_contraintes) + 1
        while len(noms_des_contraintes) < nombre_des_contraintes + nombre_des_produits:
            noms_des_contraintes.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' Z')
        solutions[:] = []
        add_from = len(noms_des_contraintes)+1
        while len(noms_des_contraintes) < len(colones_final[0][:-1]):
            variables_suprimer.append('X' + str(add_from))
            noms_des_contraintes.append('X' + str(add_from))
            add_from += 1
        variables_suprimer.append(' Z')
        variables_suprimer.append('Z1')
        noms_des_contraintes.append('Solution')
        for ems in variables_suprimer:
            solutions.append(ems)
        while len(equation_de_z) < len(colones_final[0]):
            equation_de_z.append(0)
        colones_final.append(equation_de_z)
        colones_final.append(equation_de_z2)
        cols_vals = np.array(colones_final)
        a = 0
        for _ in equation_de_z:
            row = cols_vals[:, a]
            row = row.tolist()
            final_rows.append(row)
            a += 1
        print('\n##########################################')
        minimization(colones_final, final_rows)

        pass
    else:
        sys.exit("vous avez fait un mauvais choix du problème recommencez->" + str(type_du_problem))


def maximization(colones_final, final_rows):
    row_app = []
    final_new_row = []
    derniere_colone = colones_final[-1]
    min_derniere_colone = min(derniere_colone)
    min_manager = 1
    print(" TABLEAU 1")
    print('  ', noms_des_contraintes)
    i = 0
    for cols in colones_final:
        print(solutions[i], cols)
        i += 1
    count = 2
    while min_derniere_colone < 0 and min_manager == 1:
        print("*********************************************************")
        derniere_colone = colones_final[-1]
        last_row = final_rows[-1]
        min_derniere_colone = min(derniere_colone)
        index_of_min = derniere_colone.index(min_derniere_colone)
        pivot_row = final_rows[index_of_min]
        index_pivot_row = final_rows.index(pivot_row)
        row_div_val = []
        i = 0
        for _ in last_row[:-1]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        element_du_pivot = pivot_row[index_min_div_val]
        colones_du_pivot = colones_final[index_min_div_val]
        index_colones_du_pivot = colones_final.index(colones_du_pivot)
        row_app[:] = []
        index_pivot_elem = colones_du_pivot.index(element_du_pivot)
        for col in colones_final:
            if col is not colones_du_pivot and col is not colones_final[-1]:
                form = col[index_pivot_elem] / element_du_pivot
                i = 0
                for elem in col:
                    value = (elem - float(form * colones_du_pivot[i]))
                    row_app.append(round(value, 2))
                    i += 1
            elif col is colones_du_pivot:
                for elems in colones_du_pivot:
                    value = float(elems / element_du_pivot)
                    row_app.append(round(value, 2))
            else:
                form = abs(col[index_pivot_elem]) / element_du_pivot
                i = 0
                for elem in col:
                    value = elem + float(form * colones_du_pivot[i])
                    row_app.append(round(value, 2))
                    i += 1

        colones_final[:] = []
        final_new_row[:] = []
        final_new_row = [row_app[x:x + len(equation_de_z)] for x in range(0, len(row_app), len(equation_de_z))]
        for list_el in final_new_row:
            colones_final.append(list_el)
        cols_vals = np.array(colones_final)
        a = 0
        final_rows[:] = []
        for _ in equation_de_z:
            row = cols_vals[:, a]
            row = row.tolist()
            final_rows.append(row)
            a += 1
        if min(row_div_val) != 10000000000:
            min_manager = 1
        else:
            min_manager = 0
        print('éléments du pivot: %s' % element_du_pivot)
        print('colone du pivot: ', pivot_row)
        print(' ', colones_du_pivot)
        print("\n")
        solutions[index_colones_du_pivot] = noms_des_contraintes[index_pivot_row]

        print(" TABLEAU %d " % count)
        print('  ', noms_des_contraintes)
        i = 0
        for cols in colones_final:
            print(solutions[i], cols)
            i += 1
        derniere_colone = colones_final[-1]
        min_derniere_colone = min(derniere_colone)
        count += 1


def minimization(colones_final, final_rows):
    row_app = []
    final_new_row = []
    derniere_colone = colones_final[-1]
    min_derniere_colone = min(derniere_colone)
    min_manager = 1
    print(" TABLEAU 1")
    print('  ', noms_des_contraintes)
    i = 0
    for cols in colones_final:
        print(solutions[i], cols)
        i += 1
    count = 2
    while min_derniere_colone < 0 and min_manager == 1:
        print("*********************************************************")
        derniere_colone = colones_final[-1]
        last_row = final_rows[-1]
        min_derniere_colone = min(derniere_colone[:-1])
        index_of_min = derniere_colone.index(min_derniere_colone)
        pivot_row = final_rows[index_of_min]
        index_pivot_row = final_rows.index(pivot_row)
        row_div_val = []
        i = 0
        for _ in last_row[:-2]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        element_du_pivot = pivot_row[index_min_div_val]
        colones_du_pivot = colones_final[index_min_div_val]
        index_colones_du_pivot = colones_final.index(colones_du_pivot)
        row_app[:] = []
        index_pivot_elem = colones_du_pivot.index(element_du_pivot)
        for col in colones_final:
            if col is not colones_du_pivot and col is not colones_final[-1]:
                form = col[index_pivot_elem] / element_du_pivot
                i = 0
                for elem in col:
                    value = (elem - float(form * colones_du_pivot[i]))
                    row_app.append(round(value, 2))
                    i += 1
            elif col is colones_du_pivot:
                for elems in colones_du_pivot:
                    value = float(elems / element_du_pivot)
                    row_app.append(round(value, 2))
            else:
                form = abs(col[index_pivot_elem]) / element_du_pivot
                i = 0
                for elem in col:
                    value = elem + float(form * colones_du_pivot[i])
                    row_app.append(round(value, 2))
                    i += 1
        equals = len(colones_final[0])
        colones_final[:] = []
        final_new_row[:] = []
        final_new_row = [row_app[x:x + equals] for x in range(0, len(row_app), equals)]
        for list_el in final_new_row:
            colones_final.append(list_el)
        cols_vals = np.array(colones_final)
        a = 0
        final_rows[:] = []
        try:
            for _ in equation_de_z:
                row = cols_vals[:, a]
                row = row.tolist()
                final_rows.append(row)
                a += 1
        except:
            pass
        if min(row_div_val) != 10000000000:
            min_manager = 1
        else:
            min_manager = 0
        print('éléments du pivot: %s' % element_du_pivot)
        print('colone du pivot: ', pivot_row)
        print('', colones_du_pivot)
        print("\n")
        removable = solutions[index_colones_du_pivot]
        solutions[index_colones_du_pivot] = noms_des_contraintes[index_pivot_row]
        if removable in variables_suprimer:
            idex_remove = noms_des_contraintes.index(removable)
            for colms in colones_final:
                colms.remove(colms[idex_remove])
            noms_des_contraintes.remove(removable)
        print("TABLEAU %d" % count)
        print('  ', noms_des_contraintes)
        i = 0
        for cols in colones_final:
            print(solutions[i], cols)
            i += 1
        derniere_colone = colones_final[-1]
        min_derniere_colone = min(derniere_colone)
        count += 1
        cols_vals = np.array(colones_final)
        a = 0
        final_rows[:] = []
        try:
            for _ in equation_de_z:
                row = cols_vals[:, a]
                row = row.tolist()
                final_rows.append(row)
                a += 1
        except:
            pass


def stdz_rows2(column_values):
    colones_final = [column_values[x:x + nombre_des_produits + 1] for x in range(0, len(column_values), nombre_des_produits + 1)]
    b = 0
    for _ in colones_final[0]:
        z_sum = 0
        for row in colones_final:
            z_sum = row[b] + z_sum
        equation_de_z2.append(0 - z_sum)
        b += 1

    for cols in colones_final:
        while len(cols) < (nombre_des_produits + (2*nombre_des_contraintes)-1):
            cols.insert(-1, 0)


    i= nombre_des_produits
    for sub_col in colones_final:
        sub_col.insert(i, -1)
        equation_de_z2.insert(-1, 1)
        i += 1

    for sub_col in colones_final:
        sub_col.insert(i, 1)
        i += 1
    while len(equation_de_z2) < len(colones_final[0]):
        equation_de_z2.insert(-1, 0)

    return colones_final


def stdz_rows(column_values):
    colones_final = [column_values[x:x + nombre_des_produits + 1] for x in range(0, len(column_values), nombre_des_produits + 1)] 
    for cols in colones_final:
        while len(cols) < (nombre_des_produits + nombre_des_contraintes):
            cols.insert(-1, 0)

    i = nombre_des_produits
    for sub_col in colones_final:
        sub_col.insert(i, 1)
        i += 1
    return colones_final

if __name__ == "__main__":
    main()


                                                  #Réference
 

#https://www.numpy.org/devdocs/reference/generated/numpy.matrix.max.html

#https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.maximum.html

#https://www.hackerrank.com/challenges/np-min-and-max/problem

#https://developers.google.com/edu/python/lists

#https://www.developpez.net/forums/d876840/autres-langages/python-zope/calcul-scientifique/maximisation-fonction-somme-plusieurs-variable/

#https://www.programiz.com/python-programming/methods/list/append

#https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/234239-un-peu-de-programmation-systeme

#https://www.geeksforgeeks.org/max-min-python/

#http://informathix.tuxfamily.org/?q=node/109




