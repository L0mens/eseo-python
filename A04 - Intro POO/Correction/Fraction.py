import sys 
from typing import Self
#If python version < 3.11
#https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class
#from typing_extensions import Self

class Fraction():

    def __init__(self, num : int, denum : int) -> None:
        self.numerateur = num
        self.denominateur = denum

    def simplify(self) -> Self:
        factor_num = factors(abs(self.numerateur))
        factor_denum = factors(abs(self.denominateur))
        best_factor = sys.maxsize #Prend le nombre le plus grand possible
        for f in factor_num:
            if f in factor_denum:
                best_factor = f
        return Fraction(int(self.numerateur / best_factor), int(self.denominateur /best_factor))

    def __add__(self, other: Self) -> Self:
        return Fraction(self.numerateur * other.denominateur + self.denominateur * other.numerateur,self.denominateur * other.denominateur).simplify()
    
    def __sub__(self, other: Self) -> Self:
        return Fraction(self.numerateur * other.denominateur - self.denominateur * other.numerateur,self.denominateur * other.denominateur).simplify()
    
    def __mul__(self, other: Self) -> Self:
        return Fraction(self.numerateur * other.numerateur,self.denominateur * other.denominateur).simplify()
    
    def __truediv__(self, other: Self) -> Self:
        return Fraction(self.numerateur * other.denominateur ,self.denominateur * other.numerateur).simplify()
    
    def __gt__(self,other: Self) -> bool:
        return (self.numerateur/ self.denominateur) > (other.numerateur/ other.denominateur)

    def __ge__(self,other: Self) -> bool:
        return (self.numerateur/ self.denominateur) >= (other.numerateur/ other.denominateur)
    
    def __eq__(self,other: Self) -> bool:
        return round(self.numerateur/ self.denominateur,5) == round(other.numerateur/ other.denominateur, 5)
    
    def __ne__(self,other: Self) -> bool:
        return (self.numerateur/ self.denominateur) != (other.numerateur/ other.denominateur)
    
    def __lt__(self,other: Self) -> bool:
        return (self.numerateur/ self.denominateur) < (other.numerateur/ other.denominateur)
    
    def __le__(self,other: Self) -> bool:
        return (self.numerateur/ self.denominateur) <= (other.numerateur/ other.denominateur)
    
    def __str__(self) -> str:
        return f"{self.numerateur} / {self.denominateur}"

"""
Retourne la liste des facteur positif d'un nombre
"""
def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)