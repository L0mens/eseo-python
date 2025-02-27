class Product():

    flat_tax = 0.2

    def __init__(self, code: str, name : str, priceET: float) -> None:
        self.code = code
        self.name = name
        self.priceET = priceET

    def get_price_it(self, tax: float)-> float:
        return self.priceET * (1.0 + tax)
    
    def get_price_it_flat(self) -> float:
        return self.priceET * (1.0 + Product.flat_tax)
    
    #Pour gérer l'affichage directement depuis l'objet
    def __str__(self) -> str:
        return f"{self.code} - {self.name} - {round(self.get_price_it_flat(), 2)}"
    


