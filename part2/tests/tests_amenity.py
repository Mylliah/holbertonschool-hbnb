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


def test_create_amenity_with_empty_name():
    """
    Vérifie qu'une ValueError est levée si le nom est vide
    ou uniquement composé d'espaces.
    """

    print(">>> Tentative avec une chaîne vide : Amenity('')")
    with pytest.raises(ValueError) as exc1:
        Amenity("")

    print(">>> Exception capturée :", exc1.value)

    print(">>> Tentative avec une chaîne d'espaces : Amenity('   ')")
    with pytest.raises(ValueError) as exc2:
        Amenity("   ")

    print(">>> Exception capturée :", exc2.value)


def test_create_amenity_with_non_string_name():
    """
    Vérifie qu'une TypeError est levée si le nom n'est pas une chaîne de caractères.
    """

    invalid_values = [42, None, [], {}]

    for value in invalid_values:
        print(f">>> Tentative de création avec name = {repr(value)} (type {type(value).__name__})")
        with pytest.raises(TypeError) as exc_info:
            Amenity(value)
        print(">>> Exception capturée :", exc_info.value)


def test_create_amenity_with_too_long_name():
    """
    Vérifie qu'une ValueError est levée si le nom dépasse 50 caractères.
    """

    long_name = "x" * 51  # 51 caractères

    print(f">>> Tentative avec un nom de {len(long_name)} caractères")
    with pytest.raises(ValueError) as exc_info:
        Amenity(long_name)

    print(">>> Exception capturée :", exc_info.value)


def test_repr_method_of_amenity():
    """
    Vérifie que __repr__() retourne une chaîne formatée avec id et name.
    """

    print(">>> Création d’un Amenity pour tester __repr__()")
    amenity = Amenity("Jacuzzi")
    repr_output = repr(amenity)

    print(">>> Résultat de repr(amenity) :", repr_output)

    # Vérifie la structure attendue
    assert isinstance(repr_output, str)
    assert repr_output.startswith("<Amenity ")
    assert amenity.id in repr_output
    assert "Jacuzzi" in repr_output


def test_str_method_of_amenity():
    """
    Vérifie que __str__() retourne une chaîne lisible au format attendu.
    """

    print(">>> Création d’un Amenity pour tester __str__()")
    amenity = Amenity("Piscine")
    str_output = str(amenity)

    print(">>> Résultat de str(amenity) :", str_output)

    # Vérifie que la chaîne retournée est correcte
    assert isinstance(str_output, str)
    assert str_output == "Commodité : Piscine"


