from math import sqrt
print("""   This is a program that solves quadratic equations.
        The general formula for them is 
        ax**2 + bx + c = 0.
""")
print("Enter a:")
a = float(input())
print("Enter b:")
b = float(input())
print("Enter c:")
c = float(input())
D = b**2 - 4*a*c
if D > 0:
    x1 = ((-b) - sqrt(D)) / (2 * a)
    x2 = ((-b) + sqrt(D)) / (2 * a)
    x1 = round(x1)
    x2 = round(x2)
    print(f"Your roots are {x1} and {x2}")
elif D == 0:
    x = (-b) / 2 * a
    x = round(x)
    print("You only have one root, {x}")
else:
    print("The equation has no real roots.")