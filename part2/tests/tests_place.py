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


def test_create_place_with_non_string_title():
    """
    Vérifie qu'une TypeError est levée si title n'est pas une chaîne.
    """
    owner = User(first_name="Lando", last_name="Calrissian", email="lando@cloudcity.com")
    description = "Appartement perché"
    price = 120.0
    latitude = 45.0
    longitude = 5.0

    # Cas 1 : title est un entier
    with pytest.raises(TypeError) as e1:
        Place(title=123, description=description, price=price, latitude=latitude, longitude=longitude, owner=owner)
    print("Erreur attendue (title = int) :", e1.value)

    # Cas 2 : title est un float
    with pytest.raises(TypeError) as e2:
        Place(title=4.5, description=description, price=price, latitude=latitude, longitude=longitude, owner=owner)
    print("Erreur attendue (title = float) :", e2.value)

    # Cas 3 : title est une liste
    with pytest.raises(TypeError) as e3:
        Place(title=["Maison"], description=description, price=price, latitude=latitude, longitude=longitude, owner=owner)
    print("Erreur attendue (title = list) :", e3.value)

    # Cas 4 : title est un booléen
    with pytest.raises(TypeError) as e4:
        Place(title=True, description=description, price=price, latitude=latitude, longitude=longitude, owner=owner)
    print("Erreur attendue (title = bool) :", e4.value)


def test_create_place_with_title_too_long():
    """
    Vérifie qu'une ValueError est levée si le titre dépasse 100 caractères.
    """
    owner = User(first_name="Leia", last_name="Organa", email="leia@rebellion.org")
    description = "Palais luxueux dans les nuages"
    price = 250.0
    latitude = 42.5
    longitude = 3.2

    # Génère un titre de 101 caractères
    long_title = "L" * 101

    with pytest.raises(ValueError) as e:
        Place(
            title=long_title,
            description=description,
            price=price,
            latitude=latitude,
            longitude=longitude,
            owner=owner
        )

    print("Erreur attendue (title > 100 caractères) :", e.value)


def test_create_place_with_invalid_price_value():
    """
    Vérifie qu'une ValueError est levée si price est 0 ou négatif.
    """
    owner = User(first_name="Han", last_name="Solo", email="han@falcon.co")
    title = "Appartement Corellien"
    description = "Avec vue sur les chantiers orbitaux"
    latitude = 44.0
    longitude = 1.5

    # Cas 1 : price = 0
    with pytest.raises(ValueError) as e1:
        Place(title=title, description=description, price=0, latitude=latitude, longitude=longitude, owner=owner)
    print("Erreur attendue (price = 0) :", e1.value)

    # Cas 2 : price = -10
    with pytest.raises(ValueError) as e2:
        Place(title=title, description=description, price=-10, latitude=latitude, longitude=longitude, owner=owner)
    print("Erreur attendue (price < 0) :", e2.value)


def test_create_place_with_invalid_latitude():
    """
    Vérifie qu'une ValueError est levée si latitude est hors de l'intervalle [-90, 90].
    """
    owner = User(first_name="Padmé", last_name="Amidala", email="padme@naboo.gov")
    title = "Villa lacustre"
    description = "Située sur les lacs de Naboo"
    price = 300.0
    longitude = 6.6

    # Cas 1 : latitude > 90
    with pytest.raises(ValueError) as e1:
        Place(title=title, description=description, price=price, latitude=91.0, longitude=longitude, owner=owner)
    print("Erreur attendue (latitude > 90) :", e1.value)

    # Cas 2 : latitude < -90
    with pytest.raises(ValueError) as e2:
        Place(title=title, description=description, price=price, latitude=-91.0, longitude=longitude, owner=owner)
    print("Erreur attendue (latitude < -90) :", e2.value)


def test_create_place_with_invalid_longitude():
    """
    Vérifie qu'une ValueError est levée si longitude est hors de l'intervalle [-180, 180].
    """
    owner = User(first_name="Bail", last_name="Organa", email="bail@alderaan.gov")
    title = "Domaine royal"
    description = "Résidence de la famille Organa"
    price = 400.0
    latitude = 47.2

    # Cas 1 : longitude > 180
    with pytest.raises(ValueError) as e1:
        Place(title=title, description=description, price=price, latitude=latitude, longitude=181.0, owner=owner)
    print("Erreur attendue (longitude > 180) :", e1.value)

    # Cas 2 : longitude < -180
    with pytest.raises(ValueError) as e2:
        Place(title=title, description=description, price=price, latitude=latitude, longitude=-181.0, owner=owner)
    print("Erreur attendue (longitude < -180) :", e2.value)


