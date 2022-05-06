import pygame as pg



pg.init()
infoecran= pg.display.Info()


class Pieces:
    """
    Une sorte de classe abstraite, elle sert uniquement de modèle pour l'héritage des autres pièces
    Cette classe crée des objets Pièces ayant comme attributs:
    - une couleur : Blanc ou Noir
    - un nom
    - une position sur l'écran
    - un nom sous forme d'entier -1 1 ... (permet de manipuler plus 'facilement' les pièces que par leur nom).
    """
    nombreInstances = 0
    
    def __init__(self, nom: str, couleur: str, position, nomInt: int):
        self.couleur = couleur
        assert couleur == "Blanc" or couleur == "Noir"
        self.nom = nom
        self.position = position
        self.nomInt = nomInt
        Pieces.nombreInstances += 1
        self.taille_case = infoecran.current_h/8
        
    #accesseurs
    def getNom(self) -> str:
        return self.nom
    def getCouleur(self):
        return self.couleur
    def getPosition(self):
        return self.position
    def getNombreInstances(self):
        return Pieces.nombreInstances 
    def getNomInt(self):
        return self.nomInt
    
    def getTaille_case(self):
        return self.taille_case

    def getPosx(self):
        return self.position[0]

    def getPosy(self):
        return self.position[1]

    def getPos(self):
        return self.position
    
    def setNom(self, nouveauNom: str) -> None:
        self.nom = nouveauNom
    
    def __str__(self):
        return self.nom 

    def __del__(self):
        Pieces.nombreInstances -= 1

class Pions(Pieces):
    
    nombreInstances = 0
    
    def __init__(self, numero, estBlanc: bool, position: tuple):
        """
        Les constructeurs des classes de chaque pièce (comme ici le pion) appellent le constructeur de la classe abstraite Pieces
        et ajoute chacun un attribut: le numéro de la pièce.
    
        La variable statique Pions.nombreInstances sert à connaître le nombre de pièces du type demandé présentent sur le plateau, ce qui permet d'éviter des bugs et nous aide dans la conception des algorithmes.
    
        """
    
    
    
        if numero > 8:
            print("Le pion ne peut pas être plus que le 8e !!!!!!!")
            raise Exception
        self.numero = numero
        Pions.nombreInstances += 1
        super().__init__(nom = "pion", couleur="Blanc" if estBlanc else "Noir", position=position, nomInt=1 if estBlanc else -1 )
        
    #accesseur
    def getNom(self):
        return super().getNom()+" "+ self.couleur + str(self.numero)
    
    def getNombreInstances(self):
        return Pions.nombreInstances

    def getPos(self):
        return  self.position

    def setPos(self,pos):
        self.position = pos
        
    
    def deplacements_possibles(self, tour, partie):
        """
        args
        ---------
        tour (int) : le tour actuel de la partie
        partie (Partie): un objet de type partie (définie dans le fichier Partie.py) qui représente la partie en cours.
    
        returns
        ---------
        dp (list[tuple]) : la position de tous les déplacements possibles sauf le roi (roi immangeable)
        ma (list[tuple]): la position de toutes les pièces qui peuvent être mangées
        pRcR (list[tuple]): la position du roi adverse mangeable si cela est possible => ne sert à rien dans la version rendue pour le concours des trophées NSI puisque l'algorithme de calcul des déplacements possibles dans le cas où le roi est en échec n'a pas été produit.
        
        explication de l'algorithme
        ---------
        Cette méthode sert à calculer tous les déplacements possibles du pion.
        
        L'algorithme implémenté fonctionne de la manière suivante:
        
            -- on définit des lambdas (fonctions anonymes sur une seule ligne) représentant d'un côté les déplacements "pacifiques" possibles et d'un autre les déplacements où l'on mange une pièce. Ces lambdas donnent pour chaque position (x, y) une position future potentielle
            -- ensuite on répete chaque lambda jusqu'à qu'une contrainte se présente (un obstacle ou la sortie du plateau)
            
        """
        t = self.taille_case
        dp, ma, pRcR = [], [], []
        fd = {"Blanc": lambda x, y: (x, y-t), "Noir": lambda x, y: (x, y+t)}
        fm = {"Blanc": [lambda x, y: (x-t, y-t), lambda x, y: (x+t, y-t)],
                "Noir": [lambda x, y: (x-t, y+t), lambda x, y: (x+t, y+t)]}
        
        x, y = self.position
        b = True
        if (self.position[1] == t+t/2 and self.couleur == "Noir") or  (self.position[1] == 6*t+t/2 and self.couleur == "Blanc") or tour == 1:
            for i in range(2):
                x, y = fd[self.couleur](x, y)
                if partie.getPiece((x, y)) != 0:
                    break
                else:
                    dp.append((x, y))
            b = False
        for e in fm[self.couleur]:
            x, y = self.position
            x, y = e(x, y)
            if abs(partie.getPiece((x, y))) == 6:
                pRcR.append((x, y))
            elif (partie.getPiece((x, y)) > 0 and self.couleur == "Noir") or (partie.getPiece((x, y)) < 0 and self.couleur == "Blanc"):
                ma.append((x, y))
                dp.append((x, y))
        x, y = self.position
        if b:
            x, y = fd[self.couleur](x, y)
            if partie.getPiece((x, y)) == 0:
                dp.append((x, y))
        return dp, ma, pRcR


