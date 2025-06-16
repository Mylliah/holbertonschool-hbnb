"""tests/test_user.py

Teste la création de l'entité User (valeurs valides uniquement).
"""

import pytest
from models.user import User


def test_create_valid_user():
    """
    Vérifie qu'un User valide peut être créé sans erreur,
    et que ses attributs sont correctement initialisés.
    """
    user = User(name="Leia Organa", email="leia@rebellion.org")

    assert isinstance(user, User)
    assert user.name == "Leia Organa"
    assert user.email == "leia@rebellion.org"
    assert user.id is not None
    assert user.created_at is not None
    assert user.updated_at is not None
