# TP2 : opérateurs, structures conditionnelles...

# problème 1:
a = input("Devinez le mot : ")
if a == "Manger":
    print("Oui ! Allons manger !")
else:
    print("Raté  !")

# problème 2
# idée 1
num = 42
guess = int(input("Guess the number! "))
if num > guess:
    print("Too high")
elif num < guess:
    print("too low")
else:
    print("that's a win!")

# idée 2
num = 42
x = int(input("Guess the number: "))
if x > num:
  print("Too high!")
  if x < 50:
    print("But you're closer than you think...")
  else:
    print("Really!! Not that high!!!!!") 
elif x < num:
  print("too low...")
  if x < 10:
    print("way too low!!!")
else:
  print("you win!!")

# problème 3 : calculatrice de notes
a = int(input("Entrer une note :"))
if a < 0 or a > 100:
   print("Erreur : la note doit être comprise entre 0 et 100")
else: 
   if a >= 90:
    print("A")
   elif a >= 80:
    print("B")
   elif a >= 70 and a < 80:
    print("C")
   else:
    print("D")


# problème 4 :
a = float(input("Entrer un nombre :"))
if a < 0:
   print("Le nombre est négatif !")
else:
   print("Le nombre est positif !")


# problème 5 : calcul prix des billets
age = int(input("Entrer son age :"))
if age <= 12:
    print("5 euros")
elif age >= 13 and age <= 64:
    print("10 euros")
else:
    print("7 euros")

# problème 6 : pair ou impair
nombre = int(input("Entrer un nombre"))
# le reste de la division euclidienne d'un nombre pair par 2 est égal 0
if nombre % 2 == 0:
    print("nombre est pair")
else:
    print("nombre est impair")


# problème 7 : 
yard = float(input("Entrer la longueur en yard :"))
metre = 0.9144 * yard
print(yard, "yard =", metre, "mètres")
print(yard * 0.9144)