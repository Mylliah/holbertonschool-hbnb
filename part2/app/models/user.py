"""models/user.py

Définit la classe User, représentant un utilisateur dans l'application HBnB.
Cette classe hérite de BaseModel et ajoute les attributs spécifiques
liés à l'identité de l'utilisateur.
"""

# 📦 Imports nécessaires
# BaseModel : classe de base commune
from models.base import BaseModel


class User(BaseModel):
    """
    Classe représentant un utilisateur de la plateforme HBnB.

    Hérite de :
    - BaseModel : fournit id, created_at, updated_at

    Attributs spécifiques :
    - first_name (str) : prénom de l'utilisateur
    (obligatoire, max 50 caractères)
    - last_name (str) : nom de l'utilisateur (obligatoire, max 50 caractères)
    - email (str) : adresse e-mail (obligatoire, unique, format email standard)
    - is_admin (bool) : droits administrateur (par défaut False)
    """

    def __init__(self, first_name, last_name, email, is_admin=False):
        """
        Constructeur de la classe User.

        Paramètres :
        - first_name (str) : prénom de l'utilisateur
        (obligatoire, <= 50 caractères)
        - last_name (str) : nom de l'utilisateur
        (obligatoire, <= 50 caractères)
        - email (str) : adresse e-mail
        (obligatoire, format email standard attendu)
        - is_admin (bool, optionnel) : booléen indiquant si l'utilisateur
        est admin (défaut : False)

        À faire :
        - Appeler le constructeur parent via super()
        - Vérifier que les chaînes ne sont pas vides
        - Vérifier que les longueurs de `first_name` et `last_name` ne dépassent pas 50
        - Affecter les valeurs aux attributs
        - (Facultatif) Vérifier que l'e-mail contient au moins un "@" pour validation minimale
        """
        pass  # 🛠️ À implémenter

    def __str__(self):
        """
        Représentation en chaîne lisible pour le debug.

        À faire :
        - Retourner une chaîne affichant le prénom, le nom et l’e-mail
          Exemple : "<User John Doe - john.doe@example.com>"
        """
        pass  # 🛠️ Optionnel, mais recommandé pour les tests
