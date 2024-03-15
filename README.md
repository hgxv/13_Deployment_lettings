Résumé
======

Site web d'Orange County Lettings

Développement local
===================

Prérequis
---------

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande ``python`` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

macOS / Linux
-------------

Cloner le repository
~~~~~~~~~~~~~~~~~~~~

- ``cd /path/to/put/project/in``
- ``git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git``

Créer l'environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``cd /path/to/Python-OC-Lettings-FR``
- ``python -m venv venv``
- ``apt-get install python3-venv`` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement ``source venv/bin/activate``
- Confirmer que la commande ``python`` exécute l'interpréteur Python dans l'environnement virtuel ``which python``
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure ``python --version``
- Confirmer que la commande ``pip`` exécute l'exécutable pip dans l'environnement virtuel, ``which pip``
- Pour désactiver l'environnement, ``deactivate``

- Create a .env file at the root and add your django SECRET_KEY

Exécuter le site
~~~~~~~~~~~~~~~~

`python manage.py runserver`

Aller sur http://localhost:8000 dans un navigateur.
Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

Linting
~~~~~~~

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

Tests unitaires
~~~~~~~~~~~~~~~

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

Base de données
~~~~~~~~~~~~~~~

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

Panel d'administration
~~~~~~~~~~~~~~~~~~~~~~

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`


Déploiement
===========

Prérequis
---------

- Compte Sentry
- Compte Dockerhub
- Compte CircleCI
- Compte Heroku
- Heroku CLI

Sentry
------
- Dans les paramètres du projet, dans Client Keys, ajoutez le code DSN au fichier .env

CircleCI
--------
Dans les variables d'environnement du projet, ajoutez les variables suivantes:

- DOCKER_IMAGE --> docker_username/nom_du_projet
- DOCKER_USER --> Votre nom d'utilisateur docker
- DOCKER_PASS --> Votre mot de passe docker
- HEROKU_TOKEN --> ``heroku auth:token``
- SECRET_KEY --> La clef du projet Django
- SENTRY_DSN --> La clef DSN disponible sur Sentry

Heroku
------
Dans les variables d'environnement, ajoutez les variables suivantes :

- PORT --> 8000
- SECRET_KEY --> La clef du projet Django
- SENTRY_DSN --> La clef DSN disponible sur Sentry
- HEROKU_TOKEN --> ``heroku auth:token``


Une fois les comptes configurés, chaque fois que du code est pushé sur GitHub,
CircleCI s'occupe d'effectuer les tests et le linting.

Si vous êtes sur la branche master, et que les deux étapes précédentes
sont valides, le déploiement se lance et le site se met à jour.
