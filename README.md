# RATP_Project

![plan](https://www.ratp.fr/sites/default/files/plans-lignes/Plans-essentiels/Plan-Metro.png)

FOLTYN Axel  
ROBIN Barthelemy  
CHARTIER Romain  
QUILLIOU Edouard  

Nous allons travailler sur la modélisation d'un réseau de transport (métro).  
Pour faire notre premiere simulation nous avons reflechi aux parametres que nous devions utilisé
Nous avons commencé par faire une simulation d'une ligne métro à 2 gares avec pour parametres :  
 - le pourcentage d'arrivant dans une gare (ar)
 - le pourcentage de personnes sortant de la gare apres avoir trop attendu (so)
 - Le nombre total de personne presente dans la gare au depart (N) 
 - La capacité d'un train (cm)
 - initialisatien du temps de la gare (t)
 - Le nombre de personne dans la gare a l'instant t (nb)
 - le temps d'attente entre chaque metro (ta)
 
 Nous créer les gares avec une classe :  

![capture d'écran](https://github.com/are00dynamic-2018/RATP_Project/image/capture_class.png)

![capture d'écran](image/capture_class.png)

Nous avons créer une fonction simulation qui renvoie le nombre de personne presente dans les gares en fonction du temps.  
Nous avons ensuite créer un fonction dessin afin de mettre en forme ses resultats :  
![courbe](https://github.com/are00dynamic-2018/RATP_Project/image/capture_courbe.png)
![courbe](image/capture_courbe.png)  
Pour mieux nous repartir les taches nous avons decidé de créer un TODO qui liste les différents travaux à faire.


######### src\Itineraire RATP.py & LibMetroIti.py & LibMetroCsv.py #########  

- Programme python à utiliser de préférence sur Spyder(Anaconda) ou sur un IDLE ayant les bibliothèques suivantes : os, tkinter.  
- Itineraire RATP.py est le mainfile qui rend le calcul d'itinéraire dans une interface graphique.  
- LibMetroCsv.py est la bibliothèque contenant les fonctions qui permettent de lire les fichiers .csv et de créer une liste et un dictionnaire ordonné des stations par lignes de métro.  
- LibMetroIti.py est la bibliothèque qui à partir des données extraites de LibMetroCsv.py, calcule l'itinéraire le plus court. Il contient aussi fonctions annexes.  
- .\\data\\ contient les fichiers .csv et une image pour l'interface graphique.  

######### src\ RATP_notebook_test_edouard.ipynb & LibMetroIti_NB.py & LibMetroCsv_NB.py #########  

- RATP_notebook_test_edouard.ipynb est une version test de RATP_notebook.ipynb  
Ici, on donne à chaque utilisateur du métro un itinéraire sous la forme d'une liste de listes comprenant [station-n, station-n+1, ligne, temps moyenne d'attente sur la ligne par station en seconde, capacité de la rame de la ligne].    
Par exemple :   
print(listage_stations_itineraire("PORTE DE VANVES","M13","JUSSIEU","M10"))  
[['PORTE DE VANVES', 'PLAISANCE', 'M13', 210.0, '574'], ['PLAISANCE', 'PERNETY', 'M13', 210.0, '574'], ['PERNETY', 'GAITE', 'M13', 210.0, '574'], ['GAITE', 'MONTPARNASSE', 'M13', 210.0, '574'], ['MONTPARNASSE', 'SAINT-PLACIDE', 'M4', 330.0, '574'], ['SAINT-PLACIDE', 'SAINT-SULPICE', 'M4', 330.0, '574'], ['SAINT-SULPICE', 'SAINT-GERMAIN-DES-PRES', 'M4', 330.0, '574'], ['SAINT-GERMAIN-DES-PRES', 'ODEON', 'M4', 330.0, '574'], ['ODEON', 'CLUNY-LA-SORBONNE', 'M10', 300.0, '574'], ['CLUNY-LA-SORBONNE', 'MAUBERT-MUTUALITE', 'M10', 300.0, '574'], ['MAUBERT-MUTUALITE', 'CARDINAL-LEMOINE', 'M10', 300.0, '574'], ['CARDINAL-LEMOINE', 'JUSSIEU', 'M10', 300.0, '574']]  

- LibMetroCsv_NB.py et LibMetroIti_NB.py sont des versions modifiées et complétées de LibMetroCsv.py et de LibMetroIti.py qui ont leur utilité propre pour RATP_notebook_test_edouard.ipynb (NB=notebook). On y retrouve des changements liés à l'utilisation d'un notebook et et nouvelles fonctions pour les demandes du projet. Ces fichiers seront les bibliothèques utilisées pour le projet final.  
