"""models/review.py

Modèle SQLAlchemy enrichi représentant un avis utilisateur dans HBnB.
Hérite de BaseModel. Les relations ne sont pas encore mappées (pas de ForeignKey ni de relationship).
"""

from app import db
from app.models.base import BaseModel
from app.models.user import User
from app.models.place import Place


class Review(BaseModel):
    """
    Modèle représentant un avis utilisateur sur un lieu.

    Hérite de :
    - BaseModel : fournit id, created_at, updated_at

    Attributs :
    - text (str) : contenu de l'avis (obligatoire, max 500 caractères)
    - rating (int) : note sur 5 (obligatoire, entre 1 et 5)
    - author (User) : l'utilisateur ayant rédigé l'avis (non mappé pour l’instant)
    - place (Place) : le lieu concerné par l’avis (non mappé pour l’instant)
    """

    __tablename__ = "reviews"

    text = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, text, rating, author, place):
        super().__init__()
        self.text = self.validate_text(text, "Text")
        self.rating = self.validate_rating(rating, "Rating")
        self.author = self.validate_author(author, "Author")
        self.place = self.validate_place(place, "Place")

    # ========== VALIDATIONS ==========

    def validate_text(self, value, field_name):
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")
        value = value.strip()
        if not value:
            raise ValueError(f"{field_name} is required")
        if len(value) > 500:
            raise ValueError(f"{field_name} must be at most 500 characters")
        return value

    def validate_rating(self, value, field_name):
        if not isinstance(value, int):
            raise TypeError(f"{field_name} must be an integer")
        if not (1 <= value <= 5):
            raise ValueError(f"{field_name} must be between 1 and 5")
        return value

    def validate_author(self, value, field_name):
        if not isinstance(value, User):
            raise TypeError(f"{field_name} must be an instance of User")
        return value

    def validate_place(self, value, field_name):
        if not isinstance(value, Place):
            raise TypeError(f"{field_name} must be an instance of Place")
        return value

    # ========== PROPRIÉTÉS EXTERNES POUR L'API ==========

    @property
    def user_id(self):
        """Permet d'exposer l'ID de l’auteur via user_id dans l’API."""
        return self.author.id if self.author else None

    @property
    def place_id(self):
        """Permet d'exposer l'ID du lieu via place_id dans l’API."""
        return self.place.id if self.place else None

    # ========== MÉTHODES MÉTIER ==========

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key == "text":
                self.text = self.validate_text(value, "Text")
            elif key == "rating":
                self.rating = self.validate_rating(value, "Rating")
            elif key == "author":
                self.author = self.validate_author(value, "Author")
            elif key == "place":
                self.place = self.validate_place(value, "Place")

    # ========== REPRÉSENTATIONS ==========

    def __repr__(self):
        return f"<Review {self.id}: {self.rating}⭐ by {self.user_id}>"

    def __str__(self):
        return (
            f"[Review] {self.author.first_name} {self.author.last_name} "
            f"sur {self.place.title} : {self.rating}⭐ - \"{self.text}\""
        )

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            "user_id": self.user_id,
            "place_id": self.place_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
