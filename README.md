[English version below]

# TDLOG : première séance

Ce fichier présente les exercices de la première séance du module. L'objectif
est de produire un code de qualité (lisibilité, nommage, commentaires) et non
pas de couvrir le maximum d'exercices. Les exercices sont à faire en binôme, et
en anglais (noms des fonctions et variables, commentaires). Lors de cette
séance, on s'intéresse à la modélisation des éléments de base d'une version
légèrement simplifiée du jeu Scotland Yard / Mister X. Par modélisation, on
entend la définition des classes représentant les divers éléments du jeu.


## Présentation du jeu

Le jeu [Scotland Yard / Mister X](https://fr.wikipedia.org/wiki/Scotland_Yard_(jeu))
est publié sous quelques variantes par Ravensburger. Il s'agit d'un jeu de
plateau dans lequel plusieurs détectives de Scotland Yard cherchent à attraper
un fugitif, Mister X. Une version des règles est disponible à l'adresse suivante :
https://www.ravensburger.co.uk/gameinstructions/ecm/Spielanleitungen/26646%20anl%202050897_2.pdf

On propose ci-dessous une version légèrement simplifiée du jeu.

Le [plateau](./board.png) représente le centre de Londres et son réseau de
transport, avec des stations numérotées de 1 à 199. Les connexions entre les
stations sont de quatre types : bus (turquoise), taxi (jaune), métro (rouge) et
ferry (noir). Les trois premiers types sont utilisables par les détectives et
Mister X, mais le quatrième n'est utilisable que par Mister X. Sur le plateau,
la représentation peut prendre trois formes différentes selon que la station :

- n'est accessible qu'en taxi - elle est dans ce cas uniformément jaune ;
- est accessible en taxi et bus - elle est dans ce cas jaune et turquoise ;
- est accessible en taxi, bus et métro - elle est dans ce cas jaune, turquoise
  et rouge;
- (l'accès en ferry n'est pas représenté graphiquement sur la station).

Le jeu oppose Mister X, qui utilise un pion de couleur noire, à un à cinq
détectives dont les couleurs possibles sont : orange, bleu, vert, rouge, et
violet.

Les positions initiales des détectives et de Mister X sont déterminées
aléatoirement. Les détectives placent leurs pions sur leurs positions initiales,
mais la position initiale de Mister X n'est pas révélée. Chaque détective
reçoit : 4 tickets de métro, 8 tickets de bus et 11 tickets de taxi. Les autres
tickets (23 tickets de métro, 45 tickets de bus et 57 tickets de taxi avant
distribution) sont placés dans la pioche. Mister X reçoit 3 tickets doubles et
5 tickets noirs.

À chaque tour :

- Mister X se déplace :
  - soit en utilisant un ticket de la pioche correspondant au mode de transport
    pour suivre un lien reliant deux stations ;
  - soit en consommant un ticket noir, qui lui permet de suivre n'importe quel
    lien de transport (y compris en ferry) ;
  - soit en consommant un ticket double, qui lui permet de faire deux
    déplacements successifs, suivant les possibilités des deux items précédents ;
- chaque détective, successivement, se déplace :
  - en consommant l'un des tickets qu'il détient correspondant au mode de transport
    pour suivre un lien reliant deux stations ;
  - en plaçant le ticket consommé dans la pioche.

Mister X, comme chaque détective, est tenu de se déplacer à chaque tour. La
seule exception concerne les détectives dont la situation (station et tickets
disponibles) rend tout déplacement impossible. Deux détectives ne peuvent se
trouver à la même station en même temps.

La partie prend fin lorsque :

- le 23 ème tour a été atteint ou plus aucun détective ne peut se déplacer,
  dans ce cas Mister X gagne ;
- un détective se trouve à la même station que Mister X, dans ce cas les
  détectives gagnent collectivement.


## Éléments donnés

Les fichiers suivants contiennent les informations de base sur le jeu :

- [board_data.py](./board_data.py) contient la définition du réseau de transport,
  avec les définitions des stations et des connexions entre elles ;
- [rules.py](./rules.py) définit quelques constantes symboliques, avec par
  exemple les tickets initialement disponibles pour les différents types
  de joueurs, ou les positions de départ possibles.


## Exercice : représentation du plateau

La première étape consiste à compléter le fichier [board.py](./board.py) afin de
définir les éléments nécessaires pour représenter le plateau de jeu. Le
constructeur de la classe `Board` attend les informations à propos des stations
et connexions selon l'encodage décrit dans le fichier
[board_data.py](./board_data.py). Le constructeur doit lever l'exception
`InvalidBoard` si les données passées sont incohérentes (par exemple si une
connexion fait référence à une station inexistante).


## Exercice : représentation des joueurs

La seconde étape consiste à compléter le fichier [player.py](./player.py) afin
de définir les éléments nécessaires pour représenter les joueurs participant à
la partie. Outre les éléments ci-dessus, on stockera le nom de chaque joueur.


## Exercice optionnel : représentation des coups possibles

La troisième étape consiste à compléter le fichier [move.py](./move.py) afin de
définir les éléments nécessaires pour représenter les coups possibles pour les
détectives et pour Mister X. On **ne** s'intéresse **pas** ici au calcul des coups
possibles dans une situation donnée, seulement à leur représentation.


## Exercice optionnel : classe principale

La quatrième étape consiste à compléter le fichier [scotland_yard.py](./scotland_yard.py)
afin d'écrire le constructeur de la classe `Game` de telle sorte que l'état de
l'instance correspond à l'état initial de la partie.



# TDLOG: first session

This file contains the exercises for the first session of the course. The
objective is to produce a code of quality (readability, naming, comments) rather
than to cover as many exercises as possible. The exercises must be done in teams
of two, and in English (function and variable names, comments). During this
session, we are interested in modeling the basic elements of a
slightly-simplified version of the game published as Scotland Yard / Mister X.
By modeling, we mean defining the classes to represent the elements of the game.


## Board game

The [Scotland Yard / Mister X](https://en.wikipedia.org/wiki/Scotland_Yard_(board_game))
game has been published by Ravensburger under several variants. It is a board
game during which a handful of detectives try to catch a fugitive, Mister X. A
version of the rules is available at the following address:
https://www.ravensburger.co.uk/gameinstructions/ecm/Spielanleitungen/26646%20anl%202050897_2.pdf

Below is a slightly simplified version of the game.

The [board](./board.png) represents the center of London and its transportation
network, with stations numbered from 1 to 199. The connections between the
stations are of four kinds : bus (turquoise), taxi (yellow), underground (red),
and ferry (black). The first three kinds can be used by the detectives and
Mister X, but the fourth kind can only be used by Mister X. On the board, the
representation can take one of three forms depending on whether the station:

- can be accessed only by taxi - it is in this case yellow;
- can be accessed by taxi and bus - it is in this case yellow and turquoise;
- can be accessed by taxi, bus, or underground - it is in this case yellow,
  turquoise, and red;
- (ferry access is not represented graphically).

The game pits Mister X, represented by a black pawn, against one to five
detectives whose possible pawn colors are: orange, blue, green, red, and purple.

The initial positions of the detectives and of Mister X are determined randomly.
The detectives place their pawns on the board, but the initial position of
Mister X is not revealed. Each detective gets: 4 underground tickets, 8 bus
tickets, and 11 taxi tickets. The other tickets (23 underground tickets, 45 bus
tickets, and 57 taxi tickets, before the detective take theirs) are placed into
the supply pile. Mister X gets three 3 double tickets and 5 black tickets.

During each turn:

- Mister X moves:
  - either by using a ticket from the supply pile corresponding to the mode of
    transportation to follow a connection between two stations;
  - or by consuming a black ticket, to follow any connection (including a ferry one);
  - or by consuming a double ticket, allowing them to move twice in a row, according
    to the possibilities of one of the previous two items;
- each detective, one after the other, moves:
  - by consuming a ticket they hold corresponding to the mode of transportation to
    follow a connection between two stations;
  - by placing the consumed ticket into the supply pile.

Mister X, as well as each detective, has to move at each turn. The only
exception is for detectives in such circumstances (station and available
tickets) that no move is possible. Two detectives cannot be at the same station
at the same time.

The game ends when:

- the 23rd turn has been reached or no detectives can move, in which case Mister X
  wins;
- a detective is at the same station as Mister X, in which case the detectives
  collectively win.


## Predefined elements

The following files contain the basic elements of the game:

- [board_data.py](./board_data.py) contains the definition of transportation network,
  with the definitions or the stations and the connections between them;
- [rules.py](./rules.py) defines a couple of symbolic constants, for instance, the
  number of tickets given at the start of the game to the various kinds of players,
  or the possible starting positions.


## Exercise: board representation

The first step is to complete the [board.py](./board.py) file in order to define the
elements needed to represent the board. The constructor of the `Board` class
expects the information about the stations and connections as encoded in the
[board_data.py](./board_data.py) file. The constructor must raise the
`InvalidBoard` exception if the passed data is inconsistent (for instance if
a connection refers to a nonexistent station).


## Exercise: player representation

The second step is to complete the [player.py](./player.py) file in order to
define the elements needed to represent the player participating in a game.
In addition to the elements above, we want to store the name of each player.


## Optional exercise: représentation des coups possibles

The third step is to complete the [move.py](./move.py) file in order to define
the elements needed to represent the legal moves for the detectives and
Mister X. We are only interested in the representation of the moves, **not** the
computation of the legal moves in a given state of the game.


## Optional exercise: classe principale

The fourth step is to complete the [scotland_yard.py](./scotland_yard.py) file
in order to implement the constructor of the `Game` class in such a way that the
state of the instance represents the initial state of the game.
