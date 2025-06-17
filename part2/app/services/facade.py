from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Méthode placeholder pour créer un user
    def create_user(self, user_data):
        # La logique sera implémentée dans les tâches ultérieures
        pass

    # Méthode placeholder pour récupérer un place par ID
    def get_place(self, place_id):
        # La logique sera implémentée dans les tâches ultérieures
        pass
