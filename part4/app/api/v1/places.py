"""
api/v1/places.py

Définit les endpoints pour la gestion des lieux (Place) dans l'application
HBnB.
Utilise Flask-RESTx pour définir l'API RESTful.

Chaque endpoint interagit avec la couche de logique métier via la facade
HBnBFacade.
"""

from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade  # Accès à la couche métier
from app.api.v1.reviews import review_model

# ===================================================
# Définition du Namespace pour les opérations Place
# ===================================================
api = Namespace('places', description='Place operations')

# ===================================================
# Définition du modèle Amenity (utilisé en réponse)
# ===================================================
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

# ===================================================
# Définition du modèle User (utilisé en réponse)
# ===================================================
user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# ===================================================
# Définition du modèle Place (reçu en entrée POST/PUT)
# ===================================================
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's"),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})


# ===================================================
# /api/v1/places/
# Ressource pour créer ou lister tous les lieux
# ===================================================
@api.route('/')
class PlaceList(Resource):

    @jwt_required()
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(404, 'Owner Not Found')
    @api.response(409, 'Conflict: Title already used by this owner')
    @api.response(500, 'Internal Server Error')
    def post(self):
        """
        Enregistre un nouveau lieu (place) à partir des données JSON reçues.
        """
        # Récupération et vérification du JSON reçu
        data = request.get_json()
        if not data:
            return {"error": "Missing or invalid JSON data"}, 400

        try:
            # Récupération de l'identité de l'utilisateur connecté
            current_user = get_jwt_identity()

            # Ajout de l'ID du propriétaire dans les données reçues
            data['owner_id'] = current_user 

            # Extraction de title et vérification de conflit avec cet owner
            title = data.get("title")
            existing_place = facade.get_place_by_title(title)
            if existing_place and str(existing_place.owner.id) == str(current_user):
                return {"error": "This owner already has a place with the same title"}, 409

            # Création du lieu via la facade
            new_place = facade.create_place(data)

            # Construction de la réponse JSON
            response = {
                'id': new_place.id,
                'title': new_place.title,
                'description': new_place.description,
                'price': new_place.price,
                'latitude': new_place.latitude,
                'longitude': new_place.longitude,
                'owner_id': new_place.owner.id
            }

            return response, 201

        # Gestion des erreurs de validation ou données incorrectes
        except (ValueError, TypeError, KeyError) as e:
            return {"error": str(e)}, 400

        # Gestion des erreurs inattendues (ex : crash interne, bug imprévu)
        except Exception as e:
            import traceback
            print("❌ ERREUR CRITIQUE - Exception levée lors du POST /places")
            print("Type :", type(e).__name__)
            print("Message :", str(e))
            traceback.print_exc()
            return {"error": "Internal server error"}, 500

    @api.response(200, 'List of places retrieved successfully')
    @api.response(500, 'Internal server error')
    def get(self):
        """
        Récupère la liste de tous les lieux enregistrés.
        """
        try:
            places = facade.get_all_places()
            if not places:
                return {
                    "message": "No places found",
                    "places": []
                }, 200

            result = []
            for place in places:
                result.append({
                    "id": place.id,
                    "title": place.title,
                    "description": place.description,
                    "price": place.price,
                    "picture": place.picture,
                    "latitude": place.latitude,
                    "longitude": place.longitude,
                    "owner": {
                        "id": place.owner.id,
                        "first_name": place.owner.first_name,
                        "last_name": place.owner.last_name,
                        "email": place.owner.email
                    },
                    "amenities": [
                        {
                            "id": amenity.id,
                            "name": amenity.name
                        }
                        for amenity in place.amenities
                    ],
                    "reviews": [
                        {
                            "id": review.id,
                            "text": review.text,
                            "rating": review.rating,
                            "user": {
                                "id": review.author.id,
                                "first_name": review.author.first_name,
                                "last_name": review.author.last_name,
                                "email": review.author.email
                            }
                        }
                        for review in place.reviews
                    ]
                })

            return {
                "message": "Places retrieved successfully",
                "places": result
            }, 200

        except Exception as e:
            print("❌ ERREUR dans GET /places/")
            print("Type :", type(e).__name__)
            print("Message :", str(e))
            return {"error": "Internal server error"}, 500


# ===================================================
# /api/v1/places/search
# Ressource pour rechercher un lieu par son titre exact
# ===================================================
@api.route('/search')
class PlaceSearch(Resource):
    @api.doc(params={'title': 'Exact title of the place to search'})
    @api.response(200, 'Place found')
    @api.response(400, 'Missing title parameter')
    @api.response(404, 'Place not found')
    def get(self):
        """
        Recherche un lieu par son titre exact (sensible à la casse).
        """
        title = request.args.get('title')
        if not title:
            return {"error": "Missing 'title' query parameter"}, 400

        place = facade.get_place_by_title(title)
        if not place:
            return {"error": "Place not found"}, 404

        return {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "price": place.price,
            "picture": place.picture,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner": {
                "id": place.owner.id,
                "first_name": place.owner.first_name,
                "last_name": place.owner.last_name,
                "email": place.owner.email
            },
            "amenities": [
                {
                    "id": amenity.id,
                    "name": amenity.name
                } for amenity in place.amenities
            ],
            "reviews": [
                {
                    "id": review.id,
                    "text": review.text,
                    "rating": review.rating,
                    "user": {
                        "id": review.author.id,
                        "first_name": review.author.first_name,
                        "last_name": review.author.last_name,
                        "email": review.author.email
                    }
                } for review in place.reviews
            ]
        }, 200


