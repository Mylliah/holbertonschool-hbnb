
# 🏠 HBNB - RESTful API avec Authentification JWT

---

## 📌 Objectif du projet

Ce projet consiste à étendre le backend de l'application **HBnB** avec les fonctionnalités suivantes :
- Introduction de l'authentification sécurisée via **JWT** (connexion, droits utilisateurs)
- La gestion des droits utilisateurs (`admin`, `owner`, `guest`)
- Protection des **endpoints** pour les utilisateurs connectés ou administrateurs
- Implémentation des opérations **CRUD** complètes pour toutes les entités du projet : `User`, `Place`, `Review`, `Amenity`
- **Mapping ORM** des entités vers une base SQL via **SQLAlchemy**
- Validation des données d’entrée (types, contraintes, format JSON)
- Tests automatisés à l’aide de **pytest**

Il s’appuie sur Flask, Flask-RESTx et un système de persistance modulaire (in-memory ou SQLAlchemy).


---


## 🔧 Fonctionnalités principales

### 👤 Utilisateurs :
- Création, modification, suppression, connexion
- Mots de passe hachés avec Bcrypt
- Accès restreint à leur propre compte sauf pour les admins

### 🏠 Logements (Places) :
- Liés à un utilisateur propriétaire
- Informations géographiques (latitude, longitude)
- Association à des commodités
- Validation des champs

### 📍 Commodités (Amenities) :
- CRUD sauf DELETE
- Nommage unique, contrôle de longueur et validation

### 📝 Avis (Reviews) :
- Liés à un user_id et place_id
- Note (rating), texte, vérifications d'existence

### 🔒 Authentification JWT :
- Connexion via email/mot de passe, token JWT renvoyé
- À utiliser dans les headers des requêtes protégées

### 📈 Documentation Swagger automatique via Flask-RESTx

### 🔢 Validation JSON stricte à chaque endpoint

### ✅ Tests pytest avec couverture sur utilisateurs, places, amenities et reviews


---


## 🛋️ Objectifs pédagogiques

➤ Structurer un projet Flask REST avec une **architecture en couches**
➤ Implémenter le **pattern Façade** pour isoler la logique métier
➤ Utiliser Flask-RESTx pour gérer les routes, la documentation et les schémas d’entrée
➤ Gérer des **relations entre entités** (owner/place/review/amenities)
➤ Implémenter une **authentification JWT** complète et sécurisée
➤ Écrire des **tests automatisés** pour valider le comportement des endpoints


---


## 🏗️ Architecture du projet

```
├── 📁 SQL/
│ ├── 📄 data.sql → Données d'exemple
│ ├── 📄 schema.sql → Schéma de la base de données
│ └── 📄 test_crud.sql → Script de test des requêtes SQL

├── 📁 app/
│ ├── 📁 api/v1/
│ │ ├── 📄 amenities.py → Endpoints REST pour les commodités
│ │ ├── 📄 auth.py → Endpoint de login JWT
│ │ ├── 📄 places.py → Endpoints REST pour les logements
│ │ ├── 📄 reviews.py → Endpoints REST pour les avis
│ │ ├── 📄 users.py → Endpoints REST pour les utilisateurs
│ │ └── 📄 init.py → Regroupe les routes sous le namespace v1
│ │
│ ├── 📁 models/
│ │ ├── 📄 amenity.py → Modèle Amenity
│ │ ├── 📄 base.py → Classe de base commune SQLAlchemy
│ │ ├── 📄 place.py → Modèle Place
│ │ ├── 📄 review.py → Modèle Review
│ │ ├── 📄 user.py → Modèle User (avec hash de mot de passe)
│ │ └── 📄 init.py
│ │
│ ├── 📁 persistence/
│ │ ├── 📄 repository.py → Accès aux données (CRUD)
│ │ └── 📄 init.py
│ │
│ ├── 📁 services/
│ │ ├── 📄 extensions.py → Initialisation des extensions Flask (JWT, Bcrypt, DB)
│ │ └── 📄 init.py
│ │
│ └── 📄 init.py → Création de l'application Flask

├── 📁 tests/
│ └── 📄 test_user_model_pawd.py → Test du modèle utilisateur


├── 📄 config.py → Configuration Flask (dev/prod)
├── 📄 requirements.txt → Dépendances Python
├── 📄 run.py → Point d’entrée pour lancer l’API
```


---


## 🧩 Schéma relationnel (ERD)

Ce schéma représente les relations entre les entités principales du projet **HBnB** :
`User`, `Place`, `Review`, `Amenity`, et la table de liaison `Place_Amenity`.

Ce diagramme ER a été généré avec **Mermaid.js** pour mieux visualiser la structure de la base de données relationnelle utilisée avec SQLAlchemy.

Il permet de :