class Tour(Pieces):
    nombreInstances = 0

    # constructeur
    def __init__(self, numero: int, estBlanc: bool, position: list):
        self.numero = numero
        Tour.nombreInstances += 1
        super().__init__(nom='tour', couleur="Blanc" if estBlanc else 'Noir',
                         position=position, nomInt=4 if estBlanc else -4)

    # accesseurs
    def getNumero(self) -> int:
        return self.numero

    def getNom(self) -> str:
        return super().getNom() +" "+ self.couleur + str(self.numero)

    def getNombreInstances(self):
        return Tour.nombreInstances
    def getNomInt(self):
        return self.nomInt
    # mutateurs
    def setNumero(self, n: int) -> None:
        self.numero = n

    def setPos(self,pos):
        self.position = pos
    # méthodes

    def deplacements_possibles(self, tour, partie):
        """
        args
        ---------
        tour (int) : le tour actuel de la partie
        partie (Partie): un objet de type partie (définie dans le fichier Partie.py) qui représente la partie en cours.
    
        returns
        ---------
        deplacementsPossibles (list[tuple]) : la position de tous les déplacements possibles sauf le roi (roi immangeable)
        mangeable (list[tuple]): la position de toutes les pièces qui peuvent être mangées
        pourLeRoiCurieux (list[tuple]): la position du roi adverse mangeable si cela est possible => ne sert à rien dans la version rendue pour le concours des trophées NSI puisque l'algorithme de calcul des déplacements possibles dans le cas où le roi est en échec n'a pas été produit.
        
        explication de l'algorithme
        ---------
        Cette méthode sert à calculer tous les déplacements possibles de la tour.
        
        L'algorithme implémenté fonctionne de la manière suivante:
        
            -- on définit des lambdas (fonctions anonymes sur une seule ligne) représentant les déplacements possibles d'une case . Ces lambdas donnent pour chaque position (x, y) une position future potentielle.
            -- ensuite on répete chaque lambda jusqu'à qu'une contrainte se présente (un obstacle ou la sortie du plateau)
            
        """
        t = self.taille_case

        f = [lambda x, y: (x + t, y),
             lambda x, y: (x - t, y),
             lambda x, y: (x, y + t),
             lambda x, y: (x, y - t)]
        deplacementsPossibles = []
        mangeable = []
        pourLeRoiCurieux = []

        def verif(x, y):
            if (partie.getPiece([x, y]) == 6 and self.couleur == "Noir") or (
                    partie.getPiece([x, y]) == -6 and self.couleur == "Blanc"):
                 
                pourLeRoiCurieux.append((y, x))
                return False
            
            elif (partie.getPiece((x, y)) > 0 and self.couleur == "Noir") or (
                    partie.getPiece((x, y)) < 0 and self.couleur == "Blanc"):
                mangeable.append((x, y))
                deplacementsPossibles.append((x, y))
                return False
           
            elif partie.getPiece((x, y)) == 0:
                deplacementsPossibles.append((x, y))
                return True
            else:
                return False

        x, y = self.position
        while x < 7 * t:
            x, y = f[0](x, y)
            if not verif(x, y):
                break

        x, y = self.position
        while x > t:
            x, y = f[1](x, y)
            if not verif(x, y): break

        x, y = self.position
        while y < 7 * t:
            x, y = f[2](x, y)
            if not verif(x, y): break

        x, y = self.position
        while y > t:
            x, y = f[3](x, y)
            if not verif(x, y): break



        return deplacementsPossibles, mangeable, pourLeRoiCurieux


