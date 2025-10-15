# tp 4 : boucles while

# problème 1 : guess the word!
word = "mot"
guess = input("Guess the word! ")
c = 1
while guess.lower() != word and c <= 3:
    guess = input(f"Try again! {3 - c} tries remaining")
    c += 1

result = guess.lower() == word
if result:
    print(f"You win in {c} tries!")
else:
    print(f"You lose... the word was  {word}!")


# problème 2 : voyelles
mot = input()
indice = 0
voyelle = "aeiou"
nbr_voyelles = 0

while indice < len(mot):
    if mot[indice] in voyelle:
        nbr_voyelles += 1
        print(mot[indice])
    indice += 1

print(f"Il y a {nbr_voyelles} dans le mot {mot}.")


# problème 3 : affichage progressif d'une chaîne de caractères

word = "python"
c = 1
while c <= len(word):
    print(word[:c])
    c += 1


# problème 4 : sommes
num = int(input("Entrer un nombre entier :"))
n = 0
count = 0
while n != num:
    n += 1
    count += n
print(count)


# problème 4 bis : sommes de multiples de 3
# de 2 à 28
chiffre = 2
total = 0
while chiffre < 28:
    if chiffre % 3 == 0:
        total += chiffre 
    chiffre += 1
print(total)

# problème 5 : factoriel
num = int(input("Entrer un nombre entier :"))
n = 0
count = 0
while n != num:
    n += 1
    count *= n
print(count)


# problème 6 : palindrome

mot = input("Entrer un mot : ")
c = 0
d = 1

while len(mot) <= 2:
    mot = input("Entrer un mot avec plus de deux lettres : ")


if mot[c] != mot[-d]:
    print("ce mot n'est pas un palindrome")
else:
    while mot[:c] == mot[-d]:
        pass

# solution b
mot = input("Entrer un mot:").lower().strip()
length = len(mot)
palindrome = True
i = 0
while i < length / 2:
    if (mot[i] == mot[length-i-1]):
        i += 1
    else:
        palindrome = False
        i = length

if palindrome:
    print(f"{mot} est un palindrome!")
else:
    print("Nope!")


# solution c
mot = input("Entrer un mot : ")
length = len(mot)
i = length - 1
mot_inverse = ""
while i >= 0:
    mot_inverse += mot[i]


# problème 7 : triangles * 
chiffre = int(input("Choisir un nombre"))
c = 1
while c <= chiffre:
    print("*" * c)
    c += 1

# problème 8 : triangle inversé
chiffre = int(input("Choisir un nombre"))
while chiffre > 0:
    print("*" * chiffre)
    chiffre -= 1