# ===================================================
# /api/v1/places/user/<user_id>
# Ressource pour récupérer tous les lieux d’un utilisateur donné
# ===================================================
@api.route('/user/<user_id>')
class PlacesByUser(Resource):
    @api.response(200, 'Places retrieved successfully for the user')
    @api.response(404, 'User not found or has no places')
    def get(self, user_id):
        """
        Récupère tous les lieux associés à un utilisateur (propriétaire) donné.
        """
        try:
            places = facade.get_places_by_user(user_id)
            if not places:
                return {"error": "No places found for this user"}, 404

            result = []
            for place in places:
                result.append({
                    "id": place.id,
                    "title": place.title,
                    "description": place.description,
                    "price": place.price,
                    "picture": place.picture,
                    "latitude": place.latitude,
                    "longitude": place.longitude,
                    "owner": {
                        "id": place.owner.id,
                        "first_name": place.owner.first_name,
                        "last_name": place.owner.last_name,
                        "email": place.owner.email
                    },
                    "amenities": [
                        {
                            "id": amenity.id,
                            "name": amenity.name
                        }
                        for amenity in place.amenities
                    ],
                    "reviews": [
                        {
                            "id": review.id,
                            "text": review.text,
                            "rating": review.rating,
                            "user": {
                                "id": review.author.id,
                                "first_name": review.author.first_name,
                                "last_name": review.author.last_name,
                                "email": review.author.email
                            }
                        }
                        for review in place.reviews
                    ]
                })

            return {
                "message": "Places retrieved successfully for this user",
                "places": result
            }, 200

        except Exception:
            return {"error": "Internal server error"}, 500


# ===================================================
# /api/v1/places/<place_id>
# Ressource pour accéder ou modifier un lieu spécifique
# ===================================================
@api.route('/<place_id>')
class PlaceResource(Resource):

    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    @api.response(500, 'Internal server error')
    def get(self, place_id):
        """
        Récupère les détails d’un lieu spécifique par son ID.
        """
        try:
            place = facade.get_place(place_id)
            if not place:
                return {'error': 'Place not found'}, 404

            return {
                "id": place.id,
                "title": place.title,
                "description": place.description,
                "price": place.price,
                "picture": place.picture,
                "latitude": place.latitude,
                "longitude": place.longitude,
                "owner": {
                    "id": place.owner.id,
                    "first_name": place.owner.first_name,
                    "last_name": place.owner.last_name,
                    "email": place.owner.email
                },
                "amenities": [
                    {
                        "id": amenity.id,
                        "name": amenity.name
                    } for amenity in place.amenities
                ],
                "reviews": [
                    {
                        "id": review.id,
                        "text": review.text,
                        "rating": review.rating,
                        "user": {
                            "id": review.author.id,
                            "first_name": review.author.first_name,
                            "last_name": review.author.last_name,
                            "email": review.author.email
                        }
                    } for review in place.reviews
                ]
            }, 200

        except Exception:
            return {"error": "Internal server error"}, 500

    @jwt_required()
    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'Place not found')
    @api.response(409, 'Conflict: Title already used by this owner')
    @api.response(500, 'Internal server error')
    def put(self, place_id):
        """
        Met à jour les informations d’un lieu par son ID.
        """
        # - Vérification de l'existence du lieu
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404

        current_user = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)

        if not is_admin and str(place.owner.id) != str(current_user["id"]):
            return {'error': 'Unauthorized action'}, 403

        # - Récupération et validation du JSON
        data = request.get_json()
        if not data:
            return {"error": "Missing or invalid JSON data"}, 400

        # - Préparation au traitement des amenities
        amenities_changed = False  # Flag de changement
        if "amenities" in data:
            amenities_ids = data.get("amenities")

            if not isinstance(amenities_ids, list):
                return {"error": "Field 'amenities' must be a list of IDs"}, 400

            amenities = []
            for amenity_id in amenities_ids:
                amenity = facade.get_amenity(amenity_id)
                if not amenity:
                    return {"error": f"Amenity with id '{amenity_id}' not found"}, 400
                amenities.append(amenity)

            # - Comparaison entre les anciennes et nouvelles amenities
            existing_ids = set(a.id for a in place.amenities)
            incoming_ids = set(amenities_ids)

            if existing_ids != incoming_ids:
                amenities_changed = True
                place.amenities = amenities  # Mise à jour en mémoire (hors repo)

        # - Comparaison combinée (champs simples + amenities)
        base_fields_unchanged = all(
            getattr(place, field) == data.get(field)
            for field in ['title', 'description', 'price', 'latitude', 'longitude']
            if data.get(field) is not None
        )

        if base_fields_unchanged and not amenities_changed:
            return {'error': 'No changes detected'}, 400

        # - Mise à jour finale via la facade
        try:
            facade.update_place(place_id, data)
            updated_place = facade.get_place(place_id)  # Rafraîchir les données

            return {
                'id': updated_place.id,
                'title': updated_place.title,
                'description': updated_place.description,
                'price': updated_place.price,
                "picture": place.picture,
                'latitude': updated_place.latitude,
                'longitude': updated_place.longitude,
                'owner_id': updated_place.owner.id,
                'amenities': [
                    {'id': amenity.id, 'name': amenity.name}
                    for amenity in updated_place.amenities
                ]
            }, 200

        except (ValueError, TypeError) as e:
            error_msg = str(e)
            if "Title already used" in error_msg:
                return {'error': error_msg}, 409
            return {'error': error_msg}, 400
