class Pile:

    def __init__(self):
        # Je crée une pile de taille 10 qui ne contient rien
        self.P = [None] * 10
        self.taille = 0

    def empiler(self, x):

        # Décaler les éléments vers la droite
        for i in range(................):
            self.P[...] = self.P[...]

        # Je mets l'élément ajouté au sommet de la pile
        self.P[...] = ...

        # La taille de la pile augmente
        self.taille = ...

    def depiler(self):

        # Je récupère le sommet de la pile
        x = self.P[...]

        # Décaler les éléments vers la gauche
        for i in range(................):
            self.P[...] = self.P[...]

        # La taille de la pile diminue
        self.taille = ...

        # Le dernier élément est mis à None
        self.P[...] = None

        # Je renvoie le sommet de la pile
        return ...
	
	def printPile(self):
		print("Sommet")
		for i in range(self.taille):
			print("|", self.P[i], "|")
		print("-----")

if __name__ == "__main__":

    A = Pile()
    B = Pile()
    C = Pile()

    # A = 3 1 4 2 (3 est au sommet)
    A.empiler(2)
    A.empiler(4)
    A.empiler(1)
    A.empiler(3)

    print("État initial")
	A.printPile()
	B.printPile()
	C.printPile()


    # Déplacements
    B.empiler(A.depiler())   
    B.empiler(A.depiler())   
    C.empiler(A.depiler())   
    C.empiler(A.depiler())   
	
	print("État intermédiaire")
	A.printPile()
	B.printPile()
	C.printPile()

    A.empiler(B.depiler())   
    A.empiler(C.depiler())   
    A.empiler(B.depiler())   
    A.empiler(C.depiler())   
    
    print("État final")
	A.printPile()
	B.printPile()
	C.printPile()

