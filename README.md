# Freenet Python REST

- Pour exécuter un noeud:

        python3 algo.py <yaml> <wait/init> <value>

- Pour exécuter chaque noeud sur chaque instance:

    Le script launch.sh ne prend pas de paramètres mais doit être en présence du script sshLauncher.sh

        bash launch.sh
Pour lancer sur VM faut remplacer ligne 111 host=app.node['address'] par host="0.0.0.0"
