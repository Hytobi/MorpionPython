#PLOUVIN Patrice
#8/11/17
#Jeu du tic-tac-toe






HUMAIN = 'X'    #Le symbole de l’humain.
ORDI = 'O'      #Le symbole de l’ordinateur.
VIDE = ' '      #Le symbole de case vide.
T_PLATEAU = 3   #Taille du plateau de jeu



def init_plateau():
    '''Fonction qui créé le plateau initial du jeu où
       toutes les cases sont vides.
       Argument : None
       Retour : liste --- retourne le plateau initial du jeu'''
    plateau=[]
    for i in range(T_PLATEAU):
        a=[]
        for j in range(T_PLATEAU):
            a+=[VIDE]
        plateau+=[a]
    return  plateau

def print_plateau(plateau):
    '''Fonction qui affiche le plateau sous la forme usuelle pour le jeu
       tic-tac-toe.
       Argument : liste --- une liste de liste
       Retour : Affiche le plateau sous la forme usuelle'''
    for i in range(0, len(plateau)):
        for j in range(0, len(plateau[i])):
            if len(plateau[i])-1 != j:
                print(plateau[i][j]+ '|', end='')
            else:
                print(plateau[i][j], end='\n')
        if i != len(plateau)-1:
            print('------')


def input_humain(plateau):
    '''La fonction demande les coordonnées auxquelles le joueur veut
       placer son symbole.
       Argument : liste --- liste de liste
       Retour : Retourn un tuple de deux valeurs contenant les coordonnées choisies par
       l’utilisateur. '''
    terminer = False
    coordonne = []
    while not terminer:
        co_1 = int(input('Entrez la ligne de votre coup : '))
        co_2 = int(input('Entrez la colonne de votre coup : '))
        if co_1>=0 and co_1<T_PLATEAU and co_2>=0 and co_2<T_PLATEAU and plateau[co_1][co_2]==VIDE:
            coordonne = [co_1, co_2]
            terminer = True
        else:
            print('Erreur')
            print()
        if terminer == False :
            q = input('q pour abandonner, c pour continuer : ')
            if q=='q':
                terminer = True
    return coordonne 



        
def coords_vides(plateau):
    '''Cette fonctionretourne une liste de couples correspondant
       aux coordonnées des positions vides sur le plateau.
       Argument : liste --- liste de liste
       Retour : liste de couples'''
    case_vide= []
    for i in range(0, len(plateau)):
        for j in range(0, len(plateau[i])):
            if plateau[i][j] == VIDE:
                case_vide+=[[i, j]]
    return case_vide
        

def input_ordi(plateau):
    '''Fonction qui donne le coup de l'ordi
       Argument : liste --- liste de liste
       Retour : Retourne le coup de l'ordi'''
    from random import randint
    case_vide=coords_vides(plateau)
    if case_vide != []:
        x = randint(0,len(case_vide)-1)
        return case_vide[x]

def est_victoire(symbole,plateau):
    '''Cette fonction doit retourner True
       si le joueur passé en argument a gagné la partie.
       Argument : str --- HUMAIN ou ORDI
                  liste --- liste de liste
       Retour : Retourne True si le joueur a gagné'''
    al1=0          #horrizontale
    al2=0
    al3=0
    var1=0         #verticale
    var2=0
    var3=0
    if symbole=='HUMAIN':
        for j in range(0, len(plateau)):
            if plateau[0][j]==HUMAIN:
                al1+=1
                if al1==3:
                    return True
            elif plateau[1][j]==HUMAIN:
                al2+=1
                if al2==3:
                    return True
            elif plateau[2][j]==HUMAIN:
                al3+=1
                if al3==3:
                    return True
        for i in range(0, len(plateau)):
            if plateau[i][0]==HUMAIN:
                var1+=1
                if var1==3:
                    return True
            elif plateau[i][1]==HUMAIN:
                var2+=1
                if var2==3:
                    return True
            elif plateau[i][2]==HUMAIN:
                var3+=1
                if var3==3:
                    return True
        if al1!=3 and al2!=3 and al3!=3 and var1!=3 and var2!=3 and var3!=3:
            return False
    if symbole=='ORDI':
        for j in range(0, len(plateau)):
            if plateau[0][j]==ORDI:
                al1+=1
                if al1==3:
                    return True
            elif plateau[1][j]==ORDI:
                al2+=1
                if al2==3:
                    return True
            elif plateau[2][j]==ORDI:
                al3+=1
                if al3==3:
                    return True
        for i in range(0, len(plateau)):
            if plateau[i][0]==ORDI:
                var1+=1
                if var1==3:
                    return True
            elif plateau[i][1]==ORDI:
                var2+=1
                if var2==3:
                    return True
            elif plateau[i][2]==ORDI:
                var3+=1
                if var3==3:
                    return True
        if al1!=3 and al2!=3 and al3!=3 and var1!=3 and var2!=3 and var3!=3:
            return False


def joue_partie():
    '''Fonction qui met en marche le jeu
       Argument : None
       Retour : None'''
    fin = False
    plateau = init_plateau()
    print_plateau(plateau)
    while not fin :
        coup = input_humain(plateau)
        plateau[coup[0]][coup[1]]=HUMAIN
        print_plateau(plateau)
        x = est_victoire('HUMAIN',plateau)
        if x == True:
            print("Bravo vous avez gagné !")
            fin = True
        else:
            print()
            print("L'ordi a joué : ")
            coup_ordi = input_ordi(plateau)
            plateau[coup_ordi[0]][coup_ordi[1]]=ORDI
            print_plateau(plateau)
            k = est_victoire('ORDI',plateau)
            if k == True:
                print("Vous avez perdu !")
                fin = True
        print()
        print()



def input_rejouer():
    '''La fonction demande a l'utilisateur s'il veut rejouer
       Argument : None
       Retour : True si oui, False sinon'''
    partir = False
    while not partir :
        rejouer = input("voulez vous rejouer ? 1.oui, 2.non : ")
        if rejouer=='1':
            return True
        elif rejouer=='2':
            return False
        else:
            print("Entrer invalide")




def main():
    '''La fonction est la fonction principal du jeu
       Argument : None
       Retour : le jeu'''
    print("Vous ne pouvez gagner que en ligne ou en colonne, pas en diagonale")
    fini = False
    while not fini :
        joue_partie()
        x = input_rejouer()
        if x==False :
            fini = True