def test_create_place_with_invalid_owner():
    """
    Vérifie qu'une TypeError est levée si owner n'est pas une instance de User.
    """
    title = "Caserne des clones"
    description = "Située sur Kamino"
    price = 500.0
    latitude = -33.0
    longitude = 151.0

    # Cas 1 : owner = string
    with pytest.raises(TypeError) as e1:
        Place(title=title, description=description, price=price, latitude=latitude, longitude=longitude, owner="not_a_user")
    print("Erreur attendue (owner = str) :", e1.value)

    # Cas 2 : owner = int
    with pytest.raises(TypeError) as e2:
        Place(title=title, description=description, price=price, latitude=latitude, longitude=longitude, owner=42)
    print("Erreur attendue (owner = int) :", e2.value)

    # Cas 3 : owner = float
    with pytest.raises(TypeError) as e3:
        Place(title=title, description=description, price=price, latitude=latitude, longitude=longitude, owner=3.14)
    print("Erreur attendue (owner = float) :", e3.value)

    # Cas 4 : owner = None
    with pytest.raises(TypeError) as e4:
        Place(title=title, description=description, price=price, latitude=latitude, longitude=longitude, owner=None)
    print("Erreur attendue (owner = None) :", e4.value)

    # Cas 5 : owner = dict
    with pytest.raises(TypeError) as e5:
        Place(title=title, description=description, price=price, latitude=latitude, longitude=longitude, owner={"id": "abc"})
    print("Erreur attendue (owner = dict) :", e5.value)


def test_create_place_with_invalid_lat_or_long_type():
    """
    Vérifie qu'une TypeError est levée si latitude ou longitude ne sont pas des float.
    """
    owner = User(first_name="Obi-Wan", last_name="Kenobi", email="kenobi@jedi.org")
    title = "Refuge sur Tatooine"
    description = "Lieu tenu secret"
    price = 100.0

    # Cas latitude : string
    with pytest.raises(TypeError) as e1:
        Place(title=title, description=description, price=price, latitude="34.0", longitude=12.0, owner=owner)
    print("Erreur attendue (latitude = str) :", e1.value)

    # Cas latitude : int
    with pytest.raises(TypeError) as e2:
        Place(title=title, description=description, price=price, latitude=34, longitude=12.0, owner=owner)
    print("Erreur attendue (latitude = int) :", e2.value)

    # Cas longitude : string
    with pytest.raises(TypeError) as e3:
        Place(title=title, description=description, price=price, latitude=34.0, longitude="12.0", owner=owner)
    print("Erreur attendue (longitude = str) :", e3.value)

    # Cas longitude : int
    with pytest.raises(TypeError) as e4:
        Place(title=title, description=description, price=price, latitude=34.0, longitude=12, owner=owner)
    print("Erreur attendue (longitude = int) :", e4.value)


def test_create_place_with_invalid_price_type():
    """
    Vérifie qu'une TypeError est levée si price n'est pas un float ou un int.
    """
    owner = User(first_name="Mace", last_name="Windu", email="windu@council.jedi")
    title = "Tour du Temple"
    description = "Niveau 5, aile ouest"
    latitude = 34.0
    longitude = 18.0

    # Cas 1 : price = string
    with pytest.raises(TypeError) as e1:
        Place(title=title, description=description, price="200", latitude=latitude, longitude=longitude, owner=owner)
    print("Erreur attendue (price = str) :", e1.value)

    # Cas 2 : price = list
    with pytest.raises(TypeError) as e2:
        Place(title=title, description=description, price=[200], latitude=latitude, longitude=longitude, owner=owner)
    print("Erreur attendue (price = list) :", e2.value)

    # Cas 3 : price = None
    with pytest.raises(TypeError) as e3:
        Place(title=title, description=description, price=None, latitude=latitude, longitude=longitude, owner=owner)
    print("Erreur attendue (price = None) :", e3.value)

    # Cas 4 : price = bool
    with pytest.raises(TypeError) as e4:
        Place(title=title, description=description, price=True, latitude=latitude, longitude=longitude, owner=owner)
    print("Erreur attendue (price = bool) :", e4.value)

    # Cas 5 : price = dict
    with pytest.raises(TypeError) as e5:
        Place(title=title, description=description, price={"value": 200}, latitude=latitude, longitude=longitude, owner=owner)
    print("Erreur attendue (price = dict) :", e5.value)
