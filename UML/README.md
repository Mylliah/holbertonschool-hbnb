# 🧾 Technical Documentation – HBnB Evolution Project

### Navigation

- [Introduction](#-introduction)
- [Architecture Diagram – Layered Architecture](#-architecture-diagram--layered-architecture)
- [Class Diagram – Business Logic Layer](#-class-diagram--business-logic-layer)
- [Sequence Diagrams – API Calls](#-sequence-diagrams--api-calls)

---

## 🔰 Introduction

This technical documentation was written as part of the HBnB Evolution project, a web application that allows users to post or book accommodations, leave reviews, and filter results based on their needs.

The goal of this document is to provide a **clear and structured overview** of the technical functioning of the application. It includes the **software architecture**, **main entities**, and **interactions between the different system layers**.  

Each diagram is accompanied by detailed explanations, so that everyone (developers, reviewers, POs, etc.) can understand the overall operation of the application.

---

## 📦 Architecture Diagram – Layered Architecture

### 🧱 Three Layers, Three Roles

This diagram represents the technical organization of our **HBnB** application into **three main layers**, each with a well-defined role. This is called a **layered architecture**, widely used to structure modern web applications.

<p align="center">
  <img src="./Package_Diagram.png" width="300" />
</p>

---

### 1. Presentation (`PresentationLayer`)

> 🎯 This is the **layer that interacts with the user**.

- It receives clicks, forms, requests (website or mobile app).
- It contains the **controllers** that link user actions to internal logic.

**Main Controllers:**
- `UserController`: handles signup, login, etc.
- `PlaceController`: creation, modification of listings.
- `ReviewController`: user reviews.
- `AmenityController`: amenities (WiFi, pool, etc.).

**Concretely:**  
When a user clicks a button, it's **one of these controllers** that receives the info and passes it to the system.

---

### 2. Business Logic (`BusinessLogicLayer`)

> 🫀 This is the **core of the app**. This is where business logic and operations are managed.

It contains:
- the **business models** (`User`, `Place`, `Review`, `Amenity`)  
- the **central facade** `HBnBFacade` that links controllers to models

**Concretely:**  
All business rules are managed here: validation, processing, calculations.

The controller **never speaks directly to a model**; it calls a method of the facade (register_user()), which then validates the data, creates the user, and so on. This keeps the code clean and prevents tight coupling.

---

### 3. Persistence (`PersistenceLayer`)

> 💾 This is the data layer.

- It stores and retrieves objects from the database.
- It contains the **repositories**:  
  `UserRepository`, `PlaceRepository`, `ReviewRepository`, `AmenityRepository`.
Each repository is specialized in data access for one model.
- **Persistence calls**: low-level operations that directly interact with the database, typically through raw SQL queries or ORM methods.

**Concretely:**  
When the business logic needs to save or retrieve an object, it goes through the corresponding repository, which handles communication with the database.

---

### 🔄 How Do Layers Communicate?

- The user clicks → the **controller** sends to the facade.
- The **facade** calls the right models.
- The **models** use the repositories to access the database.
- The **response** goes back up to the user.

> 📌 Why this structure?
- Better organization (each part has its role)
- Scalability (you can change the database without affecting logic)
- Easier maintenance

<p align="right"><a href="#navigation">↑ Back to Navigation</a></p>

---

## 🧩 Class Diagram – Business Logic Layer

This diagram shows the main **business entities** used in the app.  
Each entity corresponds to a real object handled by the user or the system.

<p align="center">
  <img src="./Class_Diagram_v2.png" width="10000" />
</p>

---

### 🧬 Parent Class: `BaseEntity`

To avoid repeating the same attributes everywhere, we created a common abstract class.

**Standard attributes** (present in all entities):
- `id`: UUID4 identifier
- `created_at`: creation date
- `updated_at`: last update date

All classes inherit from this base structure. This ensures a consistent logic and facilitates object tracing and serialization.

---

### 👤 User (`User`)

A user can:
- sign up, log in
- publish listings
- leave reviews

**Attributes:**
- `first_name`, `last_name`, `email`, `username`, `password`
- `is_admin`: boolean for admin rights

**Methods:**
- `register()`, `update_profile()`, `del_profile()`
- `is_admin()`: checks permissions

---

### 🏠 Place (`Place`)

A place contains location info, description, price, etc.

**Attributes:**
- `country`, `city`, `address`, `description`
- `housing_type`, `room_count`, `price`
- `latitude`, `longitude`

**Methods:**
- `create_place()`, `update_place()`, `delete_place()`, `list_places()`

---

### ✍️ Review (`Review`)

A user can leave a review on a place they visited.

**Attributes:**
- `user_id`, `place_id`
- `rating`, `commentary`

**Methods:**
- `create_review()`, `update_review()`, `delete_review()`, `list_reviews()`

---

### 🛠️ Amenity (`Amenity`)

An amenity can be shared across multiple places.

**Attributes:**
- `type`, `description`

**Methods:**
- `create_amenity()`, `update_amenity()`, `delete_amenity()`, `list_amenity()`

---

### 🎛️ Business Facade (`HBnBFacade`)

This is the **main interface used by controllers** to interact with business logic.

**Methods:**
- `register_user()`, `create_place()`, `add_review()`, `list_amenities()`, `get_user_profile()`

It **simplifies access** to business features by centralizing logic calls.

---

### 🔗 Entity Relationships

- **Inheritance:** all entities inherit from `BaseEntity`
- **Aggregations:**
  - `User` owns multiple `Place`
  - `User` writes multiple `Review`
  - `User` can create `Amenity`
- **Compositions:**
  - `Place` contains multiple `Review` (if deleted → reviews are too)
- **Multiple associations:**
  - `Place` uses multiple `Amenity` (and vice versa)

<p align="right"><a href="#navigation">↑ Back to Navigation</a></p>

---

## 🔁 Sequence Diagrams – API Calls

Sequence diagrams tell a **real user story**, showing everything that happens **from click to database**, step by step.

Each scenario is concrete and explained with a real-life example.

---

![User](./User_registration.png)

### 1. ✍️ User Registration
_a user signs up for a new account_

**The technical flow, step by step:**
> Léa wants to sign up on HBnB.

1. She fills in the form (`email`, `password`…)
2. The website sends a `POST /users/registration` request
3. The controller calls `register_user()` in `HBnBFacade`
4. The facade delegates to `UserModel` to perform checks:  
With → `validate_user_data()`:
   - that the email is properly formatted (e.g., no typos) → `check_email_format()`
   - that the password is strong enough → `hash_password()` which returns a hashed, unreadable, and thus secure version even if the database is compromised  
   - that the email is not already in use by someone else → `check_email_exists(email)`, by checking in the database via `UserRepository` (`SELECT * FROM users WHERE email = ?`)

5. If the email is available (`email_available`), a user instance is created using → `create_user_instance()`:  
   - a new unique ID is generated for Léa → `generate_uuid()`  
   - creation/update timestamps are added to the database → `set_timestamps()`

6. Léa is saved to the database by `UserRepository` using → `save_user(user_instance)` via `INSERT INTO users VALUES (…)`.

7. The server responds to the website that the registration was successful → `201 Created {user_id, message}`, and Léa can now log in.

**Example:**  
Léa tries to register with “lea@gmail.com”
- If this email already exists: she receives an error message “This email is already in use” → returned by `check_email_exists`.
- If everything is valid: she receives “Welcome to HBnB!” and her `user_id` is generated.

---

![Place](./Place_creation.png)

### 2. 🏡 Place Creation
_a user creates a new place listing_

**The technical flow, step by step:**
> Paul wants to publish his apartment in Fréjus.
  
1. Paul fills out the form (`country`, `city`, `address`, `housing_type`, `room_count`, `description`, `price`, `latitude`, `longitude`, `amenities`).  
2. The website sends the request to the API via `POST /places`, handled by `PlaceController`.  
3. The controller calls the method `create_place(place_data, user_id)` on `HBnBFacade`.  
4. The facade delegates to `PlaceModel` to perform validations:  
With → `validate_place_data()`:
   - that the coordinates are valid (no latitude like 999!) → `validate_coordinates()`  
   - that the price is positive → `validate_price()`  
   - that the selected amenities actually exist in the database → `validate_amenities(amenity_ids)`

5. If everything is valid (`amenities_valid`), the place instance is created with → `create_place_instance()`:  
   - a new unique ID is generated for the place → `generate_uuid()`  
   - creation/update timestamps are added to the database → `set_timestamps()`

6. The place is saved to the database by `PlaceRepository` using → `save_place(place_instance)`  
7. The amenity/place associations are recorded in the database via `INSERT INTO place_amenities VALUES (…)`.  
8. The server confirms to Paul that his place has been published → `201 Created {place_id, message}`.

**Example:**  
If Paul selects “WiFi” and “Pool” → the system checks if those amenities exist via **AmenityRepository**  
If Paul enters a negative price or forgets the address, he receives an error message triggered by `validate_price()`

---

![Review](./Review_Submission.png)

### 3. ⭐ Review Submission
_a user submits a review for a place_

**The technical flow, step by step:**
> Léa wants to leave a review on Paul’s place.
  
1. Léa writes her review and gives a rating (`rating`, `commentary`) on the place's page.  
2. The website sends the review to the server (API) via `POST /places/{place_id}/reviews`, handled by `ReviewController`.  
3. The controller calls the method `create_review(review_data, user_id, place_id)` on `HBnBFacade`.  
4. The facade checks:
   - that the place exists → `check_place_exists(place_id)` via `PlaceRepository` (`SELECT * FROM places WHERE id = ?`)  
   - that the user Léa exists in the database → `check_user_exists(user_id)` via `UserRepository`  
   - that Léa hasn’t already submitted a review for this place → `check_existing_review(user_id, place_id)` via `ReviewRepository` (`SELECT * FROM reviews WHERE user_id = ? AND place_id = ?`)  
   - that the rating is valid and between 1 and 5 → `validate_review_data()` via `ReviewModel`, then → `validate_rating(1-5)`

5. If everything is valid, the review instance is created with → `create_review_instance()`:  
   - a new unique ID is generated for the review → `generate_uuid()`  
   - creation/update timestamps are added to the database → `set_timestamps()`

6. The review is saved to the database by `ReviewRepository` using → `save_review(review_instance)` via `INSERT INTO reviews VALUES (…)`  
7. The server responds: “Thank you for your review!” → `201 Created {review_id, message}`.

**Example:**  
If Léa tries to rate the same place twice → check_existing_review finds an existing review and returns an error: “You have already submitted a review.”

---

![Fetching](./Fetching_a_List_of_Places.png)

### 4. 🔍 Fetching Places
_a user requests a list of places based on certain criteria_

**The technical flow, step by step:**
> Léa searches for a place in Fréjus with WiFi and a budget under €100.
  
1. Léa enters her search criteria into the search engine (e.g.: `city`, `max price`, `amenities`, etc.).  
2. The website sends the request to the server (API) via `GET /places?country=X&city=Y&housing_type=Z&min_price=A&max_price=B`, handled by `PlaceController`.  
3. The controller calls the method `get_places(filter_criteria)` on `HBnBFacade`.  
4. The facade asks `PlaceRepository` to search for all matching places:  
With → `find_places_by_criteria(filters)` which executes `SELECT * FROM places WHERE country = ? AND city = ? AND ...`:  
   - City = Fréjus  
   - Price ≤ €100  
   - Amenities include WiFi

5. For each place found:  
   - `AmenityRepository` retrieves the list of amenities with → `get_place_amenities(place_id)` via `SELECT amenities.* FROM amenities JOIN place_amenities ON ...`  
   - `ReviewRepository` calculates the average rating and number of reviews with → `get_place_reviews_summary(place_id)` via `SELECT AVG(rating), COUNT(*) FROM reviews WHERE place_id = ?` (`GET /places` returns, by default, the average rating and review count for an enriched listing)

6. `HBnBFacade` compiles the results with → `compile_places_with_details()`.  
7. The server returns the enriched list of places to the site, and Léa sees the results with prices, amenities, and ratings → `201 OK {places: [...]}`.

**Example :**
> “Cozy Studio, €90, WiFi, 4.7/5 stars (15 reviews)”  

Each displayed place includes its facilities (`amenities`), its rating (`average_rating`), and the number of reviews (`total_reviews`).

---

## Conclusion

This document brings together everything needed to **understand, build, and maintain** the HBnB project.  
Each section (architecture, entities, sequences) was designed to be **readable and directly usable** by the technical team.

> It’s now ready to serve as a **reference during development**, technical reviews, or even interviews.

<p align="right"><a href="#navigation">↑ Back to Navigation</a></p>