- Comprendre les **relations 1-N** et **N-N** entre les entités
- Vérifier la **cohérence du modèle SQLAlchemy**
- Servir de référence pour le développement ou le debug

Voici le résultat :

![Schéma ERD HBNB](images/relational_schema_ERD.png)


---


## 🛠️ Fonctionnalités

- CRUD complet pour :
  - `Users`
  - `Places`
  - `Reviews`
  - `Amenities`
- Authentification via **JWT** (`/api/v1/auth/login`)
- Mot de passe utilisateur **haché avec Flask-Bcrypt**
- Restrictions :
  - 🔒 Seuls les utilisateurs authentifiés peuvent modifier leurs propres données
  - 🛡️ Les admins peuvent modifier/supprimer n’importe quelle ressource
- Mapping SQLAlchemy des modèles
- Tests `pytest` (si implémentés)


---


## 🔐 Authentification & Sécurité

- JWT généré via `/api/v1/auth/login` avec email + mot de passe
- Décodage automatique dans les endpoints avec `@jwt_required()`
- Le champ `password` **n'est jamais retourné** dans les requêtes GET
- `is_admin=True` donne des privilèges étendus :
  - créer/modifier/supprimer n'importe quel utilisateur, review, amenity
- Vérification automatique de l'appartenance aux objets (`Place`, `Review`)


---


## 🚀 Installation & Lancement

### ⚙️ Prérequis
- Python 3.12+
- pip
- virtualenv (optionnel mais recommandé)

### 🧪 Installation

```bash
git clone https://github.com/Aluranae/holbertonschool-hbnb.git
cd part3/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ▶️ Lancement

```bash
python run.py
```

Le serveur démarre sur `http://127.0.0.1:5000/`


---


## 📡 Exemple d’utilisation (API)

### 🔑 Authentification (login)
```bash
curl -X POST http://127.0.0.1:5000/api/v1/auth/login   -H "Content-Type: application/json"   -d '{"email": "user@example.com", "password": "userpwd"}'
```

### 🔐 Accès protégé avec JWT

```bash
curl -X GET http://127.0.0.1:5000/api/v1/users/me   -H "Authorization: Bearer <your_token>"
```

### 🏠 Création d'une place (authentifié)
```bash
curl -X POST http://127.0.0.1:5000/api/v1/places   -H "Authorization: Bearer <your_token>"   -H "Content-Type: application/json"   -d '{"name": "My Flat", "description": "Nice place"}'
```

### 📝 Ajout d'un avis (review)
```bash
curl -X POST http://127.0.0.1:5000/api/v1/reviews   -H "Authorization: Bearer <your_token>"   -H "Content-Type: application/json"   -d '{"place_id": "<place_id>", "text": "Great stay!", "rating": 5}'
```

### ⛲ Création d'une commodité (admin seulement)
```bash
curl -X POST http://127.0.0.1:5000/api/v1/amenities   -H "Authorization: Bearer <admin_token>"   -H "Content-Type: application/json"   -d '{"name": "WiFi"}'
```

### ❌ Suppression d'une review (propriétaire ou admin)
```bash
curl -X DELETE http://127.0.0.1:5000/api/v1/reviews/<review_id>   -H "Authorization: Bearer <your_token>"
```


---


## ✅ Résultats des tests

### 🔬 Tests unitaires utilisateur (`pytest`)

Tous les tests sur le modèle `User` passent avec succès.  
Ils couvrent notamment :

- La validation des types (`str`, `email`, `UUID`)
- Les cas d'erreur (`missing fields`, `invalid email`, etc.)
- L’égalité entre objets utilisateur
- La mise à jour d’attributs
- La sécurité du mot de passe (champ privé, non exposé)

[Tests utilisateurs](https://github.com/Aluranae/holbertonschool-hbnb/blob/Dev_2/part3/tests/test_user_model_pawd.py)


---


### 🔐 Authentification JWT (Swagger)

La génération de token JWT fonctionne correctement via Swagger.  
Voici un exemple de connexion réussie avec un utilisateur **admin** (`admin@hbnb.io`) :

![Login JWT](https://github.com/Aluranae/holbertonschool-hbnb/blob/Dev_2/part3/images/Test_swagger_auth_admin.png)

Les tokens JWT sont ensuite utilisés pour accéder aux routes protégées comme :

- POST `/places`  
- POST `/amenities`  
- PUT `/reviews/<id>`  
- DELETE `/users/<id>` (admin uniquement)


---


## 📚 Technologies utilisées

- **Python 3.12**
- **Flask**
- **Flask-RESTx**
- **Flask-JWT-Extended**
- **Flask-Bcrypt**
- **SQLAlchemy** (mapping)
- **pytest** (tests éventuels)


---


## 👥 Auteurs

- [Benjamin Estrada](https://github.com/Aluranae)
- [Nina](https://github.com/ninaglss15)
- [Mylliah](https://github.com/Mylliah)


---
