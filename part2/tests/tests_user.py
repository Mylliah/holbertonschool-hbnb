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
    time.sleep(3)

    # Modification d'un attribut
    user.first_name = "Han-Leader"
    user.save()  # méthode héritée de Base, met à jour updated_at

    print(f"[DEBUG] Updated user → {user}")
    print(f"[INFO] updated_at (after update) = {user.updated_at}")

    assert user.first_name == "Han-Leader"
    assert user.updated_at > original_updated_at


def test_user_update_method_on_valid_attribute():
    """
    Vérifie que la méthode update() modifie un attribut existant.
    """
    user = User(first_name="Padmé", last_name="Naberrie", email="padme@senate.org")
    old_updated_at = user.updated_at

    time.sleep(1)
    user.update({"last_name": "Amidala"})

    assert user.last_name == "Amidala"
    assert user.updated_at > old_updated_at


def test_user_update_method_ignores_unknown_attribute():
    """
    Vérifie que la méthode update() ignore les clés inconnues du dictionnaire.
    """
    user = User(first_name="Anakin", last_name="Skywalker", email="anakin@jedi.org")
    user.update({"rank": "Knight"})

    assert not hasattr(user, "rank")


def test_user_update_multiple_fields():
    """
    Vérifie la mise à jour simultanée de plusieurs champs.
    """
    user = User(first_name="Ben", last_name="Kenobi", email="ben@jedi.org")

    user.update({
        "first_name": "Obi-Wan",
        "email": "obiwan@jedi.org"
    })

    assert user.first_name == "Obi-Wan"
    assert user.email == "obiwan@jedi.org"


def test_user_creation_missing_fields():
    """
    Vérifie qu'une exception est levée si des champs requis sont manquants.
    """
    with pytest.raises(TypeError) as exc_info:
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
    assert "required" in str(exc_first.value).lower()

    # Cas 3 : nom vide
    with pytest.raises(ValueError) as exc_last:
        User(first_name="Anakin", last_name="", email="anakin@jedi.org")

    print(f"[INFO] Nom vide → {exc_last.value}")
    assert "required" in str(exc_last.value).lower()


def test_user_creation_invalid_types():
    """
    Vérifie que des types incorrects provoquent une exception.
    """
    # Cas 1 : prénom en int
    with pytest.raises(TypeError) as exc_type1:
        User(first_name=42, last_name="Kenobi", email="obiwan@jedi.org")

    print(f"[INFO] Type prénom invalide → {exc_type1.value}")
    assert "first name must be a string" in str(exc_type1.value).lower()

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


def test_user_update_with_unknown_attribute():
    """
    Vérifie qu'une tentative d'ajout d'un champ inconnu sur un User échoue.
    """
    user = User(first_name="Bail", last_name="Organa", email="bail@alderaan.org")

    try:
        user.rank = "senator"  # champ non défini dans la classe User
        print(f"[DEBUG] Unexpected attribute rank → {user.rank}")
        assert not hasattr(user, "rank"), "User should not accept unknown attributes"
    except AttributeError:
        print("[INFO] AttributeError correctly raised")
        assert True


def test_user_id_and_created_at_immutability():
    """
    Vérifie que id et created_at ne doivent pas être modifiés après instanciation.
    Ce test montre qu'une mutation est possible par défaut (comportement de Python),
    mais qu'elle devrait être évitée dans un usage normal.
    """
    user = User(first_name="Cassian", last_name="Andor", email="cassian@rebellion.org")

    original_id = user.id
    original_created = user.created_at

    # Tentative de modification
    user.id = "FAKE-ID"
    user.created_at = "3019-01-01 00:00:00"

    print(f"[DEBUG] ID modifié : {user.id}")
    print(f"[DEBUG] created_at modifié : {user.created_at}")

    assert user.id != original_id, "ID should not be mutable (test volontairement FAIL)"
    assert user.created_at != original_created, "created_at should not be mutable"
