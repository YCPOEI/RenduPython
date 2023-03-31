from Baston.Combattant import combattant

class Guerrier(combattant.combattant):
    def __init__(self):
        super().__init__(120,20)

    def __str__(self):
        return (f"{self.pv} {self.pa}")

    def __repr__(self):
        return (f"objet = guerrier(pv='{self.pv}',pa='{self.pa}')")