class Cavalier(Pieces):
    nombreInstances = 0

    def __init__(self, numero: int, estBlanc: bool, position: list):
        self.numero = numero
        Cavalier.nombreInstances += 1
        super().__init__(nom="cavalier", couleur="Blanc" if estBlanc else "Noir",
                         position=position, nomInt=2 if estBlanc else -2)

    # accesseurs
    def getNom(self) -> str:
        return super().getNom() +" "+ self.couleur + str(self.numero)

    def getNumero(self) -> int:
        return self.numero

    def getNombreInstances(self) -> int:
        return Cavalier.nombreInstances

    # mutateurs
    def setNumero(self, n: int) -> None:
        self.numero = n

    def setPos(self,pos):
        self.position = pos

    def deplacements_possibles(self,tour,partie):
        """
        args
        ---------
        tour (int) : le tour actuel de la partie
        partie (Partie): un objet de type partie (définie dans le fichier Partie.py) qui représente la partie en cours.
    
        returns
        ---------
        deplacementsPossibles (list[tuple]) : la position de tous les déplacements possibles sauf le roi (roi immangeable)
        mangeable (list[tuple]): la position de toutes les pièces qui peuvent être mangées
        pourLeRoiCurieux (list[tuple]): la position du roi adverse mangeable si celà est possible => ne sert à rien dans la version rendue pour le concours des trophées NSI puisque l'algorithme de calcul des déplacements possibles dans le cas où le roi est en échec n'a pas été produit.
        
        explication de l'algorithme
        ---------
        Cette méthode sert à calculer tous les déplacements possibles du Cavalier.
        
        L'algorithme implémenté fonctionne de la manière suivante:
            -- Les déplacements possibles du Cavalier étant plutôt simples à définir, on définit tous les cas potentiels directement
            -- ensuite on trie toutes les possibilités en vérifiant qu'on ne dépasse pas le plateau ou qu'on ne se déplace pas sur une autre pièce, et si il y a une autre pièce adverse, alors on peut la manger.
            
            
        """
        deplacementsPotentiels = []
        deplacementsPossibles = []
        mangeables = []
        pourLeRoiCurieux = []
        t= self.taille_case

        if tour == 1:
            n = 1 if self.couleur == "Noir" else -1
            deplacementsPossibles.append((self.position[0] +t, self.position[1] + (2*t*n)))
            deplacementsPossibles.append((self.position[0] -t, self.position[1] + (2*t*n)))


        else:
            deplacementsPotentiels.append((self.position[0] - 2*t, self.position[1] + 1*t))
            deplacementsPotentiels.append((self.position[0] - 2*t, self.position[1] - 1*t))
            deplacementsPotentiels.append((self.position[0] + 2*t, self.position[1] + 1*t))
            deplacementsPotentiels.append((self.position[0] + 2*t, self.position[1] - 1*t))
            deplacementsPotentiels.append((self.position[0] - 1*t, self.position[1] - 2*t))
            deplacementsPotentiels.append((self.position[0] - 1*t, self.position[1] + 2*t))
            deplacementsPotentiels.append((self.position[0] + 1*t, self.position[1] - 2*t))
            deplacementsPotentiels.append((self.position[0] + 1*t, self.position[1] + 2*t))
        for e in deplacementsPotentiels:
            if e[0] < 8*t and e[0] > 0 and e[1] < 8*t and e[1] > 0:
                a = partie.getPiece(e)
                if a < 0 and self.couleur == "Blanc" and abs(a) != 6:
                    mangeables.append(e)
                    deplacementsPossibles.append(e)
                elif a > 0 and self.couleur == "Noir" and abs(a) != 6:
                    mangeables.append(e)
                    deplacementsPossibles.append(e)
                elif a == 0:
                    deplacementsPossibles.append(e)
                elif abs(a) == 6:
                    pourLeRoiCurieux.append(e)

        return (deplacementsPossibles, mangeables, pourLeRoiCurieux)


