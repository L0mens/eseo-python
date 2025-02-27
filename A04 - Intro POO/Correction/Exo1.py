from Product import Product
from Fraction import Fraction

p1 = Product("FR0001", "Stylo Rouge", 10)
p2 = Product("FR0007", "Stylo Violet", 0.99)

print(f"{p1.code} - {p1.name} - {p1.get_price_it(0.2)}")
print(f"{p2.code} - {p2.name} - {p2.get_price_it(0.2)}")


Product.flat_tax = 0.5

print(f"{p1.code} - {p1.name} - {p1.get_price_it_flat()}")

#Va Call __str__ pour gérer l'affichage d'un objet complexe
print(p2)

f1 = Fraction(3,5)
f2 = Fraction(4,5)

print(f1 + f2)

print(f1 > f2)
print(f1 < f2)

print(f1 * f2)

print(f1 - f2)

print(f2/f1)