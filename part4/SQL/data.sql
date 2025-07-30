DELETE FROM reviews;
DELETE FROM place_amenity;
DELETE FROM places;
DELETE FROM users;
DELETE FROM amenities;  -- Ajouter cette ligne pour vider aussi les amenities

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
'$2b$12$PmYGBeQAJ9Pwt4w2omdnsurzSMazUEKgp01ZyWxoBBoEpEGwnCuhC',
TRUE
);

-- Créer un utilisateur standard
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
'31fbb9be-c2ef-4868-95c4-e5c3f2b78904',
'Haruki',
'Murakami',
'soleil@levant.io',
'$2b$12$abcdefghijklmnopqrstuv', -- hash fictif
FALSE
);


-- Créer un deuxième utilisateur pour tester les avis
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
'42abc567-d7f7-4072-91de-5153c3e15ed8',
'Yukio',
'Mishima',
'papillon@painauxraisins.io',
'$2b$12$abcdefghijklmnopqrsawz', -- hash fictif
FALSE
);


-- Créer un deuxième utilisateur pour tester les avis
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
'51cvb728-e4r6-4635-12gr-7368c3e15ty0',
'Natsume',
'Sôseki',
'botchan@petitmaitre.io',
'$2b$12$abcdefghijklmnopqrsbrf', -- hash fictif
FALSE
);


-- Créer un troisième utilisateur pour tester les avis
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
'89vad163-j9c4-8507-09df-6780c5s77aw3',
'Yôko',
'Ogawa',
'etrange@journal.io',
'$2b$12$abcdefghijklmnopqrsiyu', -- hash fictif
FALSE
);


-- Créer un logement associé à l'utilisateur Haruki Murakami
INSERT INTO places (id, title, description, price, picture, latitude, longitude, owner_id)
VALUES (
'7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c', -- place id
'Le passage de la nuit',
'Admiration des tambourins de soie. - à Gero Onsen',
99.99,
'https://images.unsplash.com/photo-1670854753472-4d7cbe07a1c0?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
34.2,
23.1,
'31fbb9be-c2ef-4868-95c4-e5c3f2b78904' -- owner id
);


-- Créer un logement associé à l'utilisateur Yukio Mishima
INSERT INTO places (id, title, description, price, picture, latitude, longitude, owner_id)
VALUES (
'2r3uyt75-ki79-7z3n-3825-132f2a3iyu8j', -- place id
'La mer et le couchant',
'Collision entre deux merveilles. - à Kanazawa',
45.99,
'https://images.unsplash.com/photo-1695539330133-f0c931c95f27?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
34.2,
23.1,
'42abc567-d7f7-4072-91de-5153c3e15ed8' -- owner id
);


-- Créer un logement associé à l'utilisateur Natsume Souseki
INSERT INTO places (id, title, description, price, picture, latitude, longitude, owner_id)
VALUES (
'5dvgf3v-k789-0m6b-4093-678r1d6e2wz7p', -- place id
'Les Sept Ponts',
'Un croisement vers septs lieux exceptionnels. - à Saitama',
9.99,
'https://images.unsplash.com/photo-1474168999089-5956598f4ea4?q=80&w=1929&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
34.2,
23.1,
'51cvb728-e4r6-4635-12gr-7368c3e15ty0' -- owner id
);


-- Créer un logement associé à l'utilisateur Natsume Souseki
INSERT INTO places (id, title, description, price, picture, latitude, longitude, owner_id)
VALUES (
'6jndl9y-k789-0m6b-4093-827r1d6e2pa8b', -- place id
'Grandeur Nature',
'Doux, brute et bienveillant. - à Kyôtô',
100.99,
'https://images.unsplash.com/photo-1686933021211-19a669f3acb2?q=80&w=2127&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
34.2,
23.1,
'51cvb728-e4r6-4635-12gr-7368c3e15ty0' -- owner id
);


