# Jeu de devinette
# PROJET SUR LES STRUCTURES DE CONTROLE

Le HANGMAN ou le jeu du pendu.
L’idée du jeu, c’est qu’un mot secret est proposé au hasard et que l’utilisateur doit le deviner.
# Règles du jeu :
1. Le jeu peut se jouer sur 3 niveaux. 
- Lorsque l'utilisateur choisit le niveau 1, le jeu lui suggère des mots à 5 lettres au maximum
- Lorsque l'utilisateur choisit le niveau 2, le jeu lui suggère des mots à 8 lettres au maximum
- Lorsque l'utilisateur choisit le niveau 3, le jeu lui suggère des mots à 10 lettres et plus
2. Un mot secret est tiré au hasard d’une liste de terme qui est chargée, selon le niveau
3. L’utilisateur aura 6 tentatives maximales, pour deviner le mot secret
a - L'utilisateur démarre avec la possibilité de faire jusqu’à 3 erreurs. On les appelle point-erreur
b - Si l'utilisateur tape autre chose qu'une lettre de l’alphabet (symboles, chiffres), dites a l'utilisateur qu'il ne peut saisir qu'une lettre  de l’alphabet. Ensuite il perd un point-erreur, et vous lui indiquez le nombre de point-erreur restants. S’il épuise sa cartouche de point-erreur il perd une tentative.
c - Si l'utilisateur entre une lettre qui n'a pas été devinée auparavant et que la lettre soit dans le mot secret, l'utilisateur ne perd aucune tentative, au cas contraire il en gagne une de plus.
d - Si l'utilisateur entre une consonne qui n'a pas été devinée et que la consonne n’est pas dans le mot secret, l’utilisateur perd une tentative.
e - Si l’utilisateur fournit une voyelle et que la voyelle n'a pas été devinée et aussi n'est pas dans le mot secret, l'utilisateur perd deux tentatives. Les voyelles sont « a, e, i, o et u » la lettre « y » est non comptée comme une voyelle.
4. Le jeu doit se terminer lorsque l'utilisateur construit le mot complet ou atteint le nombre maximal de tentatives.
5. Si le joueur n'a plus de tentatives avant de terminer le mot, dites-lui qu'il est pendu et révéler le mot secret à l'utilisateur à la fin du jeu.
6. Si l'utilisateur gagne, imprimez un message de félicitations et dites à l'utilisateur son score.
7. Le score total est le nombre de tentatives restantes une fois que l'utilisateur a deviné le mot secret multiplier avec le nombre de lettres uniques dans le mot secret.
8. Donner à l'utilisateur la possibilité d'effectuer plusieurs parties dans le même niveau, en  ajoutant une gestion du meilleur score obtenu dans la série des parties.
NB : A chaque tentative :
⦁	Le jeu vous retourne les lettres disponibles (non encore utilisées)
⦁	Egalement il place les bonnes lettres à leur endroit à chaque bonne tentative et laisse vide le reste du mot à deviner

