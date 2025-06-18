from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # ==========================
    # Gestion de User
    # ==========================

    # Méthode placeholder pour créer un user
    def create_user(self, user_data):
        """
        Crée un nouvel utilisateur à partir d'un dictionnaire de données.
        Exige : first_name, last_name, email (is_admin est optionnel).
        Lève une ValueError si les données sont invalides.
        """
        try:
            user = User(
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                email=user_data["email"],
                is_admin=user_data.get("is_admin", False)
            )
            self.user_repo.add(user)
            return user
        except (KeyError, TypeError, ValueError) as e:
            raise ValueError(f"Invalid user data: {e}")

    def get_user(self, user_id):
        """
        Récupère un utilisateur par son identifiant.
        Retourne l'objet User ou None si non trouvé.
        """
        return self.user_repo.get(user_id)

    def get_all_users(self):
        """
        Retourne la liste de tous les utilisateurs.
        """
        return self.user_repo.get_all()

    def update_user(self, user_id, update_data):
        """
        Met à jour un utilisateur existant avec les données fournies.
        Lève une ValueError si l'utilisateur n'existe pas.
        """
        user = self.get_user(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")

        user.update(update_data)  # méthode fournie par BaseModel
        self.user_repo.add(user)  # réécriture dans le stockage
        return user

    def delete_user(self, user_id):
        """
        Supprime un utilisateur par son identifiant.
        Retourne True si suppression réussie, False sinon.
        """
        if self.get_user(user_id):
            self.user_repo.delete(user_id)
            return True
        return False

    # ==========================
    # Gestion de Place
    # ==========================

    # Méthode placeholder pour récupérer un place par ID
    def get_place(self, place_id):
        # La logique sera implémentée dans les tâches ultérieures
        pass

    # ==========================
    # Gestion de Amenity
    # ==========================

    # Méthode placeholder pour récupérer un amenity par ID
    def get_amenity(self, place_id):
        # La logique sera implémentée dans les tâches ultérieures
        pass

    # ==========================
    # Gestion de Review
    # ==========================

    # Méthode placeholder pour récupérer un review par ID
    def get_review(self, place_id):
        # La logique sera implémentée dans les tâches ultérieures
        pass
