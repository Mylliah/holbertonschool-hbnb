# tests/tests_place.py

import pytest
from app.models.user import User
from app.models.place import Place


def test_create_valid_place():
    """
    Vérifie qu'une instance valide de Place est correctement initialisée.
    """
    owner = User(first_name="Bail", last_name="Organa", email="bail@alderaan.org")

    place = Place(
        title="Palais Royal",
        description="Vue sur les cascades de Theed",
        price=180.5,
        latitude=44.5,
        longitude=2.3,
        owner=owner
    )

    assert isinstance(place, Place)
    assert place.title == "Palais Royal"
    assert place.description == "Vue sur les cascades de Theed"
    assert place.price == 180.5
    assert place.latitude == 44.5
    assert place.longitude == 2.3
    assert place.owner == owner
    assert place.reviews == []
    assert place.amenities == []
    assert place.id is not None
    assert place.created_at is not None
    assert place.updated_at is not None
