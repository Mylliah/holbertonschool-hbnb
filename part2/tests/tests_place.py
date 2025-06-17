import pytest
from app.models.place import Place
from app.models.user import User


def test_create_valid_place():
    """
    Vérifie qu'un Place valide peut être créé sans erreur,
    et que ses attributs sont correctement initialisés.
    """
    user = User(first_name="Padmé", last_name="Naberrie", email="padme@senate.repub")

    place = Place(
        title="Appartement de Naboo",
        description="Résidence royale avec vue sur le lac",
        price=250.0,
        latitude=43.5,
        longitude=7.1,
        owner=user
    )

    # Debug
    print("[DEBUG] Created place →", place)
    print("[INFO] title =", place.title)
    print("[INFO] owner =", place.owner)
    print("[INFO] id =", place.id)
    print("[INFO] created_at =", place.created_at)

    # Assertions
    assert isinstance(place, Place)
    assert place.title == "Appartement de Naboo"
    assert place.price == 250.0
    assert place.latitude == 43.5
    assert place.longitude == 7.1
    assert place.owner == user
    assert place.id is not None
    assert place.created_at is not None
    assert place.updated_at is not None


def test_place_invalid_title_type():
    """
    Vérifie que la création d’un Place échoue si le titre n’est pas une chaîne.
    """
    user = User(first_name="Bail", last_name="Organa", email="bail@alderaan.org")

    with pytest.raises(TypeError) as excinfo:
        Place(
            title=123,  # Mauvais type
            description="Refuge de la Rébellion",
            price=100.0,
            latitude=45.0,
            longitude=6.0,
            owner=user
        )
    print("[INFO] Exception levée →", excinfo.value)
    assert str(excinfo.value) == "Title must be a string"


import time
from app.models.place import Place
from app.models.user import User


def test_place_update_method():
    """
    Vérifie que la méthode update() modifie correctement les attributs d'un Place.
    """
    user = User(first_name="Lando", last_name="Calrissian", email="lando@cloudcity.org")
    place = Place(
        title="Appartement dans les nuages",
        description="Vue panoramique sur Bespin",
        price=300,
        latitude=35.0,
        longitude=23.0,
        owner=user
    )

    # Attente pour s'assurer que updated_at sera différent
    time.sleep(3)
    previous_updated_at = place.updated_at

    # Mise à jour de plusieurs champs
    place.update({
        "title": "Suite royale dans les nuages",
        "price": 450,
        "description": "Suite luxueuse au-dessus de la Cité des Nuages"
    })

    assert place.title == "Suite royale dans les nuages"
    assert place.price == 450
    assert place.description == "Suite luxueuse au-dessus de la Cité des Nuages"
    assert place.updated_at > previous_updated_at
    print("[DEBUG] Place mis à jour →", place)
