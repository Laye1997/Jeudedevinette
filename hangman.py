# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:36:13 2020

@author: Abdul Lahi Jaaw
"""

# -*- coding: utf-8 -*


#
import random #pour effectuer des choix aléatoires
import sys #Utilisé dans notre code pour arreter le programme
from collections import Counter #Utilisé dans notre programme pour compter le nombre d'éléments d'un mot


def niveau():
    
    niveau=input('Veuillez choisir un niveau: ')
    if niveau == '1':
        print('Vous avez choisi le niveau  1')
        words = "niveau1.txt"
        print("Chargement liste des mots depuis le fichier...")
        # inFile: importation du fichier txt
        inFile = open(words, 'r')
        # line: string
        line = inFile.readline()
    # wordlist: liste des mot
        wordlist = line.split()
        print("  ", len(wordlist), "mots chargés.")
    

    elif niveau =='2':
        print('vous avez choisi le niveau  2')
        words = "niveau2.txt"
        print("Chargement liste des mots depuis le fichier...")
        # inFile: fhichier
        inFile = open(words, 'r')
        # line: string
        line = inFile.readline()
    # wordlist: liste des mots chargés
        wordlist = line.split()
        print("  ", len(wordlist), "mots chargés.")    
    
    elif niveau =='3':
        print('vous avez choisi le niveau  3')
        words = "niveau3.txt"
        print("Chargement liste des mots depuis le fichier...")
        # inFile: fichier
        inFile = open(words, 'r')
        # line: string
        line = inFile.readline()
    # wordlist: liste des mots chargés
        wordlist = line.split()
        print("  ", len(wordlist), "mots chargés.")
    word=random.choice(wordlist)
    return word

def play_game():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    consonne = 'bcdfghjklmnpqrstvwxyz'
    voyelle = 'aeoiu'
    word = niveau()
    countDistinct(word)
    letters_guessed = []
    tentatives = 6
    points_erreur = 3
    guessed = False
    
    if __name__=="__main__": 
        a = len(Counter(word).keys())
    print(' le mot contient ',len(word),' lettres')
    print(len(word) * '*')
    while guessed == False and tentatives>0 and points_erreur>=0:
        print('tu as '+str(tentatives)+' tentatives')
        print('tu as '+str(points_erreur)+' points_erreur')
        guess = input(' SVP, entrer une lettre     ').lower()
        
        if len(guess) == 1:
                if guess not in alphabet:
                    print('Veuillez entrer une lettre     ')
                    print('Désolé, vous navez pas compris le principe')
                    print('Ce jeu ne genere pas les caracteres  ')
                    points_erreur-=1
                if points_erreur == 0:
                    tentatives-=1
                    print(visuals(tentatives))
                if guess in letters_guessed:
                    print ("Vous avez déjà tenté la lettre    ",guess,)
                    x = letters_guessed
                    print('ainsi que ces lettres ci     ',x)
                elif guess not in word:
                    print('Désolé,cette lettre n\'existe pas dans le mot')
                    if guess in consonne:
                        tentatives-=1
                        print(visuals(tentatives))
                    elif guess in voyelle:
                        tentatives-=2
                        print(visuals(tentatives))
                        letters_guessed.append(guess)
                    if tentatives == 0:
                        print('Tu es pendu   ')
                        print(visuals(tentatives))
                        print('le mot à deviner est:  ')
                        print(word)
                if guess in word and guess not in letters_guessed:
                    print('Parfait! Cette lettre existe dans le mot')
                    letters_guessed.append(guess)
                    tentatives+=1
                    y=tentatives*a
        status=''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status+=letter
                else:
                    status+='*'
            print(status)
            
        if status==word:
            print('Félicitations, tu as deviné. Le mot est: ========>',word)
            guessed=True                     
            if y>0:
               print('Voici ton score ',y,' points')
               
        if tentatives == 0:
            print('Tu es pendu')
            print('le mot à deviner est: ',word)
            
def menu():         #Création d'un menu pour le jeu
        print('\t\t-- LE PENDU --\n')
        print('1. Jouer')
        print('2. Instructions')
        print('3. Quitter')         
        saisie = input()
        saisie = int(saisie)         
        while saisie < 1 or saisie > 3:
                print('Erreur, 1 pour Jouer,2 pour instructions et 3 pour Quitter')
                saisie = input()
                saisie = int(saisie)         
        if saisie == 1:              
                play_game()   
        elif saisie == 2:
                print ("\n\t\t-- Règles du jeu --\
                                                                                                  Des mots sont tirés au sort parmi une base de donnée. Seule la première et dernière lettre\
 sont affichées, les autres lettres étant remplacées par des étoiles. Le but du jeu est d'essayer de\
 retrouver le mot. Vous pouvez saisir vos réponses lettres par lettre ou avec l'intégralité du mot.\
 Les majuscules et les caractères spéciaux (accents,...) sont volontairement omis pour plus de facilité.\n")
          
                menu()
        else:
                return 0
        rejouer()
                     
def countDistinct(word): 
	return len(Counter(word).keys())	 

def visuals(tentatives):
#This function is used to print the progress through visuals
	if tentatives == 6:
		return"""
		_______
		|     |
		|     
		|
		|
		|
		|
		|________
		|        |
		"""
	elif tentatives == 5:
		return"""
		_______
		|     |
		|     O
		|
		|
		|
		|
		|________
		|        |
		"""
	elif tentatives == 4:
		return"""
		_______
		|     |
		|     O
		|   --|
		|
		|
		|
		|________
		|        |
		"""
	elif tentatives == 3:
		return"""
		_______
		|     |
		|     O
		|   --|--
		|
		|
		|
		|________
		|        |
		"""
	elif tentatives == 2:
		return"""
		_______
		|     |
		|     O
		|   --|--
		|     |
		|    |
		|
		|________
		|        |
		"""
	elif tentatives == 1:
		return"""
		_______
		|     |
		|     O
		|   --|--
		|     |
		|    | |
		|
		|________
		|        |
		"""
	elif tentatives == 0:
		return"""
		_______
		|     |
		|     l0
		|    |||
		|     |
		|    | |
		|
		|________
		| Mort|
		"""	
def rejouer(): # Choisir de Rejouer ou pas
   print("Veux tu rejouer?!\n")
   while True:
        gameChoice = input("oui pour rejouer,non pour quitter\n").lower()
        if gameChoice == "oui" or gameChoice == "o":
            menu()
        elif gameChoice == "non" or gameChoice == "n":
            sys.exit("A bientot")
menu()                    
    