-- Créer un logement associé à l'utilisateur Yôko Ogawa
INSERT INTO places (id, title, description, price, picture, latitude, longitude, owner_id)
VALUES (
'8sgoi8n-k789-0m6b-4093-836m9qw9eyc93', -- place id
'La loi du silence',
'Apaisement et tranquillité. - à Nara',
126.88,
'https://images.unsplash.com/photo-1722229808606-d060bf607028?q=80&w=2030&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
34.2,
23.1,
'89vad163-j9c4-8507-09df-6780c5s77aw3' -- owner id
);


-- Insertion des commodités initiales (avec OR IGNORE pour éviter les doublons)
INSERT OR IGNORE INTO amenities (id, name) VALUES
('7b3e3737-ef53-4f13-8c38-6031e27d42ff', 'WiFi'),
('126eb780-f845-4ef8-8a68-e90b25534860', 'Swimming Pool'),
('b5c86946-44bb-4765-9db2-0ae21f190b47', 'Air Conditioning'),
('xba87439-89xn-2395-0bhx-udqs87hjkjx8', 'View'),
('9lkjzlqj-e7au-3278-hsjs-873289jhghza', 'Futon'),
('57sjhl8o-d762-hjz1-8lmz-278jk08llkjs', 'Private Bath'),
('lk79mals-t45h-kjsh-4520-kj087lkjvc7n', 'Kaiseki Breakfast')
;


-- Lier le logement à deux commodités (WiFi et Piscine)
INSERT INTO place_amenity (place_id, amenity_id) VALUES -- Place de Haruki Murakami
('7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c', '7b3e3737-ef53-4f13-8c38-6031e27d42ff'), -- WiFi
('7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c', 'b5c86946-44bb-4765-9db2-0ae21f190b47'), -- Air Conditioning
('7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c', 'xba87439-89xn-2395-0bhx-udqs87hjkjx8'), -- View
('7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c', 'lk79mals-t45h-kjsh-4520-kj087lkjvc7n'), -- Kaiseki Breakfast
('7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c', '57sjhl8o-d762-hjz1-8lmz-278jk08llkjs'), -- Private Bath
('7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c', '9lkjzlqj-e7au-3278-hsjs-873289jhghza'); -- Futon


INSERT INTO place_amenity (place_id, amenity_id) VALUES -- Place de Yukio Mishima
('2r3uyt75-ki79-7z3n-3825-132f2a3iyu8j', '7b3e3737-ef53-4f13-8c38-6031e27d42ff'), -- WiFi
('2r3uyt75-ki79-7z3n-3825-132f2a3iyu8j', 'b5c86946-44bb-4765-9db2-0ae21f190b47'), -- Air Conditioning
('2r3uyt75-ki79-7z3n-3825-132f2a3iyu8j', '126eb780-f845-4ef8-8a68-e90b25534860'); -- Swimming Pool


INSERT INTO place_amenity (place_id, amenity_id) VALUES -- Place 1 de Natsume Sôseki
('5dvgf3v-k789-0m6b-4093-678r1d6e2wz7p', '7b3e3737-ef53-4f13-8c38-6031e27d42ff'), -- WiFi
('5dvgf3v-k789-0m6b-4093-678r1d6e2wz7p', '9lkjzlqj-e7au-3278-hsjs-873289jhghza'), -- Futon
('5dvgf3v-k789-0m6b-4093-678r1d6e2wz7p', 'xba87439-89xn-2395-0bhx-udqs87hjkjx8'); -- View


INSERT INTO place_amenity (place_id, amenity_id) VALUES -- Place 2 de Natsume Sôseki
('6jndl9y-k789-0m6b-4093-827r1d6e2pa8b', '7b3e3737-ef53-4f13-8c38-6031e27d42ff'), -- WiFi
('6jndl9y-k789-0m6b-4093-827r1d6e2pa8b', '9lkjzlqj-e7au-3278-hsjs-873289jhghza'), -- Futon
('6jndl9y-k789-0m6b-4093-827r1d6e2pa8b', 'xba87439-89xn-2395-0bhx-udqs87hjkjx8'), -- View
('6jndl9y-k789-0m6b-4093-827r1d6e2pa8b', 'lk79mals-t45h-kjsh-4520-kj087lkjvc7n'); -- Kaiseki Breakfast


