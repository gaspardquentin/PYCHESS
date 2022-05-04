from piece_pygame import *
import pygame as pg
from datetime import datetime

#---| Les ressources des images des pions par défaut |----#
pionB = "../res/pion_noir.png"
pionW = "../res/pion_blanc.png"
tourB = "../res/tour_noir.png"
tourW = "../res/tour_blanc.png"
cavalierB = "../res/cheval_noir.png"
cavalierW = "../res/cheval_blanc.png"
roiB = "../res/roi_noir.png"
roiW = "../res/roi_blanc.png"
reineB = "../res/reine_noir.png"
reineW = "../res/reine_blanc.png"
fouB = "../res/fou_noir.png"
fouW = "../res/fou_blanc.png"



#---| Pièces Noires |----#
pion_noir = "../res/pion_noir.png"
tour_noir = "../res/tour_noir.png"
cavalier_noir = "../res/cheval_noir.png"
roi_noir = "../res/roi_noir.png"
reine_noir = "../res/reine_noir.png"
fou_noir = "../res/fou_noir.png"
#---| Pièces Blanches |----#
pion_blanc = "../res/pion_blanc.png"
tour_blanc = "../res/tour_blanc.png"
cavalier_blanc = "../res/cheval_blanc.png"
roi_blanc = "../res/roi_blanc.png"
reine_blanc = "../res/reine_blanc.png"
fou_blanc = "../res/fou_blanc.png"
#---| Pièces Rouges |----#
pion_rouge = "../res/pion_rouge.png"
tour_rouge = "../res/tour_rouge.png"
cavalier_rouge = "../res/cheval_rouge.png"
roi_rouge = "../res/roi_rouge.png"
reine_rouge = "../res/reine_rouge.png"
fou_rouge = "../res/fou_rouge.png"
#---| Pièces Roses |----#
pion_rose = "../res/pion_rose.png"
tour_rose = "../res/tour_rose.png"
cavalier_rose = "../res/cheval_rose.png"
roi_rose = "../res/roi_rose.png"
reine_rose = "../res/reine_rose.png"
fou_rose = "../res/fou_rose.png"
#---| Pièces Bleues |----#
pion_bleu = "../res/pion_bleu.png"
tour_bleu = "../res/tour_bleu.png"
cavalier_bleu = "../res/cheval_bleu.png"
roi_bleu = "../res/roi_bleu.png"
reine_bleu = "../res/reine_bleu.png"
fou_bleu = "../res/fou_bleu.png"
#---| Pièces Vertes |----#
pion_vert = "../res/pion_vert.png"
tour_vert = "../res/tour_vert.png"
cavalier_vert = "../res/cheval_vert.png"
roi_vert = "../res/roi_vert.png"
reine_vert = "../res/reine_vert.png"
fou_vert = "../res/fou_vert.png"
#---| Pièces Violetes |----#
pion_violet = "../res/pion_violet.png"
tour_violet = "../res/tour_violet.png"
cavalier_violet = "../res/cheval_violet.png"
roi_violet = "../res/roi_violet.png"
reine_violet = "../res/reine_violet.png"
fou_violet = "../res/fou_violet.png"


#---| Initialisation des ressources |----#
plateau = pg.image.load("../res/plateau.png")
overlay = pg.image.load("../res/overlay2.png")
boutton_recommencer =  pg.image.load("../res/b_recommencer.png")
boutton_recommencer2 =  pg.image.load("../res/b2_recommencer.png")
boutton_retour = pg.image.load("../res/retour.png")
boutton_retour2 = pg.image.load("../res/retour2.png")
Victoire1 = pg.image.load("../res/Victoire1.png")
Victoire2 = pg.image.load("../res/Victoire2.png")

infoecran= pg.display.Info()

taille_piece_couleur = (infoecran.current_w- infoecran.current_h)/6 #---| taille des cases du choix de couleurs |----#

#---| position de chaque case de choix de la couleur pour le joueur 1 |----#
pos_j1_blanc =(infoecran.current_h, infoecran.current_h/3+30)
pos_j1_bleu = (infoecran.current_h+1*(taille_piece_couleur), infoecran.current_h/3+30)
pos_j1_rouge =(infoecran.current_h+2*(taille_piece_couleur), infoecran.current_h/3+30)
pos_j1_vert = (infoecran.current_h+3*(taille_piece_couleur), infoecran.current_h/3+30)
pos_j1_rose = (infoecran.current_h+4*(taille_piece_couleur), infoecran.current_h/3+30)
pos_j1_noir = (infoecran.current_h+5*(taille_piece_couleur), infoecran.current_h/3+30)


