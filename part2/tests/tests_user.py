"""tests/test_user.py

Teste la création de l'entité User (valeurs valides uniquement).
"""

import pytest
import time
from app.models.user import User


def test_create_valid_user():
    """
    Vérifie qu'un User valide peut être créé sans erreur,
    et que ses attributs sont correctement initialisés.
    """
    user = User(first_name="Leia", last_name="Organa", email="leia@rebellion.org")

    print(f"[DEBUG] Created user → {user}")
    print(f"[INFO] Email = {user.email}")
    print(f"[INFO] ID = {user.id}")
    print(f"[INFO] created_at = {user.created_at}")

    assert isinstance(user, User)
    assert user.first_name == "Leia"
    assert user.last_name == "Organa"
    assert user.email == "leia@rebellion.org"
    assert user.id is not None
    assert user.created_at is not None
    assert user.updated_at is not None


def test_update_user_attribute():
    """
    Vérifie que la modification d'un attribut met à jour updated_at.
    """
    user = User(first_name="Han", last_name="Solo", email="han@falcon.com")
    original_updated_at = user.updated_at

    # Pause pour observer une vraie différence temporelle
    time.sleep(1)

    # Modification d'un attribut
    user.first_name = "Han-Leader"
    user.save()  # méthode héritée de Base, met à jour updated_at

    print(f"[DEBUG] Updated user → {user}")
    print(f"[INFO] updated_at (after update) = {user.updated_at}")

    assert user.first_name == "Han-Leader"
    assert user.updated_at > original_updated_at


def test_user_creation_missing_fields():
    """
    Vérifie qu'une exception est levée si des champs requis sont manquants.
    """
    with pytest.raises(ValueError) as exc_info:
        User(first_name="Luke")  # manque last_name et email

    print(f"[INFO] Exception levée → {exc_info.value}")
    assert "last_name" in str(exc_info.value) or "email" in str(exc_info.value)


def test_user_creation_empty_fields():
    """
    Vérifie qu'une exception est levée si les champs requis sont vides ou None.
    """
    # Cas 1 : email vide
    with pytest.raises(ValueError) as exc_email:
        User(first_name="Padmé", last_name="Naberrie", email="")

    print(f"[INFO] Email vide → {exc_email.value}")
    assert "email" in str(exc_email.value).lower()

    # Cas 2 : prénom vide
    with pytest.raises(ValueError) as exc_first:
        User(first_name="", last_name="Skywalker", email="anakin@jedi.org")

    print(f"[INFO] Prénom vide → {exc_first.value}")
    assert "first_name" in str(exc_first.value).lower()

    # Cas 3 : nom vide
    with pytest.raises(ValueError) as exc_last:
        User(first_name="Anakin", last_name="", email="anakin@jedi.org")

    print(f"[INFO] Nom vide → {exc_last.value}")
    assert "last_name" in str(exc_last.value).lower()


def test_user_creation_invalid_types():
    """
    Vérifie que des types incorrects provoquent une exception.
    """
    # Cas 1 : prénom en int
    with pytest.raises(TypeError) as exc_type1:
        User(first_name=42, last_name="Kenobi", email="obiwan@jedi.org")

    print(f"[INFO] Type prénom invalide → {exc_type1.value}")
    assert "first_name" in str(exc_type1.value).lower()

    # Cas 2 : email en list
    with pytest.raises(TypeError) as exc_type2:
        User(first_name="Obi-Wan", last_name="Kenobi", email=["kenobi@jedi.org"])

    print(f"[INFO] Type email invalide → {exc_type2.value}")
    assert "email" in str(exc_type2.value).lower()


def test_user_creation_invalid_email_format():
    """
    Vérifie que des emails au format invalide sont rejetés.
    """
    # Pas d’arobase
    with pytest.raises(ValueError) as exc1:
        User(first_name="Qui-Gon", last_name="Jinn", email="quigon.jedi.org")

    print(f"[INFO] Email sans @ → {exc1.value}")
    assert "email" in str(exc1.value).lower()

    # Double @
    with pytest.raises(ValueError) as exc2:
        User(first_name="Count", last_name="Dooku", email="dooku@@sith.org")

    print(f"[INFO] Email avec @@ → {exc2.value}")
    assert "email" in str(exc2.value).lower()

    # Pas de domaine
    with pytest.raises(ValueError) as exc3:
        User(first_name="General", last_name="Grievous", email="grievous@")

    print(f"[INFO] Email sans domaine → {exc3.value}")
    assert "email" in str(exc3.value).lower()


def test_user_creation_invalid_email_double_at():
    """
    Vérifie que l'email avec double arobase est rejeté.
    """
    with pytest.raises(ValueError) as exc:
        User(first_name="Count", last_name="Dooku", email="dooku@@sith.org")

    print(f"[INFO] Email avec @@ → {exc.value}")
    assert "email" in str(exc.value).lower()
