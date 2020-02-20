# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:36:13 2020

@author: Abdul Lahi Jaaw
"""

# -*- coding: utf-8 -*-azzzzzzzzzzzzzzzaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeezzzzzzzzzzzzzzzzzzzzzzzzzzzzzzeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeezzzzzzzzzzzzzzzzzzzzzzzzz*

import random
def rejouer():
    print("Veux tu rejouer?!\n")

    while True:
        gameChoice = input("oui pour rejouer,non pour quitter\n").lower()

        if gameChoice == "oui" or gameChoice == "o":
            menu()
        elif gameChoice == "non" or gameChoice == "n":
            print("A bientot")
            break
        


def niveau():
    niveau=input('choisir un niveau')
   
    if niveau=='1':
        print('vous avez choisi le niveau1')
        words = "niveau1.txt"
    
        print("Loading word list from file...")
        # inFile: file
        inFile = open(words, 'r')
        # line: string
        line = inFile.readline()
    # wordlist: list of strings
        wordlist = line.split()
        print("  ", len(wordlist), "words loaded.")
    

    elif niveau=='2':
        print('vous avez choisi le niveau2')
        words = "niveau2.txt"
    
        print("Loading word list from file...")
        # inFile: file
        inFile = open(words, 'r')
        # line: string
        line = inFile.readline()
    # wordlist: list of strings
        wordlist = line.split()
        print("  ", len(wordlist), "words loaded.")    
    elif niveau=='3':
        print('vous avez choisi le niveau3')
        words = "niveau3.txt"
    
        print("Loading word list from file...")
        # inFile: file
        inFile = open(words, 'r')
        # line: string
        line = inFile.readline()
    # wordlist: list of strings
        wordlist = line.split()
        print("  ", len(wordlist), "words loaded.")
    
    
    word=random.choice(wordlist)
    
    return word

def play_game():
    alphabet='abcdefghijklmnopqrstuvwxyz'
    consonne='bcdfghjklmnpqrstvwxyz'
    voyelle='aeoiu'
    word=niveau()
    countDistinct(word)
    letters_guessed=[]
    tentatives=6
    points_erreur=3
    guessed=False
    
    if __name__=="__main__": 
	 
        a=countDistinct(word)
    
    print(' le mot contient',len(word),'lettres')
    print(len(word) * '*')
    while guessed== False and tentatives>0 and points_erreur>=0:
        print('tu as'+str(tentatives)+'tentatives')
        print('tu as'+str(points_erreur)+'points_erreur')
        guess=input(' SVP entrer une lettre').lower()
        
        if len(guess)==1:
                if guess not in alphabet:
                    print('Veuillez entrer une lettre')
                    print('Désolé, vous navez pas compris le principe')
                      
                    print('   Ce jeu ne genere pas les caracteres')
                    points_erreur-=1
                if points_erreur==0:
                    tentatives-=1
                    print(visuals(tentatives))
                
                    
                if guess in letters_guessed:
                    print ("Vous avez déjà tenté la lettre",guess,)
                    x=letters_guessed
                    print('ainsi que ces lettres ci',x)
                
                
                elif guess not in word:
                    print('Désolé,cette lettre n\'existe pas de le mot')
                
                    if guess in consonne:
                        tentatives-=1
                        print(visuals(tentatives))
                    elif guess in voyelle:
                        tentatives-=2
                        print(visuals(tentatives))
                        letters_guessed.append(guess)
                    if tentatives==0:
                        print('Tu es pendu')
                        print(visuals(tentatives))
                        print('le mot à deviner est:')
                        print(word)
                if guess in word and guess not in letters_guessed:
                    print('Bravo!, cette lettre existe dans le mot')
                    letters_guessed.append(guess)
                    tentatives+=1
                    y=tentatives*a
                
                
        status=''
        if guessed==False:
            for letter in word:
                if letter in letters_guessed:
                    status+=letter
                else:
                    status+='*'
            print(status)
            
        if status==word:
            print('felicitation, tu as deviner. Le mot est: ')
            print(word)
                          
            if y>0:
                print('Voici ton score',y,'points')
            guessed=True
        if tentatives==0:
            print('Tu es pendu')
            print('le mot à deviner est:')
            print(word)
def menu():
                
        print('\t\t-- LE PENDU --\n')
        print('1. Jouer')
        print('2. Instructions')
        print('3. Quitter')
                
        saisie = input()
        saisie = int(saisie)
                
        while saisie < 1 or saisie > 3:
                print('Erreur, 1 pour Jouer, 2 pour Quitter')
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



from collections import Counter 

def countDistinct(word): 

	
	return len(Counter(word).keys())	 

def visuals(tentatives):
#This function is used to print the progress through visuals
	if tentatives== 6:
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
		| D E A D|
		"""	
            
menu()                    
    