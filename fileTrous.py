def afficher3Files(A, B, C):

    print("A : ", end="")
    for i in range(A.taille - 1, -1, -1):
        print(A.F[i], end=" ")
    print()

    print("B : ", end="")
    for i in range(B.taille - 1, -1, -1):
        print(B.F[i], end=" ")
    print()

    print("C : ", end="")
    for i in range(C.taille - 1, -1, -1):
        print(C.F[i], end=" ")
    print()

class File:

    def __init__(self):
        # Je crée une file de taille 10 qui ne contient rien
        self.F = [None] * 10
        self.taille = 0

    def enfiler(self, x):

        # Décaler les éléments vers la droite
        for i in range(................):
            self.F[...] = self.F[...]

        # J'ajoute le nouvel élément
        self.F[...] = ...

        # La taille de la file augmente
        self.taille = ...

    def defiler(self):

        # La taille de la file diminue
        self.taille = ...

        # Je récupère l'élément qui sort
        x = self.F[...]

        # Le dernier emplacement devient vide
        self.F[...] = None

        # Je retourne l'élément qui sort
        return ...



if __name__ == "__main__":

	A = File()
	B = File()
	C = File()

	A.enfiler(3)
	A.enfiler(1)
	A.enfiler(4)
	A.enfiler(2)

	print("État initial")
	afficher3Files(A,B,C)
	
	B.enfiler(A.defiler())   
	C.enfiler(A.defiler())   
	B.enfiler(A.defiler())   
	C.enfiler(A.defiler())   

	A.enfiler(C.defiler())   
	A.enfiler(C.defiler())   
	A.enfiler(B.defiler())   
	A.enfiler(B.defiler())   
	
	print("État Final")
	afficher3Files(A,B,C)
