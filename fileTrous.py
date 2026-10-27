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

	def printPile(self):

		print("Sommet")

		for i in range(self.taille):
			print("|", self.P[i], "|")

		print("-----")

if __name__ == "__main__":

    F = File()

    # Vos tests ici
