Membres du groupe :

JEGATHASAN Tamilselvan, DUCLAUD Jordan, LONGOBARDI Lucas

## I. Création du projet :
Avant de commencer, nous avons lancé une application qui nous permettait d'insérer du code. Pour notre part, nous avons utilisé Visual Studio Code.

Voici les commandes que nous avons exécutées dans un premier temps :

Créer une nouvelle application

```
python manage.py startapp notes_app Aller dans le répertoire de l'application
```

```
cd notes_app
```

## II. Déploiement des classes :
Ensuite, nous avons lancé la commande "python manage.py startapp notes_app" qui a permis dans notre dossier de créer une application. Avec cette commande, plusieurs fichiers .py ont été créés, et nous nous sommes concentrés sur celui se situant dans notes_app > models.py. À cet endroit, nous avons importé les trois classes qui sont "matières", "étudiants" ainsi que "notations".

Pour terminer ce deuxième chapitre, nous avons effectué l'application des migrations avec les commandes suivantes :

```
python manage.py makemigrations python manage.py migrate
```

## III. Création des formulaires :
Nous avons créé un formulaire que nous avons nommé forms.py dans notes_app, ce qui a permis d'importer les variables Matières, Étudiant et la notation. Par la suite, dans notes_app > Views.py, nous avons alimenté ce fichier afin de traiter les requêtes des trois classes définies avant.


## IV. Alimentation du fichier views.py
C'est à cet endroit que nous avons défini les fonctions de vue qui étaient responsables de traiter les requêtes HTTP.


## V. Création des Templates HTML :
Nous avons créé des templates HTML dans un dossier que nous avons nommé "Templates", avec les commandes suivantes : Nous avons créé un dossier templates dans le répertoire de notre application notes_app :

```
bash Copy code cd notes_app mkdir templates Cela a créé un dossier templates à l'intérieur de notre application Django.
```

Structure des Templates : Nous avons créé un sous-dossier pour chaque modèle principal (matières, étudiants, notations).

```
cd templates mkdir matieres mkdir etudiants mkdir notations Nous avons également créé un dossier includes pour stocker les éléments réutilisables, tels que l'en-tête et le pied de page. (Il s'agissait de notre base)
```

```
mkdir includes Après cela, nous avons ajouté des fichiers .html que nous avons alimentés. Après cela, nous avons dû configurer le fichier views.py afin de pouvoir utiliser ces templates.

```

## VI. Ajout des URL :
Nous avons ajouté les liens dans le dossier template via les différents fichiers nécessaires.


## VII. Ajout des URLs dans les fichiers concernés :
Pour finir, nous avons dû mettre en place les URLs afin qu'ils soient importés sur le site.


## VIII. Tester l'application :
Avec la commande python manage.py runserver, l'application était censée démarrer.

Note : Une erreur a été rencontrée, nécessitant l'ajout de lignes dans notre models.py pour chaque variable "Matiere", "Etudiant" et "Notation".
