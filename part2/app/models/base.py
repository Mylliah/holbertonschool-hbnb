"""models/base.py

Définit la classe de base pour toutes les entités métier de l'application HBnB.
Cette classe centralise les attributs communs et fournit des méthodes
utilitaires telles que la sauvegarde (mise à jour de `updated_at`)
et la mise à jour d'attributs à partir d'un dictionnaire.

Toutes les entités (User, Place, Review, Amenity) hériteront de cette classe.
"""

# Imports nécessaires
# uuid : pour générer un identifiant unique (UUID v4) sous forme de chaîne
# datetime : pour générer les horodatages de création et mise à jour
import uuid
from datetime import datetime


class BaseModel:
    """
    Classe de base commune aux entités métier de l'application.

    Attributs publics :
    - id (str) : identifiant unique de l'instance
    (UUID v4 sous forme de chaîne)
    - created_at (datetime) : date/heure de création de l'objet
    - updated_at (datetime) : date/heure de dernière modification de l'objet

    Méthodes :
    - save() : met à jour l'attribut `updated_at`
    - update(data: dict) : met à jour les attributs depuis un dictionnaire
    """

    def __init__(self):
        """
        Constructeur commun à toutes les entités métier.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Met à jour la date de dernière modification de l'objet.
        """
        self.updated_at = datetime.now()

    def update(self, data):
        """
        Met à jour dynamiquement les attributs de l'objet
        à partir d'un dictionnaire.

        Paramètre :
        - data (dict) : dictionnaire contenant des paires clé/valeur
                        où chaque clé correspond à un attribut de l'objet
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # met à jour `updated_at`
