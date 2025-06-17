import pytest
from datetime import datetime
from app.models.place import Place
from app.models.user import User
from app.models.review import Review
from app.models.amenity import Amenity


def test_create_valid_amenity():
    """
    Vérifie qu’un Amenity valide peut être créé sans erreur,
    et que tous les attributs sont correctement initialisés.
    """

    print(">>> Création d’un Amenity valide avec name = 'Wi-Fi'")
    amenity = Amenity(name="Wi-Fi")

    print(">>> Objet créé :", amenity)

    print(">>> Attributs hérités :")
    print("- id =", amenity.id)
    print("- created_at =", amenity.created_at)
    print("- updated_at =", amenity.updated_at)

    print(">>> Attribut spécifique :")
    print("- name =", amenity.name)

    print(">>> Test des méthodes d’affichage :")
    print("- repr() :", repr(amenity))
    print("- str()  :", str(amenity))

    assert isinstance(amenity, Amenity)
    assert isinstance(amenity.id, str)
    assert isinstance(amenity.created_at, datetime)
    assert isinstance(amenity.updated_at, datetime)
    assert amenity.name == "Wi-Fi"


def test_create_amenity_without_name():
    """
    Vérifie qu’une exception TypeError est levée si aucun nom n’est fourni.
    """

    print(">>> Tentative de création d’un Amenity sans passer de name...")

    with pytest.raises(TypeError) as exc_info:
        amenity = Amenity()  # Pas de name fourni

    print(">>> Exception capturée :", exc_info.value)