#---| position de chaque case de choix de la couleur pour le joueur 2 |----#
pos_j2_blanc =(infoecran.current_h, infoecran.current_h/2+90)
pos_j2_bleu = (infoecran.current_h+1*(taille_piece_couleur), infoecran.current_h/2+90)
pos_j2_rouge =(infoecran.current_h+2*(taille_piece_couleur), infoecran.current_h/2+90)
pos_j2_vert = (infoecran.current_h+3*(taille_piece_couleur), infoecran.current_h/2+90)
pos_j2_rose = (infoecran.current_h+4*(taille_piece_couleur), infoecran.current_h/2+90)
pos_j2_noir = (infoecran.current_h+5*(taille_piece_couleur), infoecran.current_h/2+90)

pg.init()

#---| Taille fenêtre |----#
ecran = pg.display.set_mode((infoecran.current_w, infoecran.current_h), pg.FULLSCREEN)

#---| position des 2 boutons |----#
pos_b_recommencer = (infoecran.current_h+0.05*infoecran.current_h,infoecran.current_h*(2/3)+0.05*infoecran.current_h)
pos_b_retour =(infoecran.current_h+0.05*infoecran.current_h,infoecran.current_h-0.15*infoecran.current_h)




#---| Taille des boutons selon la taille de l'écran |----#

taillex_bouton = infoecran.current_w - infoecran.current_h-50
tailley_bouton = int(infoecran.current_h/8)

#---| Redimension selon la taille de lécran |----#
boutton_recommencer = pg.transform.scale(boutton_recommencer, (taillex_bouton,tailley_bouton))
boutton_recommencer2 = pg.transform.scale(boutton_recommencer2, (taillex_bouton,tailley_bouton))

boutton_retour = pg.transform.scale(boutton_retour, (taillex_bouton,tailley_bouton))
boutton_retour2 = pg.transform.scale(boutton_retour2, (taillex_bouton,tailley_bouton))

plateau = pg.transform.scale(plateau, (infoecran.current_h, infoecran.current_h))
overlay = pg.transform.scale(overlay,(infoecran.current_w - infoecran.current_h ,infoecran.current_h))



#---| définition des tailles selon la taille de l'écran |----#
taille_case = infoecran.current_h/8
milieu_case = (infoecran.current_h/8)/2
hauteur_case =milieu_case/2
t = taille_case
m = milieu_case
h = hauteur_case


def initFile(f = "parties.txt"):
    """Initialise la partie dans le fichier texte"""

    with open(f, "a") as file:
        date = str(datetime.now()).split(" ")
        file.write("\npartie du " + date[0] + " à " + date[1] + " :\n\n")


