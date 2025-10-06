# tp 3 : chaînes de caractères

# problème 1: échauffements
mot = input("Entrer un mot : ")
if len(mot) > 6:
    print(len(mot))  #  longueur du mot
    print(mot[-2])  # avant dernier caractère
    print(mot[:-3])  # avant avant dernier car
    print(mot[-3:])  # trois derniers caractères
    print(mot[::-1])  # chaîne inversée
    print(mot[::3])  # un caractère sur trois
    print(mot[1:5])  # du caractère d'indice 1 au caractère d'indice 5 (exclus)

# problème 2 : guess the word!
word = "sakura"
guess = input("Entrer un mot")
guess_min = guess.lower()
if word == guess_min:
    print("Bravo ! Tu as trouvé !")
else:
    print("Dommage, retentes")


# problème 3 : calcul de longueur
msg = input("Écrire un message : ")
length = len(msg)
if length > 15:
    print("Le message est trop long")
elif length == 15:
    print("Le message est parfait !")
else:
    print("Le message est trop court")

# problème 4 : recherche de mot clé
msg = "on ne voit pas le temps passer quand on programme en Python"
msg_low = msg.lower()
rep = input("Donne moi un mot et je te dirai s'il est dans mon message : ")
mot_clef = rep.lower().strip()

if mot_clef in msg_low:
    print(f"Le mot {mot_clef} est dans le message.")
else:
    print(f"Le mot {mot_clef} n'est pas dans le message.")


# problème 5 : une affaire de précision
pi = 3.15159265
print(f"Avec une précision de 2 décimales : {pi:.2f}")
print(f"Avec une précision de 5 décimales : {pi:.5f}")
print(f"En écriture scientifique, avec une précision de 3 décimales : {pi:.3e}")


# problème 6 : palindrome
word = input("Entrer un mot : ").lower()
if word == word[::-1]:
    print(f"{word} est un palindrome !")
else:
    print(f"{word} n'est pas un palindrome...")


# problème 7 : voyelles
mot = input("Entrer un mot de trois lettres : ")

voyelles = "aeiou"
nbr_voyelles = 0
if mot[0] in voyelle:
    nbr_voyelles += 1
if mot[1] in voyelle:
    nbr_voyelles += 1
if mot[2] in voyelle:
    nbr_voyelles += 1

print(f"Il y a {nbr_voyelles} voyelles dans le mot {mot}.")


# problème 7 : option 2
vowels = "aeiou"
word = input("Enter any word: ")
count_vowels = word[0] in vowels + word[1] in vowels + word[2] in vowels
print(f"There are {count_vowels} vowels in the word {word}.")