class Fou(Pieces):
    nombresInstances = 0

    def __init__(self, numero: int, estBlanc: bool, position: tuple or list):
        self.numero = numero
        Fou.nombreInstances += 1
        super().__init__(nom="fou", couleur="Blanc" if estBlanc else "Noir",
                         position=position, nomInt=3 if estBlanc else -3)

    # accesseurs
    def getNom(self) -> str:
        return super().getNom() +" "+ self.couleur + str(self.numero)

    def getNumero(self) -> int:
        return self.numero

    def getNombreInstances(self) -> int:
        return Fou.nombreInstances

    def setPos(self,pos):
        self.position = pos

    # mutateurs
    def setNumero(self, n: int) -> None:
        self.numero = n

    def deplacements_possibles(self,tour,partie):
        """
        args
        ---------
        tour (int) : le tour actuel de la partie
        partie (Partie): un objet de type partie (définie dans le fichier Partie.py) qui représente la partie en cours.
    
        returns
        ---------
        deplacementsPossibles (list[tuple]) : la position de tous les déplacements possibles sauf le roi (roi immangeable)
        mangeable (list[tuple]): la position de toutes les pièces qui peuvent être mangées
        pourLeRoiCurieux (list[tuple]): la position du roi adverse mangeable si celà est possible => ne sert à rien dans la version rendue pour le concours des trophées NSI puisque l'algorithme de calcul des déplacements possibles dans le cas où le roi est en échec n'a pas été produit.
        
        explication de l'algorithme
        ---------
        Cette méthode sert à calculer tous les déplacements possibles de le fou.
        
        L'algorithme implémenté fonctionne de la manière suivante:
        
            -- on définit des lambdas (fonctions anonymes sur une seule ligne) représentant les déplacements possibles d'une case . Ces lambdas donnent pour chaque position (x, y) une position future potentielle.
            -- ensuite on répete chaque lambda jusqu'à qu'une contrainte se présente (un obstacle ou la sortie du plateau)
            
        """
        t = self.taille_case
        f1 = lambda x, y: (x + 1*t, y - 1*t)
        f2 = lambda x, y: (x - 1*t, y - 1*t)
        f3 = lambda x, y: (x + 1*t, y + 1*t)
        f4 = lambda x, y: (x - 1*t, y + 1*t)

        deplacementsPotentiels = []
        mangeables = []
        pourLeRoiCurieux = []
        x, y = self.position

        while y > 1*t and x < 7*t:
            x, y = f1(x,y)
            if (partie.getPiece([x, y]) == 6 and self.couleur == "Noir") or (partie.getPiece([x, y]) == -6 and self.couleur == "Blanc"):
                pourLeRoiCurieux.append((x, y))
                break
            if partie.getPiece([x, y])> 0 and self.couleur == "Noir":
                mangeables.append((x, y))
                deplacementsPotentiels.append((x, y))
                break
            elif partie.getPiece([x, y]) < 0 and self.couleur == "Blanc":
                mangeables.append((x, y))
                deplacementsPotentiels.append((x, y))
                break
            elif partie.getPiece([x, y]) > 0 and self.couleur == "Blanc":
                break
            elif partie.getPiece([x, y]) < 0 and self.couleur == "Noir":
                break
            else:
                deplacementsPotentiels.append((x, y))

        x, y = self.position
        while y > 1*t and x > 1*t:
            x, y = f2(x, y)
            if (partie.getPiece([x, y]) == 6 and self.couleur == "Noir") or (partie.getPiece([x, y]) == -6 and self.couleur == "Blanc"):
                pourLeRoiCurieux.append((x, y))
                break
            if partie.getPiece([x, y]) > 0 and self.couleur == "Noir":
                mangeables.append((x, y))
                deplacementsPotentiels.append((x, y))
                break
            elif partie.getPiece([x, y]) < 0 and self.couleur == "Blanc":
                mangeables.append((x, y))
                deplacementsPotentiels.append((x, y))
                break
            elif partie.getPiece([x, y]) > 0 and self.couleur == "Blanc":
                break
            elif partie.getPiece([x, y]) < 0 and self.couleur == "Noir":
                break
            else:
                deplacementsPotentiels.append((x, y))

        x, y = self.position
        while y < 7*t and x < 7*t:
            x, y = f3(x, y)
            if (partie.getPiece([x, y]) == 6 and self.couleur == "Noir") or (partie.getPiece([x, y]) == -6 and self.couleur == "Blanc"):
                pourLeRoiCurieux.append((x, y))
                break
            if partie.getPiece([x, y]) > 0 and self.couleur == "Noir":
                mangeables.append((x, y))
                deplacementsPotentiels.append((x, y))
                break
            elif partie.getPiece([x, y]) < 0 and self.couleur == "Blanc":
                mangeables.append((x, y))
                deplacementsPotentiels.append((x, y))
                break
            elif partie.getPiece([x, y]) > 0 and self.couleur == "Blanc":
                break
            elif partie.getPiece([x, y]) < 0 and self.couleur == "Noir":
                break
            else:
                deplacementsPotentiels.append((x, y))

        x, y = self.position
        while y < 7*t and x > 1*t:
            x, y = f4(x, y)
            if (partie.getPiece([x, y]) == 6 and self.couleur == "Noir") or (partie.getPiece([x, y]) == -6 and self.couleur == "Blanc"):
                pourLeRoiCurieux.append((x, y))
                break
            if partie.getPiece([x, y]) > 0 and self.couleur == "Noir":
                mangeables.append((x, y))
                deplacementsPotentiels.append((x, y))
                break
            elif partie.getPiece([x, y]) < 0 and self.couleur == "Blanc":
                mangeables.append((x, y))
                deplacementsPotentiels.append((x, y))
                break
            elif partie.getPiece([x, y]) > 0 and self.couleur == "Blanc":

                break
            elif partie.getPiece([x, y])< 0 and self.couleur == "Noir":
                break
            else:
                deplacementsPotentiels.append((x, y))
        return deplacementsPotentiels, mangeables, pourLeRoiCurieux


