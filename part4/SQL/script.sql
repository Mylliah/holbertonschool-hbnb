DELETE FROM places;

-- Créer un logement associé à cet utilisateur
INSERT INTO places (id, title, description, price, picture, latitude, longitude, owner_id)
VALUES (
'7a1cfb4d-e422-4e9a-8917-998f8e8e1d7c',
'Tatooine Hideout',
'Secluded place in the Dune Sea.',
99.99,
'https://www.archi-wiki.org/images/thumb/1/16/Gommersdorf_%28pignon%29_DSC04951.jpg/300px-Gommersdorf_%28pignon%29_DSC04951.jpg',
34.2,
23.1,
'31fbb9be-c2ef-4868-95c4-e5c3f2b78904' -- FK vers Luke
);

-- Créer un logement associé à cet utilisateur
INSERT INTO places (id, title, description, price, picture, latitude, longitude, owner_id)
VALUES (
'7abcfb4d-e422-4e9a-8917-998f8e8e1d7c',
'Tatooine Hideout',
'Secluded place in the Dune Sea.',
99.99,
'https://www.archi-wiki.org/images/thumb/1/16/Gommersdorf_%28pignon%29_DSC04951.jpg/300px-Gommersdorf_%28pignon%29_DSC04951.jpg',
34.2,
23.1,
'31fbb9be-c2ef-4868-95c4-e5c3f2b78904' -- FK vers Luke
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
