# TP8 : fonctions
#
# L3 TAL S5
# 2025
# 
# PROF: LENA GAUBERT

# PARTIE 1 : PREMIERES FONCTIONS 

# PROBLEME 1 : HELLO WORLD!
def print_greetings(l):
    for name in l:
        print(f"Salutations à toi {name} !")

# example 
names = ["Ada", "Alan"]
print_greetings(names)

# PROBLEME 2 : OPERTIONS MATHS
def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def euclidian_div(a, b):
    return a // b, a % b

def calculate(a, b):
    """
        Compute different operations.
    """
    m = multiply(a, b)
    d = divide(a, b)
    q, r = euclidian_div(a, b)
    return m, d, q, r

# PROBLEME 3 : CARACTER COUNT
def count_char(text, c):
    count_c = 0
    for car in text:
        if car == c:
            count_c += 1

    return count_c

# PROBLEME 4 : STATS
def get_average(l):
    n = len(l)
    num = 0
    for e in l:
        num += e 
    return num / n

def get_min_max():
    pass 

def get_sum():
    pass

# NumPy est un module : ensemble de fonctions pour du calcul mathématique
import numpy as np  # importation du module sous l'alias np

l = [2, 5, 7.8, 14, 78]

def summarize(l):
    # on appelle différentes fonctions de numpy
    avg = np.mean(l)
    n_min = np.min(l)
    n_max = np.max(l)
    n_sum = np.sum(l)
    return avg, n_min, n_max, n_sum


# PROBLEME 5 : PALINDROME
def is_palindrome(word):
    is_pal = False
    if word == word[::-1]:
        is_pal = True 
    return is_pal

def filter_palindrome(words):
    all_palindromes = []
    for word in words:
        if is_palindrome(word):
            all_palindromes.append(word)
    return all_palindromes


# PROBLEME 6 : VOYELLES
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for car in text:
        if car.lower() in vowels:
            count += 1
    return count

def count_all_vowels(texts):
    counts = []
    for text in texts:
        counts.append(count_vowels(text))
    return counts


# PROBLEME 7 : MOTS COMMUNS
def common_words(l1, l2):
    common = []
    for word in l1:
        if word in l2 and word not in common:
            common.append(word)
    return common

def common_words(l1, l2):
    return [e for e in set(l1) if e in l2]


# PARTIE II : PLUS DIFFICILES

# PROBLEME 8 : GUESS THE WORD!
def guessing_game(word, n_trials=3):
    has_won = False

    # first guess
    guess = input("Guess the word! ")
    n_trials -= 1

    # following guesses
    while guess.lower() != word and n_trials != 0:
        guess = input("Guess again: ")
        n_trials -= 1

    if guess.lower() == word:
        has_won = True
    
    return has_won

guessing_game("banana", n_trials=2)


# PROBLEME 9 : SOMME DES CHIFFRES
def sum_digits(num):
    # on convertit l'input en chaîne de caractère
    number = str(num)  # itérable

    s = 0  # init somme
    for d in number:
        if d.isdigit():  # vérifier si le caractère est numérique
            s += int(d)  # on convertit la chaîne en int
    
    return s 

print(sum_digits(123))

# PROBLEME 10 : MOTS DE LONGUEUR CROISSANTE
def longest_words(words):
    c = 0
    for i in range(len(l) - 1):
        if len(l[i+1]) > len(l[i]):
            c += 1

    return c

l = ["my", "beautiful", "catterpillar"]
print(longest_words(l))

# PROBLEME 11 : REPETER LES CARACTÈRES
def repeat_chars(s, n=2):
    new_s = ""
    for car in s:
        new_s += car * n
    return new_s

print(repeat_chars("hello"))

# PROBLEME 12
def first_word(text):
    first = ""  # init
    for c in text:
        if c == " ":
            return first
        
        first += c

    return first
    

def first_word_bis(text):
    """
        Renvoie le premier mot d'un texte, à l'aide
        de la méthode split.
    """
    return text.split()[0]


# PROBLEME 13 : COMPTEUR DE MOTS
def count_words(text):
    word_count = 0
    for car in text:
        print(car)
        if car == " ":
            word_count += 1
    
    return word_count + 1  # on compte les espaces (ils sont entre les mots)

def count_words_bis(text):
    text = text.strip()
    return len(text.split())

text = "I love coding in Python!"
print("Word count 1:", count_words(text))
print("Word count 2:", count_words_bis(text))