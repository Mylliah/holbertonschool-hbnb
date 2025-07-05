"""models/amenity.py

Modèle représentant une commodité dans l'application HBnB.
Contient également la table d'association many-to-many avec Place.
"""

from app.extensions import db
from app.models.base import BaseModel

# Table d'association many-to-many entre Place et Amenity
place_amenity = db.Table(
    'place_amenity',
    db.Column('place_id', db.String(60), db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.String(60), db.ForeignKey('amenities.id'), primary_key=True)
)

class Amenity(BaseModel):
    """
    Modèle représentant une commodité associée à un hébergement.

    Hérite de :
    - BaseModel : fournit id, created_at, updated_at

    Attributs :
    - name (str) : nom de la commodité (obligatoire, max 50 caractères)
    - places : relation many-to-many avec Place
    """

    __tablename__ = "amenities"

    name = db.Column(db.String(50), nullable=False)

    # 🔗 Relation vers Place (many-to-many, via table d'association)
    places = db.relationship(
        "Place",  # nom du modèle cible (doit être exactement le même nom que la classe Place)
        secondary=place_amenity,
        backref=db.backref("amenities", lazy=True),
        lazy="subquery"
    )

    def __init__(self, name):
        super().__init__()
        self.name = self.validate_name(name, "Name")

    def validate_name(self, value, field_name):
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")
        value = value.strip()
        if not value:
            raise ValueError(f"{field_name} is required")
        if len(value) > 50:
            raise ValueError(f"{field_name} must be at most 50 characters")
        return value

    def __repr__(self):
        return f"<Amenity {self.id}: {self.name}>"

    def __str__(self):
        return f"Commodité : {self.name}"
