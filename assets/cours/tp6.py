# TP6 : BOUCLES & ITERATIONS II
# BOUCLES FOR
#
# L3 TAL S5
# 2025
# 
# PROF: LENA GAUBERT

# PROBLEME 3
# COMPTEUR D'ITERATIONS

animals = ["bear", "otter", "seal", "kiwi", "dog"]
# option 1
for i, animal in enumerate(animals):
    print(f"Iteration {i+1} : {animal}")

# option 2
n = len(animals)
for i in range(n):
    print(f"Iteration {i+1} : {animals[i]}")

# PROBLEME 4 : COMPTE À REBOURS
for i in range(10, 1, -1):
    print(i)

# PROBLEME 5 : MULTIPLES DE 5
for i in range(21):
    if i % 5 == 0:
        print(i)

# PROBLEME 6 : COMPTEUR DE CONSONNES
vowels = "aeiou"
c_count = 0  # nb of consonants
word = input("Enter a word: ")
for letter in word:
    if letter not in vowels:
        c_count += 1
print(f"There are {c_count} consonants in the word {word}!")

# PROBLEME 7 : CONSTRUCTION DE CHAINE

# option 1
n = 5
chain = ""
for i in range(n):
    chain += str(i+1)
    if i < n-1:
        chain += "-"
print(chain)

# option 2
chain = ""
for i in range(n-1):
    chain += str(i+1)
    chain += "-"
chain += "5"

# option 3 : le cas limite est le premier caractère de la chaîne.


# PROBLEME 8
sent = input("Enter a message: ")
# option 1
clean_sent = ""
for car in sent:
    if car.isalpha():
        clean_sent += car
print(f"Clean message: {clean_sent}")

# opton 2
n = len(sent)
clean_sent = ""
for i in range(n):
    if sent[i].isalpha():
        clean_sent += sent[i]


# PROBLEME 9 : WHILE TO FOR
for i in range(2, 11, 2):
    print(i)


# PROBLEME 10 : FOR TO WHILE
msg = input("Enter a message: ")
i = 0
n = len(msg)
while i < n:
    print(msg[i].lower())
    i += 1


# PROBLEME 11 : LE RETOUR DE LA PYRAMIDE
# option 1
for i in range(5):
    print(i * "*")

# option 2
for i in range(5):
    for j in range(i):
        print("*", end="")
    print()

# option 3
for i in range(5):
    row = ""
    for j in range(i):
        row += "*"
    print(row)


# PROBLEME 12 : MOT LE PLUS LONG
words = ["python", "algorithm", "linux", "anaconda", "jupyter", "spyder"]
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print(f"The longest word is {longest}")


# PROBLEME 13 : TABLEAU DE NOMBRES
n_rows = 3
table = ""
for i in range(n_rows):
    for j in range(5):
        table += str(j+1)
        table += "\t"
    table += "\n"
print(table)