class SpriteLoader(pg.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pg.image.load(path)
        self.image = pg.transform.scale(self.image, (int(taille_case - taille_case / 6), int(taille_case - taille_case / 6)))
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.pos = x_pos, y_pos

    def get_pos(self):
        return self.pos

    def getImage(self):
        return self.image

    def set_pos(self, pos):
        self.pos = pos
    def setImage(self,path):
        self.image = pg.image.load(path)
        self.image = pg.transform.scale(self.image,(int(taille_case - taille_case / 6), int(taille_case - taille_case / 6)))


class SpritePiece(SpriteLoader):
    def __init__(self, path, piece):
        self.p = piece
        super().__init__(path, self.p.getPosx(), self.p.getPosy())

    def update(self, pos, piece):
        if self.p.getNom() == piece:
            self.rect.x = pos[0] - (int(taille_case - taille_case / 6))/2
            self.rect.y = pos[1] - (int(taille_case - taille_case / 6))/2


class Partie:
    "Permet de gérer de tout le déroulement de la partie en s'aidant de chaque classe correspondant aux pièces"
    def __init__(self):
        # ---| Initialisation des pièce sur le plateau |----#
        self.dictPieces ={"pion Noir1":SpritePiece(pionB, Pions(1, False, (milieu_case, taille_case+milieu_case)))
                        ,"pion Noir2":SpritePiece(pionB, Pions(2, False, (taille_case+milieu_case, taille_case+milieu_case)))
                        ,"pion Noir3":SpritePiece(pionB, Pions(3, False, (2*taille_case+milieu_case, taille_case+milieu_case)))
                        ,"pion Noir4":SpritePiece(pionB, Pions(4, False, (3*taille_case+milieu_case, taille_case+milieu_case)))
                        ,"pion Noir5":SpritePiece(pionB, Pions(5, False, (4*taille_case+milieu_case, taille_case+milieu_case)))
                        ,"pion Noir6":SpritePiece(pionB, Pions(6, False, (5*taille_case+milieu_case, taille_case+milieu_case)))
                        ,"pion Noir7":SpritePiece(pionB, Pions(7, False, (6*taille_case+milieu_case, taille_case+milieu_case)))
                        ,"pion Noir8":SpritePiece(pionB, Pions(8, False, (7*taille_case+milieu_case, taille_case+milieu_case)))
                        ,"pion Blanc1":SpritePiece(pionW, Pions(1, True, (milieu_case, 6*taille_case +milieu_case)))
                        ,"pion Blanc2":SpritePiece(pionW, Pions(2, True, (taille_case+milieu_case, 6*taille_case+milieu_case)))
                        ,"pion Blanc3":SpritePiece(pionW, Pions(3, True, (2*taille_case+milieu_case, 6*taille_case +milieu_case)))
                        ,"pion Blanc4":SpritePiece(pionW, Pions(4, True, (3*taille_case+milieu_case, 6*taille_case +milieu_case)))
                        ,"pion Blanc5":SpritePiece(pionW, Pions(5, True, (4*taille_case+milieu_case, 6*taille_case +milieu_case)))
                        ,"pion Blanc6":SpritePiece(pionW, Pions(6, True, (5*taille_case+milieu_case, 6*taille_case +milieu_case)))
                        ,"pion Blanc7":SpritePiece(pionW, Pions(7, True, (6*taille_case+milieu_case, 6*taille_case +milieu_case)))
                        ,"pion Blanc8":SpritePiece(pionW, Pions(8, True, (7*taille_case+milieu_case, 6*taille_case +milieu_case)))
                        ,"tour Noir1":SpritePiece(tourB, Tour(1, False, (milieu_case, 0 +milieu_case)))
                        ,"tour Noir2":SpritePiece(tourB, Tour(2, False, (7*taille_case+milieu_case,0 +milieu_case)))
                        ,"tour Blanc1":SpritePiece(tourW, Tour(1, True, (milieu_case, 7*taille_case +milieu_case)))
                        ,"tour Blanc2":SpritePiece(tourW, Tour(2, True, (7*taille_case+milieu_case, 7*taille_case +milieu_case)))
                        ,"cavalier Noir1":SpritePiece(cavalierB, Cavalier(1, False, (6*taille_case+milieu_case,0 +milieu_case)))
                        ,"cavalier Noir2":SpritePiece(cavalierB, Cavalier(2, False, (taille_case+milieu_case,0 +milieu_case)))
                        ,"cavalier Blanc1":SpritePiece(cavalierW, Cavalier(1, True, (taille_case+milieu_case, 7*taille_case +milieu_case)))
                        ,"cavalier Blanc2":SpritePiece(cavalierW, Cavalier(2, True, (6*taille_case+milieu_case, 7*taille_case +milieu_case)))
                        , "fou Noir1": SpritePiece(fouB, Fou(1, False, (2 * taille_case + milieu_case, 0 +milieu_case)))
                        , "fou Noir2": SpritePiece(fouB, Fou(2, False, (5 * taille_case + milieu_case, 0 +milieu_case)))
                        , "fou Blanc1": SpritePiece(fouW, Fou(1, True, (2 * taille_case + milieu_case, 7 * taille_case +milieu_case)))
                        , "fou Blanc2": SpritePiece(fouW, Fou(2, True, (5 * taille_case + milieu_case, 7 * taille_case +milieu_case)))
                        ,"roi Noir":SpritePiece(roiB, Roi(False, (4*taille_case+milieu_case, 0 +milieu_case)))
                        ,"roi Blanc":SpritePiece(roiW, Roi(True, (4*taille_case+milieu_case, 7*taille_case +milieu_case)))
                        ,"dame Noir1":SpritePiece(reineB, Dame(1, False, (3*taille_case+milieu_case, 0 +milieu_case)))
                        ,"dame Blanc2":SpritePiece(reineW, Dame(1, True, (3*taille_case+milieu_case, 7*taille_case +milieu_case)))}

        # ---| Initialisation d'un tableau contenant la position du milieu de chaque case |----#
        self.tabplateaumilieu = [[(m, m),(t+m, m),(2*t+m, m),(3*t+m, m),(4*t+m, m),(5*t+m, m),(6*t+m, m),(7*t+m, m)]
                  ,[(m, t+m),(t+m, t+m),(2*t+m, t+m),(3*t+m, t+m),(4*t+m, t+m),(5*t+m, t+m),(6*t+m, t+m),(7*t+m, t+m)]
                  ,[(m, 2*t+m),(t+m, 2*t+m),(2*t+m, 2*t+m),(3*t+m, 2*t+m),(4*t+m, 2*t+m),(5*t+m, 2*t+m),(6*t+m, 2*t+m),(7*t+m, 2*t+m)]
                  ,[(m, 3*t+m),(t+m, 3*t+m),(2*t+m, 3*t+m),(3*t+m, 3*t+m),(4*t+m, 3*t+m),(5*t+m, 3*t+m),(6*t+m, 3*t+m),(7*t+m, 3*t+m)]
                  ,[(m, 4*t+m),(t+m, 4*t+m),(2*t+m, 4*t+m),(3*t+m, 4*t+m),(4*t+m, 4*t+m),(5*t+m, 4*t+m),(6*t+m, 4*t+m),(7*t+m, 4*t+m)]
                  ,[(m, 5*t+m),(t+m, 5*t+m),(2*t+m, 5*t+m),(3*t+m, 5*t+m),(4*t+m, 5*t+m),(5*t+m, 5*t+m),(6*t+m, 5*t+m),(7*t+m, 5*t+m)]
                  ,[(m, 6*t+m),(t+m, 6*t+m),(2*t+m, 6*t+m),(3*t+m, 6*t+m),(4*t+m, 6*t+m),(5*t+m, 6*t+m),(6*t+m, 6*t+m),(7*t+m, 6*t+m)]
                  ,[(m, 7*t+m),(t+m, 7*t+m),(2*t+m, 7*t+m),(3*t+m, 7*t+m),(4*t+m, 7*t+m),(5*t+m, 7*t+m),(6*t+m, 7*t+m),(7*t+m, 7*t+m)]]

        # ---| Initialisation d'un tableau contenant la position  de chaque case |----#
        self.tabplateau = [[(0, 0), (t, 0), (2 * t, 0), (3 * t, 0), (4 * t, 0), (5 * t, 0), (6 * t, 0), (7 * t, 0)]
                        , [(0, t), (t, t), (2 * t, t), (3 * t, t), (4 * t, t), (5 * t, t), (6 * t, t), (7 * t, t)]
                        , [(0, 2 * t), (t, 2 * t), (2 * t, 2 * t), (3 * t, 2 * t), (4 * t, 2 * t), (5 * t, 2 * t), (6 * t, 2 * t),(7 * t, 2 * t)]
                        , [(0, 3 * t), (t, 3 * t), (2 * t, 3 * t), (3 * t, 3 * t), (4 * t, 3 * t), (5 * t, 3 * t), (6 * t, 3 * t),(7 * t, 3 * t)]
                        , [(0, 4 * t), (t, 4 * t), (2 * t, 4 * t), (3 * t, 4 * t), (4 * t, 4 * t), (5 * t, 4 * t), (6 * t, 4 * t),(7 * t, 4 * t)]
                        , [(0, 5 * t), (t, 5 * t), (2 * t, 5 * t), (3 * t, 5 * t), (4 * t, 5 * t), (5 * t, 5 * t), (6 * t, 5 * t),(7 * t, 5 * t)]
                        , [(0, 6 * t), (t, 6 * t), (2 * t, 6 * t), (3 * t, 6 * t), (4 * t, 6 * t), (5 * t, 6 * t), (6 * t, 6 * t),(7 * t, 6 * t)]
                        , [(0, 7 * t), (t, 7 * t), (2 * t, 7 * t), (3 * t, 7 * t), (4 * t, 7 * t), (5 * t, 7 * t), (6 * t, 7 * t),(7 * t, 7 * t)]]



        self.group = pg.sprite.Group()  # ---| Initialise la variable du  groupe qui va contenir les pièces |----#
        self.tableau_possibilite = []  # ---| Initialise la variable du tableau des déplacements possibles |----#
        self.selectPiece = ()  # ---| Initialise la variable de la pièce sélectionnée lors du clic utilisateur |----#
        self.tableau_case_possibilite = [] # ---| Initialise la variable du tableau des cases en fontion de self.tableau_possibilite|----#
        self.tableau_mangeable = [] # ---| Initialise la variable du tableau des possiblités de "manger" une piece |----#
        self.tableau_case_mange = [] # ---| Initialise la variable du tableau des cases en fontion de self.tableau_mangeable|----#
        self.tour = 0   # ---| compteur du tour |----#
        self.jeu = True # ---| booléen , True lors du fonctionnement du jeu |----#
        self.fin = "None"   # ---| Initialise la variable qui désigne le vainqueur |----#
        self.couleur_actuelle_J1 = "blanc"  # ---| Initialise la variable de la couleur du joeur 1 |----#
        self.couleur_actuelle_J2 = "noir" # ---| Initialise la variable de la couleur du joeur 2 |----#
        self.retour = False  # ---| booléen, True si l'utilisateur à sa souris sur le bouton de retour au  bureau|----#
        self.recommencer = False   # ---| booléen, True si l'utilisateur à sa souris sur le bouton recommencer|----#


    def get_Dict(self):
        """Get le dictionnaire des pièces"""
        return self.dictPiece

    def get_group(self):
        """Get le group des pièces"""
        return self.group


    def getPiece(self,coo: tuple) -> int:
        """Accède aux numéro d'identification de la piece se trouvant aux coordonnées coo"""
        for e in self.dictPieces:
            if self.trouver_case(self.dictPieces[e].p.getPos()) == self.trouver_case(coo):
                return self.dictPieces[e].p.getNomInt()
        return 0

    def setDictCouleurJ1(self,pion,cavalier,tour,fou,roi,reine):
        """Change la couleur des pièces du joueur 1"""
        for cle,v in self.dictPieces.items():
            if "pion" in cle and "Blanc" in cle:
                v.setImage(pion)
            if cle == "cavalier Blanc1" or cle == "cavalier Blanc2":
                v.setImage(cavalier)
            if cle == "tour Blanc1" or cle == "tour Blanc2":
                v.setImage(tour)

            if cle == "fou Blanc1" or cle == "fou Blanc2":
                v.setImage(fou)
            if cle == "roi Blanc":
                v.setImage(roi)
            if "dame" in cle and "Blanc" in cle:
                v.setImage(reine)

    def setDictCouleurJ2(self,pion,cavalier,tour,fou,roi,reine):
        """Change la couleur des pièces du joueur 2"""
        for cle,v in self.dictPieces.items():
            if "pion" in cle and "Noir" in cle:
                v.setImage(pion)
            if cle == "cavalier Noir1" or cle == "cavalier Noir2":
                v.setImage(cavalier)
            if cle == "tour Noir1" or cle == "tour Noir2":
                v.setImage(tour)

            if cle == "fou Noir1" or cle == "fou Noir2":
                v.setImage(fou)
            if cle == "roi Noir":
                v.setImage(roi)
            if "dame" in cle and "Noir" in cle:
                v.setImage(reine)

    def coupJoue(self, coo1, coo2, f="parties.txt"):
        """Ecrit le coup joué dans le fichier texte qui répertorie les parties"""
        with open(f, "a") as file:
            c1 = self.ScreenToCase(coo1)
            c2 = self.ScreenToCase(coo2)
            joueur = "Joueur 1 => " if self.tour % 2 else "Joueur 2 => "
            file.write(joueur + c1[1] + str(c1[0]) + " -> " + c2[1] + str(c2[0]) + "\n")

    def trouver_case(self,pos):
        """Renvoie la case où se situe les coordonnées pos"""
        case = 0, 0
        for i in range(8):
            for j in range(8):
                if (self.tabplateau[i][j][0] <= pos[0] <= self.tabplateau[i][j][0] + taille_case) and (self.tabplateau[i][j][1] <= pos[1] <= self.tabplateau[i][j][1] + taille_case):
                    case = i, j
                    return case

    def selection_piece(self,case):
        """Renvoie la pièce se situant sur la case donnée en argument"""
        piece = ""
        for cle, p in self.dictPieces.items():
            if (self.tabplateau[case[0]][case[1]][0] <= p.get_pos()[0] <= self.tabplateau[case[0]][case[1]][0] + taille_case) and (self.tabplateau[case[0]][case[1]][1] <= p.get_pos()[1] <= self.tabplateau[case[0]][case[1]][1] + taille_case):
                piece = cle
        return piece

    def rond(self,centre):
        """Crée un rond aux coordonnées donnée par centre en argument """
        pg.draw.circle(ecran, (170, 170, 170), centre,30)

    def donut(self,centre):
        """Crée un cercle aux coordonnées donnée par centre en argument """
        pg.draw.circle(ecran, (0, 250,0), centre,t/2, 5)

    def affichage_point(self,tab_case):
        """Crée les ronds sur les cases données en argument par tab_case """
        for e in tab_case:
            self.rond(self.tabplateaumilieu[e[0]][e[1]])

    def entourer(self,tab_case):
        """Crée les cercles sur les cases données en argument par tab_case """
        for e in tab_case:
            self.donut(self.tabplateaumilieu[e[0]][e[1]])


    def initialisation(self):
        """Remplie le group avec les pièces présente dans le dictionnaire"""
        for e in self.dictPieces.values():
            self.group.add(e)

    def ScreenToCase(self, s):
        """Transforme une position en pixel en  une position du jeu d'échec """
        a = "abcdefgh"
        b = "87654321"
        for i in range(len(self.tabplateaumilieu)):
            for j in range(len(self.tabplateaumilieu[i])):
                if self.tabplateaumilieu[i][j] == s:

                    return (b[i], a[j])

    def selection_mangeable(self):
        """Renvoie les positions où une piece peut être "manger" et l'enlève des cases de déplacement possible """
        new = []
        for e in self.tableau_case_mange:
            for element in self.dictPieces:
                if e == self.trouver_case(self.dictPieces[element].p.getPos()) and e in self.tableau_case_possibilite:
                    new.append(e)
                    self.tableau_case_possibilite.remove(e)
        return new,self.tableau_case_possibilite

    def refresh(self):
        """Réinitialise ces variables """
        self.tableau_case_possibilite = []
        self.tableau_case_mange = []
        self.tableau_possibilite = []
        self.selectPiece = ()

    def Pions_changement(self):
        """Transforme le pion en dame lorsqu'il atteint la limite adverse"""
        new = {}
        nom = ""
        for cle,e in self.dictPieces.items():
            pos = e.p.getPos()
            if e.p.getPos()[1] == m and e.p.getNomInt() == 1:
                if  self.couleur_actuelle_J1 == "blanc":
                    couleur_dame = reine_blanc
                elif self.couleur_actuelle_J1 == "bleu":
                        couleur_dame = reine_bleu
                elif self.couleur_actuelle_J1 == "vert":
                        couleur_dame = reine_vert
                elif self.couleur_actuelle_J1 == "rouge":
                        couleur_dame = reine_rouge
                elif self.couleur_actuelle_J1 == "rose":
                    couleur_dame = reine_rose
                elif self.couleur_actuelle_J1 == "noir":
                    couleur_dame = reine_noir
                elif self.couleur_actuelle_J1 == "violet":
                        couleur_dame = reine_violet
                nom = e
                new["dame Blanc"+str(Dame.nombreInstances)] = SpritePiece(couleur_dame, Dame(Dame.nombreInstances, True, pos))
            if e.p.getPos()[1] == 7*t+m and e.p.getNomInt() == -1:
                if self.couleur_actuelle_J2 == "blanc":
                    couleur_dame = reine_blanc
                elif self.couleur_actuelle_J2 == "bleu":
                    couleur_dame = reine_bleu
                elif self.couleur_actuelle_J2 == "vert":
                    couleur_dame = reine_vert
                elif self.couleur_actuelle_J2 == "rouge":
                    couleur_dame = reine_rouge
                elif self.couleur_actuelle_J2 == "rose":
                    couleur_dame = reine_rose
                elif self.couleur_actuelle_J2 == "noir":
                    couleur_dame = reine_noir
                elif self.couleur_actuelle_J2 == "violet":
                    couleur_dame = reine_violet
                nom = e
                #del self.dictPieces[cle]
                new["dame Noir"+str(Dame.nombreInstances)] = SpritePiece(couleur_dame, Dame(Dame.nombreInstances, False, pos))
            if e != nom:
                new[cle] = e
        return new

    def Fin(self,perdant):
        """Met à jour l'écran """
        P.fin = perdant
        ecran.blit(overlay, (infoecran.current_h, 0))
        ecran.blit(boutton_recommencer, pos_b_recommencer)
        if self.retour:
            ecran.blit(boutton_retour2, pos_b_retour)
        else:
            ecran.blit(boutton_retour, pos_b_retour)
        if self.recommencer:
            ecran.blit(boutton_recommencer2, pos_b_recommencer)
        else:
            ecran.blit(boutton_recommencer, pos_b_recommencer)

        ecran.blit(plateau, (0, 0))
        P.group.draw(ecran)

        if perdant == "Blanc":
            ecran.blit(Victoire1, (0, 0))
        elif perdant == "Noir":
            ecran.blit(Victoire2, (0, 0))


    def deroulement_tour(self,mouse):
        """Execute tout le déroulement d'un tour en prenant en argument la position du clic de la souris (mouse) """
        case = self.trouver_case(mouse)
        self.dictPieces = self.Pions_changement()
        self.group = pg.sprite.Group()
        self.initialisation()

        if self.selection_piece(case) != '' and self.tableau_case_mange == [] and self.fin == "None":
            self.tableau_possibilite = self.dictPieces[self.selection_piece(case)].p.deplacements_possibles(self.tour, self)[0]
            self.tableau_mangeable = self.dictPieces[self.selection_piece(case)].p.deplacements_possibles(self.tour, self)[1]
            self.selectPiece = self.selection_piece(case)
            if self.tour%2 == 1 and self.dictPieces[self.selectPiece].p.getNomInt() < 0:
                self.tableau_case_possibilite = []
                self.tableau_case_mange = []

                for i in self.tableau_possibilite:
                    if i != []:
                        self.tableau_case_possibilite.append(self.trouver_case(i))
                for b in self.tableau_mangeable:
                    if b != [] and b != None:
                        self.tableau_case_mange.append(self.trouver_case(b))
                self.tableau_case_mange, self.tableau_case_possibilite = self.selection_mangeable()

            if self.tour%2 == 0 and self.dictPieces[self.selectPiece].p.getNomInt() > 0:
                self.tableau_case_possibilite = []
                self.tableau_case_mange = []

                for i in self.tableau_possibilite:
                    if i != []:
                        self.tableau_case_possibilite.append(self.trouver_case(i))
                for b in self.tableau_mangeable:
                    if b != [] and b != None:
                        self.tableau_case_mange.append(self.trouver_case(b))
                self.tableau_case_mange, self.tableau_case_possibilite = self.selection_mangeable()
            if self.tour % 2 == 0 and self.dictPieces[self.selectPiece].p.getNomInt() < 0:
                self.selectPiece = ()
            if self.tour % 2 == 1 and self.dictPieces[self.selectPiece].p.getNomInt() > 0:
                self.selectPiece = ()


        elif case in self.tableau_case_possibilite and self.selectPiece != ():
            posdepart = self.dictPieces[self.selectPiece].p.getPos()
            self.dictPieces[self.selectPiece].p.setPos(self.tabplateaumilieu[case[0]][case[1]])
            self.dictPieces[self.selectPiece].set_pos(self.tabplateaumilieu[case[0]][case[1]])
            posfinal = self.dictPieces[self.selectPiece].p.getPos()
            print(posdepart,posfinal)
            pos = self.tabplateaumilieu[case[0]][case[1]]
            self.group.update(pos, self.selectPiece)
            self.refresh()
            self.tour += 1
            P.coupJoue(posdepart,posfinal)

        elif case in self.tableau_case_mange and self.selectPiece != ():
            mangee = self.selection_piece(case)
            del self.dictPieces[mangee]
            self.dictPieces[self.selectPiece].p.setPos(self.tabplateaumilieu[case[0]][case[1]])
            self.dictPieces[self.selectPiece].set_pos(self.tabplateaumilieu[case[0]][case[1]])
            pos = self.tabplateaumilieu[case[0]][case[1]]
            self.group = pg.sprite.Group()
            self.initialisation()
            self.group.update(pos, self.selectPiece)
            self.refresh()
            self.tour += 1

        else:
            self.refresh()





P = Partie()
P.initialisation()
initFile()


while P.jeu:
    mouse = pg.mouse.get_pos()
    if (pos_b_retour[0] <= mouse[0] <= pos_b_retour[0] + taillex_bouton) and (pos_b_retour[1] <= mouse[1] <= pos_b_retour[1] + 148):# ---| Vérifie si le bouton retour au bureau est sous la souris |----#
        P.retour = True

    else:
        P.retour = False

    if (pos_b_recommencer[0] <= mouse[0] <= pos_b_recommencer[0] + taillex_bouton) and (pos_b_recommencer[1] <= mouse[1] <= pos_b_recommencer[1] + 148):# ---| Vérifie si le bouton recommencer est sous la souris |----#
        P.recommencer = True

    else:
        P.recommencer = False


    for e in pg.event.get():

        if e.type == pg.KEYDOWN:  # ---| Une sixième couleur cachée est possible : le violet |----#
            if e.key == pg.K_UP:    # ---| Lorsque l'utilisateur appuie sur la fléche du haut sur le clavier |----#
                P.setDictCouleurJ2(pion_violet, cavalier_violet, tour_violet, fou_violet, roi_violet, reine_violet)
                P.couleur_actuelle_J2 = "violet"
            if e.key == pg.K_DOWN:  # ---| Lorsque l'utilisateur appuie sur la fléche du bas sur le clavier |----#
                P.setDictCouleurJ1(pion_violet, cavalier_violet, tour_violet, fou_violet, roi_violet, reine_violet)
                P.couleur_actuelle_J1 = "violet"

        if e.type == pg.MOUSEBUTTONDOWN:  # ---| Lorsque l'utilisateur clique sur l'écran |----#
            mouse = pg.mouse.get_pos()
            if (pos_b_retour[0] <= mouse[0] <= pos_b_retour[0] + taillex_bouton) and (pos_b_retour[1] <= mouse[1] <= pos_b_retour[1] + tailley_bouton):# ---| Vérifie si le bouton retour au bureau est cliqué |----#
                P.jeu = False
                pg.quit()
            if (pos_b_recommencer[0] <= mouse[0] <= pos_b_recommencer[0] + taillex_bouton) and (pos_b_recommencer[1] <= mouse[1] <= pos_b_recommencer[1] + tailley_bouton):# ---| Vérifie si le bouton recommencer  est cliqué |----#
                P = Partie()
                P.initialisation()
                P.refresh()
                P.jeu = True
                P.tour = 0
                ecran.blit(overlay, (0, 0))
                ecran.blit(boutton_recommencer, pos_b_recommencer)
                ecran.blit(boutton_retour, pos_b_retour)
                ecran.blit(plateau, (0, 0))
                P.group.draw(ecran)
                P.fin = "None"
                Dame.nombreInstances = 0

                                # ---| Vérifie si l'utilisateur 1 décide de changer de couleur ses pièces |----#
            if (pos_j1_blanc[0] <= mouse[0] <= pos_j1_blanc[0] + taille_piece_couleur) and (pos_j1_blanc[1] <= mouse[1] <= pos_j1_blanc[1] + 110):
                P.setDictCouleurJ1(pion_blanc,cavalier_blanc,tour_blanc,fou_blanc,roi_blanc,reine_blanc)
                P.couleur_actuelle_J1 = "blanc"

            if (pos_j1_bleu[0] <= mouse[0] <= pos_j1_bleu[0] +  taille_piece_couleur) and (pos_j1_bleu[1] <= mouse[1] <= pos_j1_bleu[1] + 110):
                P.setDictCouleurJ1(pion_bleu,cavalier_bleu,tour_bleu,fou_bleu,roi_bleu,reine_bleu)
                P.couleur_actuelle_J1 = "bleu"

            if (pos_j1_rouge[0] <= mouse[0] <= pos_j1_rouge[0] +  taille_piece_couleur) and (pos_j1_rouge[1] <= mouse[1] <= pos_j1_rouge[1] + 110):
                P.setDictCouleurJ1(pion_rouge,cavalier_rouge,tour_rouge,fou_rouge,roi_rouge,reine_rouge)
                P.couleur_actuelle_J1 = "rouge"

            if (pos_j1_vert[0] <= mouse[0] <= pos_j1_vert[0] +  taille_piece_couleur) and (pos_j1_vert[1] <= mouse[1] <= pos_j1_vert[1] + 110):
                P.setDictCouleurJ1(pion_vert,cavalier_vert,tour_vert,fou_vert,roi_vert,reine_vert)
                P.couleur_actuelle_J1 = "vert"

            if (pos_j1_rose[0] <= mouse[0] <= pos_j1_rose[0] +  taille_piece_couleur) and (pos_j1_rose[1] <= mouse[1] <= pos_j1_rose[1] + 110):
                P.setDictCouleurJ1(pion_rose,cavalier_rose,tour_rose,fou_rose,roi_rose,reine_rose)
                P.couleur_actuelle_J1 = "rose"

            if (pos_j1_noir[0] <= mouse[0] <= pos_j1_noir[0] +  taille_piece_couleur) and (pos_j1_noir[1] <= mouse[1] <= pos_j1_noir[1] + 110):
                P.setDictCouleurJ1(pion_noir,cavalier_noir,tour_noir,fou_noir,roi_noir,reine_noir)
                P.couleur_actuelle_J1 = "noir"


                                # ---| Vérifie si l'utilisateur 2 décide de changer de couleur ses pièces |----#
            if (pos_j2_blanc[0] <= mouse[0] <= pos_j2_blanc[0] +  taille_piece_couleur) and (pos_j2_blanc[1] <= mouse[1] <= pos_j2_blanc[1] + 110):
                P.setDictCouleurJ2(pion_blanc,cavalier_blanc,tour_blanc,fou_blanc,roi_blanc,reine_blanc)
                P.couleur_actuelle_J2 = "blanc"

            if (pos_j2_bleu[0] <= mouse[0] <= pos_j2_bleu[0] +  taille_piece_couleur) and (pos_j2_bleu[1] <= mouse[1] <= pos_j2_bleu[1] + 110):
                P.setDictCouleurJ2(pion_bleu,cavalier_bleu,tour_bleu,fou_bleu,roi_bleu,reine_bleu)
                P.couleur_actuelle_J2 = "bleu"

            if (pos_j2_rouge[0] <= mouse[0] <= pos_j2_rouge[0] +  taille_piece_couleur) and (pos_j2_rouge[1] <= mouse[1] <= pos_j2_rouge[1] + 110):
                P.setDictCouleurJ2(pion_rouge,cavalier_rouge,tour_rouge,fou_rouge,roi_rouge,reine_rouge)
                P.couleur_actuelle_J2 = "rouge"

            if (pos_j2_vert[0] <= mouse[0] <= pos_j2_vert[0] +  taille_piece_couleur) and (pos_j2_vert[1] <= mouse[1] <= pos_j2_vert[1] + 110):
                P.setDictCouleurJ2(pion_vert,cavalier_vert,tour_vert,fou_vert,roi_vert,reine_vert)
                P.couleur_actuelle_J2 = "vert"

            if (pos_j2_rose[0] <= mouse[0] <= pos_j2_rose[0] +  taille_piece_couleur) and (pos_j2_rose[1] <= mouse[1] <= pos_j2_rose[1] + 110):
                P.setDictCouleurJ2(pion_rose,cavalier_rose,tour_rose,fou_rose,roi_rose,reine_rose)
                P.couleur_actuelle_J2 = "rose"

            if (pos_j2_noir[0] <= mouse[0] <= pos_j2_noir[0] + taille_piece_couleur) and (pos_j2_noir[1] <= mouse[1] <= pos_j2_noir[1] + 110):
                P.setDictCouleurJ2(pion_noir,cavalier_noir,tour_noir,fou_noir,roi_noir,reine_noir)
                P.couleur_actuelle_J2 = "noir"







            if (0 <= mouse[0] <= infoecran.current_h) and (0 <= mouse[1] <= infoecran.current_h):# ---| Vérifie si l'utilisateur clique sur le plateau|----#
                P.deroulement_tour(mouse)
                P.dictPieces["roi Noir"].p.Echec(P.tour,P)# ---| Vérifie si l'utilisateur 2 est en échec |----#
                P.dictPieces["roi Blanc"].p.Echec(P.tour,P)# ---| Vérifie si l'utilisateur 1 est en échec |----#

    P.Fin(P.fin)


    echecBlanc = P.dictPieces["roi Blanc"].p.enEchec # ---| initialise au booléen True si échec False sinon |----#
    echecNoir = P.dictPieces["roi Noir"].p.enEchec

    for e in P.tableau_case_possibilite:# ---| Permet l'affichage des déplacements possibles de l'utilisateur |----#
        if e != [] and e != None:
            if (P.tour % 2 == 0 and echecNoir):
                if e in P.dictPieces["roi Noir"].p.solutions:
                    P.affichage_point([e])
            elif (P.tour % 2 == 1 and echecBlanc):
                if e in P.dictPieces["roi Blanc"].p.solutions:
                    P.affichage_point([e])
            else:
                P.affichage_point([e])

    for e in P.tableau_case_mange:# ---| Permet l'affichage des "mangeables" par l'utilisateur |----#
        if e != [] and e != None:
            P.entourer([e])

    pg.display.flip()


