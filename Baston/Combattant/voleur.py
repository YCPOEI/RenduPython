from Baston.Combattant import combattant

class Voleur(combattant.combattant):
    def __init__(self):
        super().__init__(60, 20)

    def __str__(self):
        return f'Voleur;{self.pv};{self.pa}'

    def __repr__(self):
        return f"objet = Voleur(pv='{self.pv}',pa='{self.pa}')"