INSERT INTO place_amenity (place_id, amenity_id) VALUES -- Place de Yôko Ogawa
('8sgoi8n-k789-0m6b-4093-836m9qw9eyc93', '9lkjzlqj-e7au-3278-hsjs-873289jhghza'), -- Futon
('8sgoi8n-k789-0m6b-4093-836m9qw9eyc93', 'xba87439-89xn-2395-0bhx-udqs87hjkjx8'), -- View
('8sgoi8n-k789-0m6b-4093-836m9qw9eyc93', 'lk79mals-t45h-kjsh-4520-kj087lkjvc7n'), -- Kaiseki Breakfast
('8sgoi8n-k789-0m6b-4093-836m9qw9eyc93', '57sjhl8o-d762-hjz1-8lmz-278jk08llkjs'); -- Private Bath


-- Ajouter un avis sur le logement de Haruki Murakami par Yukio Mishima
INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES (
'aa7dd002-c672-4d5d-a28c-7168dfc390f2', -- review id
'La pie niche haut, l oie niche bas',
2,
'42abc567-d7f7-4072-91de-5153c3e15ed8', -- Yukio Mishima donne son avis
'7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c'  -- Sur le logement de Haruki Murakami
);


-- Ajouter un avis sur le logement de Haruki Murakami par Nastume Sôseki
INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES (
'ff9sf673-c672-4d5d-a28c-6458dkc926s9', -- review id
'Mais où niche l hiboux ?',
3,
'51cvb728-e4r6-4635-12gr-7368c3e15ty0', -- Natsume Sôseki donne son avis
'7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c'  -- Sur le logement de Haruki Murakami
);


-- Ajouter un avis sur le logement de Haruki Murakami par Yôko Ogawa
INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES (
'ix7zk089-c672-4d5d-a28c-0638xla069a7', -- review id
'L hiboux niche ni haut, ni bas',
4,
'89vad163-j9c4-8507-09df-6780c5s77aw3', -- Yôko Ogawa donne son avis
'7a9cfb4d-e422-4e9a-8917-998f8e8e1d7c'  -- Sur le logement de Haruki Murakami
);


-- Ajouter un avis sur le logement de Yukio Mishima par Yôko Ogawa
INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES (
'bb8ee103-d783-5e6e-b39d-8279efc501g3', -- review id DIFFÉRENT
'Rien à envier à... (voir plus)',
5,
'89vad163-j9c4-8507-09df-6780c5s77aw3', -- Yôko Ogawa donne son avis
'2r3uyt75-ki79-7z3n-3825-132f2a3iyu8j'  -- Sur le logement de Yukio Mishima
);


-- Ajouter un avis sur le logement de Yukio Mishima par Haruki Murakami
INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES (
'ml8ee103-d783-5e6e-b39d-8279efc048k44', -- review id DIFFÉRENT
'Dommage, ils n étaient pas au rendez-vous',
3,
'31fbb9be-c2ef-4868-95c4-e5c3f2b78904', -- Haruki Murakami donne son avis
'2r3uyt75-ki79-7z3n-3825-132f2a3iyu8j'  -- Sur le logement de Yukio Mishima
);


-- Ajouter un avis sur le logement de Natsume Sôseki par Yukio Mishima
INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES (
'za8ee103-d783-5e6e-b39d-8279efc465p12', -- review id DIFFÉRENT
'Pas très stable malheureusement',
2,
'42abc567-d7f7-4072-91de-5153c3e15ed8', -- Yukio Mishima donne son avis
'5dvgf3v-k789-0m6b-4093-678r1d6e2wz7p'  -- Sur le logement de Natsume Sôseki
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
