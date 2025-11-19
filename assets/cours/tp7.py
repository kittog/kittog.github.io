# TP7 : BOUCLES ET LISTES
#
# L3 TAL S5
# 2025
# 
# PROF: LENA GAUBERT


# PROBLEME 1 : HELLO WORLD!
names = [
    "Ava", "Evelyne", "Lili", "Nailine",
    "Chaker", "Max", "Bintou",
    "Babette", "Yixin",
    "Cindy", "Djamila"
    ]

for name in names:
    print(f"Hello {name}!!!")


# PROBLEME 3 : JOURS DE LA SEMAINE
week = [
    "monday", "tuesday", "wednesday",
    "thursday", "friday",
    "saturday", "sunday"
    ]

weekdays, weekend = week[:-2], week[-2:]

# inverser la liste
week.reverse()
# week = week[::-1]

# insérer, ajouter
week.insert(0, "may")
week.append(26)

# permutation
week[0], week[-1] = week[-1], week[0]


# PROBLEME 4 : OPERATIONS
l = [12, 45, 7, 23, 56, 89, 34]

# somme
s = 0
n = len(l)
for i in range(n):
    s += l[i]
print(f"Sum: {s}")

# max
max_n = 0
for i in range(n):
    if l[i] > max_n:
        max_n = l[i]
print(f"Maximum: {max_n}")

# len
c = 0
for e in l:
    c += 1
print(f"List length: {c}")

# substract 1
for i in range(n):
    l[i] -= 1
print(f"New list: {l}")

# permutation
l[1], l[5] = l[5], l[1]


# PROBLEME 5 : FILTRE
numbers = [1, 6, 3, 7, 29, 4, 45]
odds = []
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)
print(f"Odd numbers: {odds}")
print(f"Even numbers: {evens}")


# PROBLEME 6 : APRES UN PARTIEL
notes = [14, 8, 16, 12, 6, 18, 10, 15, 9, 17]

# average
n = len(notes)
s = 0
for note in notes:
    s += note
avg = s / n
print(f"Average grade: {avg}")

# above 10
has_avg = 0
for note in notes:
    if note >= 10:
        c += 1

# below 10
not_avg = n - has_avg

print(f"{has_avg} students passed.")
print(f"{not_avg} students failed.")

# above 15 list
above_fifteen = []
for note in notes:
    if note >= 15:
        above_fifteen.append(note)


# PROBLEME 7 : MANIPULATION DE CHAINES
words = ["python", "programmation", "liste", "boucle", "algorithme"]

words_upper = []
long_words = []
first_letters = []
for word in words_upper:
    # uppercase
    words_upper.append(word.upper())
    # words longer than 6 letters
    if len(word) > 6:
        long_words.append(word)
    # print word reversed
    print(word[::-1])
    # extract first letter
    first_letters.append(word[0])

print(f"Uppercase: {words_upper}")
print(f"Longer words: {long_words}")
print(f"First letters: {first_letters}")

# PROBLEME 8: NESTED LOOPS
lengths = []
for word in words:
    c = 0
    for car in word:
        c += 1
    lengths.append(c)

# advanced (one-liner)
lengths = [len(word) for word in words]


# PROBLEME 9 : RECHERCHE DANS UNE LISTE
user = input("Enter a name")
is_found = False
for i in range(len(names)):
    is_found = names[i] == user
    if is_found:
        print(f"Name {user} found at position {i}.")

if not is_found:
    print(f"Name {user} not found.")


# PROBLEME 10 : COMBINAISON DE LISTES
l1 = [2, 4, 6, 8, 10]
l2 = [1, 3, 5, 7, 9]
# l1 and l2 have the same number of elements

sums = []
prods = []
for i in range(len(l1)):
    sums.append(l1[i] + l2[i])
    prods.append(l1[i] * l2[i])


# PROBLEME 11 : DU MIN AU MAX
a = [3, 5, 7, 2, 8, 1]

min_n = a[0]
max_n = a[0]
i_max = 0
i_min = 0
for i in range(len(a)):
    if a[i] > max_n:
        max_n = a[i]
        i_max = i
    elif a[i] < min_n:
        min_n = a[i]
        i_min = i
    else:
        continue

print(f"Max: {max_n}; found at position {i_max}")
print(f"Min: {min_n}; found at position {i_min}")
