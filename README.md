[ Projet ReadOrganizer ]

Ce projet vise à améliorer la compression des fichiers de lecture issus du séquençage haut débit en réorganisant ces lectures de manière à optimiser l'efficacité de la compression via le compresseur générique gzip. 
Le script proposé s’appuie sur l’utilisation d’un génome de référence pour réorganiser les fichiers de reads de manière à les rendre plus efficients dans la compression. Une compression sans cette étape de réorganisation permet de diviser la taille du fichier avec un facteur d’environ 3. Cet outil propose 2 approches de mapping appelées méthodes 1 et méthodes 2 permettant de s’adapter au mieux aux jeux de données. L’idée est d’aligner chacun des reads sur le génome en utilisant une méthode de mapping pour déterminer leurs positions.

L’outil est un ensemble de fichiers python développé en python 3.10.11 : 
BTW_package.py
tools_karkkainen_sanders.py
read.py
ReadOrganizer.py

Ces scripts doivent se trouver dans le même répertoire que votre génome de référence et vos données de séquençage, les deux au format fasta. L’outil se lance dans un terminal de la manière suivante :

python .\ReadOrganizer.py -i .\sequencing_data.fasta -r .\reference_genome.fasta -k 5 -m 1 -o reorganized_reads_k5_m1.fasta

Exemple :
python .\ReadOrganizer.py -i .\humch1_100Kb_reads_5x.fasta -r .\humch1_100Kb.fasta -k 10 -m 1 -o .\humch1_100Kb_reads_5x_reorganized.fasta

Voici les paramètres configurables : 
i : le fichier de reads issus du séquençage
r : le génome à utiliser en référence
k : la taille de la seed à utiliser pour le mapping
m : la méthode de mapping à utiliser 1 ou 2
o : le nom du fichier de sortie de vos reads réorganisés


Contact développeurs :
Yann LEFRANCOIS, yann.lefrancois@etudiant.univ-rennes.fr
Victor BERTHOD, victor.berthod@etudiant.univ-rennes.fr
