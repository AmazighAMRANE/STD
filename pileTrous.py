def afficher3Piles(A, B, C):
    print("-" * 28)
    print("   A        B        C")
    print("-" * 28)
    h = max(A.taille, B.taille, C.taille)

    for i in range(h):
        a = A.P[i] if i < A.taille else ""
        b = B.P[i] if i < B.taille else ""
        c = C.P[i] if i < C.taille else ""

        print(f"{str(a):^8} {str(b):^8} {str(c):^8}")

    print("-" * 28)

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
    afficher3Piles(A,B,C)


    # Déplacements
    B.empiler(A.depiler())   
    B.empiler(A.depiler())   
    C.empiler(A.depiler())   
    C.empiler(A.depiler())   
	
    print("\nÉtat intermédiaire")
    afficher3Piles(A,B,C)

    A.empiler(B.depiler())   
    A.empiler(C.depiler())   
    A.empiler(B.depiler())   
    A.empiler(C.depiler())   
    
    print("\nÉtat final")
    afficher3Piles(A,B,C)