class Roi(Pieces):
    nombreInstances = 0

    def __init__(self, estBlanc: bool, position: list):
        """
        Le constructeur de cette classe fonctionne sur le même principe que les autres, mais cette classe possède des attributs supplémentaires uniques au roi:
        - self.quiMetEnEchec (list ou None) : le tableau de toutes les pièces qui mettent en échec le roi.
        - self.enEchec (bool) : un booléen nous informant si le roi est en situation d'échec ou non.
        - self.solutions (list ou None) : le tableau de toutes les pièces qui peuvent sauver le roi de l'échec et donc empêcher le mat.
        """
        self.quiMetEnEchec = None
        self.enEchec = False
        self.solutions = None
        self.numero = 1
        Roi.nombreInstances += 1
        super().__init__(nom='roi', couleur='Blanc' if estBlanc else 'Noir',
                         position=position, nomInt=6 if estBlanc else -6)

    def getNumero(self) -> int:
        return self.numero

    def getNombreInstances(self) -> int:
        return Roi.nombreInstances

    def getDeplacementsPossibles(self):
        return self.tousLesDeplacementsPossibles

    def getEnEchec(self):
        return self.enEchec

    def getEchecEtMat(self):
        return self.echecEtMat

    def getNom(self) -> str:
        return super().getNom() + " " + self.couleur

    def setEnEchec(self, b: bool) -> None:
        self.enEchec = b

    def setNumero(self, n: int) -> None:
        self.numero = n

    def setPos(self, pos):
        self.position = pos

    def Echec(self, tour, partie) -> bool:
        """
        
        /!\ Faute de temps, l'algorithme de l'échec est incomplet, il s'agit alors d'une ébauche qui peut détecter l'échec, l'échec et mat mais qui ne permet pas comme convenu initialement d'afficher les déplacements permettant de sauver le roi /!\
        

        args
        ---------
        tour (int) : le tour actuel de la partie
        partie (Partie): un objet de type partie (définie dans le fichier Partie.py) qui représente la partie en cours.
    
        returns
        ---------
        len(vilains)>0 (bool): un booléen qui définit si le roi est en échec
        
        explication de l'algorithme
        ---------
        Cette méthode calcule si le roi est en échec ou non, celle-ci doit être calculée à chaque fin de tour.
        Cette méthode vérifie également qu'il n'y a pas échec et mat et propose (partiellement, l'algorithme n'a malheureusement pas pu être terminé dans les délais accordés pour le concours) les solutions pour éviter le mat.
        Si le mat est détecté alors la partie se termine.
        
        L'algorithme implémenté fonctionne de la manière suivante:
        
            -- on parcoure toutes les pièces de la partie en cours et si ce sont des pièces alliées alors on place leurs noms dans le dictionnaire solutionsPotentielles sinon on place leur nom dans le tableau vilain (seulement si ils peuvent atteindre le roi cependant)
            -- en fonction de si le tableau solution est vide on lance la fin de la partie ou non
            -- pour définir si le roi est en échec, on renvoie juste True si une pièce adverse ou plus a le roi dans ses déplacements possibles ou non.
            
        """

        tousLesDP = {}
        solutionsP = {}
        for cle, e in partie.dictPieces.items():

            if (e.p.getNomInt() > 0 and self.couleur == "Noir") or (
                    e.p.getNomInt() < 0 and self.couleur == "Blanc") and abs(e.p.getNomInt()) != 6:
                tousLesDP[cle] = (e.p.getPos(), e.p.deplacements_possibles(tour, partie)[2])
            if (e.p.getNomInt() < 0 and self.couleur == "Noir") or (
                    e.p.getNomInt() > 0 and self.couleur == "Blanc") and abs(e.p.getNomInt()) != 6:
                solutionsP[cle] = e.p.deplacements_possibles(tour, partie)[0]
            if (e.p.getNomInt() == 6 and self.couleur == "Blanc") or (e.p.getNomInt() == -6 and self.couleur == "Noir"):
                self.calc = False
                solutionsP[cle] = e.p.deplacements_possibles(tour, partie)[0]

            if (e.p.getNomInt() == -6 and self.couleur == "Blanc") or (e.p.getNomInt() == 6 and self.couleur == "Noir"):
                tousLesDP[cle] = (e.p.getPos(), e.p.deplacements_possibles(tour, partie)[2])

        vilains = [e for e in tousLesDP.keys() if self.position in tousLesDP[e][1]]
        a =  [partie.dictPieces[e] for e in vilains]
        
            
            
        if len(vilains) > 0:
            self.setEnEchec(True)
        if len(vilains) == 0: self.setEnEchec(False)

        dpv = [tousLesDP[e][0] for e in tousLesDP if e in vilains]


        solutions = []
        for e in solutionsP.values():
            for it in e:
                if it in dpv:
                    solutions.append(it)

        


        if len(solutions) == 0 and len(vilains) > 0:

            partie.Fin(self.couleur)
            # FIN DE LA PARTIE
        elif len(vilains) > 0:
            self.solutions = solutions
            self.quiMetEnEchec = vilains

        return len(vilains) > 0

    def deplacements_possibles(self, tour: int, partie):
        """
        args
        ---------
        tour (int) : le tour actuel de la partie
        partie (Partie): un objet de type partie (définie dans le fichier Partie.py) qui représente la partie en cours.
    
        returns
        ---------
        deplacementsPossibles (list[tuple]) : la position de tous les déplacements possibles sauf le roi (roi immangeable)
        mangeable (list[tuple]): la position de toutes les pièces qui peuvent être mangées
        pourLeRoiCurieux (list[tuple]): la position du roi adverse mangeable si celà est possible => ne sert à rien dans la version rendue pour le concours des trophées NSI puisque l'algorithme de calcul des déplacements possibles dans le cas où le roi est en échec n'a pas été produit.
        
        explication de l'algorithme
        ---------
        Cette méthode sert à calculer tous les déplacements possibles du roi.
        
        L'algorithme implémenté fonctionne de la manière suivante:
        
            -- tout comme le cavalier, les déplacements potentiels du roi sont peu nombreux et peuvent donc être directement inscrits dans un tableau.
            -- ensuite on vérifie simplement que chaque déplacement est possible, autrement dit que le déplacement est bien dans le plateau, qu'il n'y a aucune pièce sur le chemin ou si il y en a une adverse, qu'elle soit mise dans le tableau mangeable.
            
        """
        t = self.taille_case
        deplacementsPotentiels = []
        deplacementsPotentiels.append((self.position[0] + 1 * t, self.position[1]))
        deplacementsPotentiels.append((self.position[0] - 1 * t, self.position[1]))
        deplacementsPotentiels.append((self.position[0], self.position[1] + 1 * t))
        deplacementsPotentiels.append((self.position[0], self.position[1] - 1 * t))
        deplacementsPotentiels.append((self.position[0] + 1 * t, self.position[1] + 1 * t))
        deplacementsPotentiels.append((self.position[0] + 1 * t, self.position[1] - 1 * t))
        deplacementsPotentiels.append((self.position[0] - 1 * t, self.position[1] + 1 * t))
        deplacementsPotentiels.append((self.position[0] - 1 * t, self.position[1] - 1 * t))

        deplacementsPossibles = []
        mangeables = []

        for e in deplacementsPotentiels:

            if e[0] < 8 * t and e[0] > 0 and e[1] < 8 * t and e[1] >= 0:
                a = partie.getPiece(e)
                if not a:
                    deplacementsPossibles.append(e)
                if a and (a > 0 and self.nomInt < 0) or (a < 0 and self.nomInt > 0):
                    if abs(a) != 6:
                        mangeables.append(e)
                        deplacementsPossibles.append(e)
        return deplacementsPossibles, mangeables, []

