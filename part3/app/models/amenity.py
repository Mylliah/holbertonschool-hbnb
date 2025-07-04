"""models/amenity.py

Définit la classe Amenity, représentant une commodité disponible
dans un lieu de l'application HBnB.
Cette classe hérite de BaseModel.
"""

# Import de la classe de base
from app.models.base import BaseModel
from app.extensions import db
import uuid
from app import db
from app.models.base import BaseModel


# Table d'association many-to-many entre Place et Amenity
place_amenity = db.Table(
    'place_amenity',
    db.Column('place_id', db.String(36), db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.String(36), db.ForeignKey('amenities.id'), primary_key=True)
)

class Amenity(BaseModel):
    """
    Modèle représentant une commodité associée à un hébergement.

    Hérite de :
    - BaseModel : fournit id, created_at, updated_at

    Attributs :
    - name (str) : nom de la commodité (obligatoire, max 50 caractères)
    """

    __tablename__ = "amenities"

    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        super().__init__()
        self.name = self.validate_name(name, "Name")

    # ==========================
    # MÉTHODE DE VALIDATION
    # ==========================

    def validate_name(self, value, field_name):
        """
        Valide le nom de la commodité : str non vide, max 50 caractères.
        """
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")
        value = value.strip()
        if not value:
            raise ValueError(f"{field_name} is required")
        if len(value) > 50:
            raise ValueError(f"{field_name} must be at most 50 characters")
        return value

    # ==========================
    # MÉTHODE TECHNIQUE
    # ==========================

    def __repr__(self):
        """
        Représentation technique de l'amenity, utile pour le debug.
        Exemple : <Amenity 78c1... - Wi-Fi>
        """
        return f"<Amenity {self.id}: {self.name}>"

    def __str__(self):
        """
        Affichage lisible d'une commodité.
        Exemple : Commodité : Wi-Fi
        """
        return f"Commodité : {self.name}"

class Amenity(db.Model):
    __tablename__ = 'amenities'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)

    # Ajout de la relation avec PlaceModel
    places = db.relationship(
        'PlaceModel',
        secondary=place_amenity,
        back_populates='amenities'
    )

    def __repr__(self):
        return f"<Amenity {self.name}>"
