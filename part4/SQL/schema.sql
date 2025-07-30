-- Create database tables for HBnB

-- Create User table
CREATE TABLE IF NOT EXISTS users (
id CHAR(36) PRIMARY KEY,
first_name VARCHAR(255),
last_name VARCHAR(255),
email VARCHAR(255) UNIQUE NOT NULL,
password VARCHAR(255) NOT NULL,
is_admin BOOLEAN DEFAULT FALSE,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Place table
CREATE TABLE IF NOT EXISTS places (
id CHAR(36) PRIMARY KEY,
title VARCHAR(255),
description TEXT,
price DECIMAL(10, 2),
picture VARCHAR(1024),
latitude FLOAT,
longitude FLOAT,
owner_id CHAR(36),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (owner_id) REFERENCES users(id)
);

-- Create Review table
CREATE TABLE IF NOT EXISTS reviews (
id CHAR(36) PRIMARY KEY,
text TEXT,
rating INT CHECK (rating BETWEEN 1 AND 5),
user_id CHAR(36),
place_id CHAR(36),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (place_id) REFERENCES places(id),
CONSTRAINT unique_user_place_review UNIQUE (user_id, place_id)
);

-- Create Amenity table
CREATE TABLE IF NOT EXISTS amenities (
id CHAR(36) PRIMARY KEY,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
name VARCHAR(255) UNIQUE NOT NULL
);

-- Create Place_Amenity table
CREATE TABLE IF NOT EXISTS place_amenity (
place_id CHAR(36),
amenity_id CHAR(36),
PRIMARY KEY (place_id, amenity_id),
FOREIGN KEY (place_id) REFERENCES places(id),
FOREIGN KEY (amenity_id) REFERENCES amenities(id)
);