class Dame(Pieces):
    nombreInstances = 0

    def __init__(self, numero: int, estBlanc: bool, position: tuple or list):

        Dame.nombreInstances += 1
        self.numero = Dame.nombreInstances
        super().__init__(nom="dame", couleur="Blanc" if estBlanc else "Noir",
                         position=position, nomInt=5 if estBlanc else -5)

    # accesseurs
    def getNumero(self) -> int:
        return self.numero

    def getNom(self) -> str:
        return super().getNom() + " " + self.couleur + str(self.numero)

    def getNombreInstances(self) -> int:
        return Dame.nombreInstances

    # mutateurs
    def setNumero(self, n: int) -> None:
        self.numero = n

    def setPos(self,pos):
        self.position = pos

    # méthodes


    def deplacements_possibles(self,tour,partie):
        """
        args
        ---------
        tour (int) : le tour actuel de la partie
        partie (Partie): un objet de type partie (définie dans le fichier Partie.py) qui représente la partie en cours.
    
        returns
        ---------
        deplacementsPossibles (list[tuple]) : la position de tous les déplacements possibles sauf le roi (roi immangeable)
        mangeable (list[tuple]): la position de toutes les pièces qui peuvent être mangées
        pourLeRoiCurieux (list[tuple]): la position du roi adverse mangeable si celà est possible => ne sert à rien dans la version rendue pour le concours des trophées NSI puisque l'algorithme de calcul des déplacements possibles dans le cas où le roi est en échec n'a pas été produit.
        
        explication de l'algorithme
        ---------
        Cette méthode sert à calculer tous les déplacements possibles de la reine.
        
        L'algorithme implémenté fonctionne de la manière suivante:
        
            -- On instancie une fausse tour et un faux fou à la position de la reine
            -- on récupère leurs déplacements possibles et on les ajoute au tableau des déplacements possibles de la reine.
            
        Oui cette méthode est plutôt simple puisque la reine se déplace comme une tour et comme un fou. On peux alors utiliser leurs algorithmes pour définir le mouvement de la reine.
            
        """

        t = Tour(1, self.couleur == "Blanc", self.position)

        f = Fou(1, self.couleur == "Blanc", self.position)
        deplacementsPotentiels, mangeable, pourLeRoiCurieux = t.deplacements_possibles(tour,partie)
        dp, ma, pr = f.deplacements_possibles(tour,partie)
        deplacementsPotentiels, mangeable, pourLeRoiCurieux = deplacementsPotentiels + dp, mangeable + ma, pourLeRoiCurieux + pr

        return deplacementsPotentiels, mangeable, pourLeRoiCurieux
