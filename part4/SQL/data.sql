DELETE FROM reviews;
DELETE FROM place_amenity;
DELETE FROM places;
DELETE FROM users;

-- Vérifier que l’utilisateur admin existe
--SELECT id, email, is_admin FROM users WHERE email = 'admin@hbnb.io';

-- Vérifier que les commodités ont bien été insérées
--SELECT * FROM amenities;

-- Insertion de l’administrateur
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
'9eac0ba7-d7f7-4072-91de-5153c3e15ed7',
'Admin',
'HBnB',
'admin@hbnb.io',
'$2b$12$F0cMKcD8gF0uF2c1vZofGe0jMlRVNK7GEf3EJzRgWX4FHFkVYr.MK',
TRUE
);

-- Créer un utilisateur standard
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
'31fbb9be-c2ef-4868-95c4-e5c3f2b78904',
'Luke',
'Skywalker',
'luke@force.io',
'$2b$12$abcdefghijklmnopqrstuv', -- hash fictif
FALSE
);

-- Créer un logement associé à cet utilisateur
INSERT INTO places (id, title, description, price, picture, latitude, longitude, owner_id)
VALUES (
'7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c',
'Tatooine Hideout',
'Secluded place in the Dune Sea.',
99.99,
'https://www.archi-wiki.org/images/thumb/1/16/Gommersdorf_%28pignon%29_DSC04951.jpg/300px-Gommersdorf_%28pignon%29_DSC04951.jpg',
34.2,
23.1,
'31fbb9be-c2ef-4868-95c4-e5c3f2b78904' -- FK vers Luke
);

-- Insertion des commodités initiales
INSERT INTO amenities (id, name) VALUES
('7b3e3737-ef53-4f13-8c38-6031e27d42ff', 'WiFi'),
('126eb780-f845-4ef8-8a68-e90b25534860', 'Swimming Pool'),
('b5c86946-44bb-4765-9db2-0ae21f190b47', 'Air Conditioning');


-- Lier le logement à deux commodités (WiFi et Piscine)
INSERT INTO place_amenity (place_id, amenity_id) VALUES
('7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c', '7b3e3737-ef53-4f13-8c38-6031e27d42ff'), -- WiFi
('7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c', '126eb780-f845-4ef8-8a68-e90b25534860'); -- Swimming Pool

-- Ajouter un avis sur le logement par Luke
INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES (
'aa7dd002-c672-4d5d-a28c-7168dfc390f2',
'The force is strong with this place.',
5,
'31fbb9be-c2ef-4868-95c4-e5c3f2b78904',
'7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c'
);

-- Modifier le titre du logement
--UPDATE places
--SET title = 'Jedi Hideout'
--WHERE id = '7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c';

-- Supprimer un avis
--DELETE FROM reviews
--WHERE id = 'aa7dd002-c672-4d5d-a28c-7168dfc390f2';

-- Refaire un SELECT sur les reviews pour confirmer la suppression
--SELECT * FROM reviews;
