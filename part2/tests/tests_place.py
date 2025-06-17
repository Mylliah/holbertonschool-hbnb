import pytest
import time
from app.models.place import Place
from app.models.user import User


def test_create_valid_place():
    """
    Vérifie qu'une instance valide de Place peut être créée correctement.
    """
    owner = User(first_name="Han", last_name="Solo", email="han@falcon.space")
    place = Place(
        title="Cabine du Faucon",
        description="Un lieu mythique dans la galaxie.",
        price=500.0,
        latitude=12.34,
        longitude=56.78,
        owner=owner
    )

    # ✅ Vérifications
    assert isinstance(place, Place)
    assert place.title == "Cabine du Faucon"
    assert place.description == "Un lieu mythique dans la galaxie."
    assert place.price == 500.0
    assert place.latitude == 12.34
    assert place.longitude == 56.78
    assert place.owner == owner
    assert place.reviews == []
    assert place.amenities == []

    # 🖨️ Affichage complet
    print("\n✅ Création d'un logement réussie :")
    print(f"→ Titre : {place.title}")
    print(f"→ Description : {place.description}")
    print(f"→ Prix : {place.price}")
    print(f"→ Latitude : {place.latitude}")
    print(f"→ Longitude : {place.longitude}")
    print(f"→ Owner : {place.owner}")
    print(f"→ Reviews : {place.reviews}")
    print(f"→ Amenities : {place.amenities}")


def test_create_place_missing_required_fields():
    """
    Vérifie qu'une exception est levée si on tente de créer un Place
    sans titre, prix ou propriétaire.
    """
    owner = User(first_name="Lando", last_name="Calrissian", email="lando@cloud.city")

    # Manque le titre
    with pytest.raises(TypeError):
        Place(
            price=100.0,
            latitude=0.0,
            longitude=0.0,
            owner=owner
        )

    # Manque le prix
    with pytest.raises(TypeError):
        Place(
            title="Cloud City Loft",
            latitude=0.0,
            longitude=0.0,
            owner=owner
        )

    # Manque le owner
    with pytest.raises(TypeError):
        Place(
            title="Cloud City Loft",
            price=100.0,
            latitude=0.0,
            longitude=0.0
        )

    print("\n Exceptions correctement levées pour les champs manquants :")
    print("→ Erreur sans titre ✔")
    print("→ Erreur sans prix ✔")
    print("→ Erreur sans propriétaire ✔")


def test_create_place_with_empty_fields():
    """
    Vérifie qu'une erreur est levée si certains champs de Place sont vides ou None.
    """
    owner = User(first_name="Lando", last_name="Calrissian", email="lando@cloudcity.com")

    # Cas 1 : title vide → ValueError
    with pytest.raises(ValueError) as e1:
        Place(title="", description="Lieu chic", price=120.0, latitude=45.0, longitude=5.0, owner=owner)
    print("Erreur attendue (title vide) :", e1.value)

    # Cas 2 : title = None → TypeError
    with pytest.raises(TypeError) as e2:
        Place(title=None, description="Lieu chic", price=120.0, latitude=45.0, longitude=5.0, owner=owner)
    print("Erreur attendue (title None) :", e2.value)

    # Cas 3 : description vide → ValueError
    with pytest.raises(ValueError) as e3:
        Place(title="Cloud City", description="", price=120.0, latitude=45.0, longitude=5.0, owner=owner)
    print("Erreur attendue (description vide) :", e3.value)

    # Cas 4 : description = None → TypeError
    with pytest.raises(TypeError) as e4:
        Place(title="Cloud City", description=None, price=120.0, latitude=45.0, longitude=5.0, owner=owner)
    print("Erreur attendue (description None) :", e4.value)

    # Cas 5 : price = None → TypeError
    with pytest.raises(TypeError) as e5:
        Place(title="Cloud City", description="Ville flottante", price=None, latitude=45.0, longitude=5.0, owner=owner)
    print("Erreur attendue (price None) :", e5.value)