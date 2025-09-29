#  TP 1 : déclarration de variables, entrées, affichages, opérations

# problème 1 : Hello world!
a = "Hello"
b = "World"
a, b = "Hello", "World"  # on peut définir les deux variables sur une seule ligne
print(a, b, end="\n", sep="#")
print(a, b, end="!")

c = a + b  # concaténation
print(c * 3)

# problème 2 : multi-printing
a = input("a = ")  # a et b sont des entiers
b = input("b = ")
c = input("c = ")
int_a = int(a)
int_b = int(b)
print(a * int_a, b * int_b, sep=c)

# problème 3 : opérations
num = input("Entrer un nombre :")
print(int(num) * 2)
d = input("Entrer un nombre : ")
print("Le reste de la division euclidienne de num par d est :", int(num) % int(d))
print("num puissance d :", int(num) ** int(d))

# problème 4 : température
# note : la conversion de la température en float se fait où vous le souhaitez !
t_f = float(input("Entrer une température : "))
t_c = (t_f - 32) * 5/9
print(t_c)

# problème 5 : variable swap
a = input("a = ")
b = input("b = ")
# méthode 1
a, b = b, a
# méthode 2
nouveau_a = a
a = b
b = nouveau_a 
print("a =", a, "b =", b)

# problème 6 : variables multiples
name = input("What is your name?")
age = input("How old are you?")
n_cats = input("How many cats do you have?")

int_age = int(age)
age = float(age)
n_cats = int(n_cats)
print("My name is " + name + ", I am " + str(age) + " years old.")
print("I have " + str(n_cats))
