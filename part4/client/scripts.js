// fonction utilitaire pour lire un cookie
function getCookie(name) {
  const cookieString = document.cookie;
  const cookies = cookieString.split('; ');
  for (let cookie of cookies) {
    const [key, value] = cookie.split('=');
    if (key === name) {
      return value;
    }
  }
  return null;
}

document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    // Listener sur le submit
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault(); // empêcher rechargement par défaut

      // Récupération des champs email/password
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      try {
        // Requête AJAX vers l'API
        const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json' // obligatoire pour JSON
          },
          body: JSON.stringify({ email, password }) // envoi du corps JSON
        });

        // Traitement de la réponse
        if (response.ok) {
          const data = await response.json();

          // Stockage du JWT dans un cookie
          document.cookie = `token=${data.access_token}; path=/; max-age=3600`;

          // Redirection vers index.html
          window.location.href = 'index.html';
        } else {
          // Gestion d'erreur
          alert('Login failed: ' + response.statusText);
        }
      } catch (error) {
        alert('Login failed: ' + error.message); // gestion d'erreur réseau
      }
    });
  }

  const currentPage = window.location.pathname;

  if (currentPage.includes('index.html')) {
    const token = getCookie('token');
    const loginLink = document.querySelector('.login-button');

    if (!token) {
      loginLink.style.display = 'block'; // Non connecté
    } else {
      loginLink.style.display = 'none'; // Connecté
      fetchPlaces(token); // récupérer les lieux
    }

    setupPriceFilter(); // initialiser le filtre de prix
  }

  if (currentPage.includes('place.html')) {
    const placeId = getPlaceIdFromURL();
    const token = getCookie('token');
    const addReviewSection = document.getElementById('add-review');

    if (!token) {
      addReviewSection.style.display = 'none'; // cacher le formulaire
    } else {
      addReviewSection.style.display = 'block'; // afficher le formulaire
    }

    fetchPlaceDetails(placeId, token);
  }

  // Formulaire d'ajout de review
  if (currentPage.includes('add_review.html')) {
    const token = getCookie('token');
    if (!token) {
      window.location.href = 'index.html'; // redirection si non connecté
      return;
    }

    const placeId = getPlaceIdFromURL();
    const reviewForm = document.getElementById('review-form');

    if (reviewForm) {
      reviewForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        
        const reviewText = document.getElementById('review').value;
        const rating = document.getElementById('rating').value;

        if (!reviewText || !rating) {
          alert('Please fill in all fields');
          return;
        }

        try {
          const response = await fetch('http://127.0.0.1:5000/api/v1/reviews', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({
              place_id: placeId,
              text: reviewText,
              rating: parseInt(rating)
            })
          });

          if (response.ok) {
            alert('Review submitted successfully!');
            reviewForm.reset();
          } else {
            const data = await response.json();
            alert('Failed to submit review: ' + (data.message || data.error || response.statusText));
          }
        } catch (error) {
          alert('Error: ' + error.message);
        }
      });
    }
  }
});

// fetch des lieux depuis l'API
async function fetchPlaces(token) {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });

    if (!response.ok) {
      throw new Error('Failed to fetch places');
    }

    const places = await response.json();
    displayPlaces(places); // afficher les lieux
  } catch (error) {
    alert('Error: ' + error.message);
  }
}

function displayPlaces(places) {
  const placesList = document.getElementById('places-list');
  placesList.innerHTML = ''; // reset

  places.forEach(place => {
    const card = document.createElement('div');
    card.className = 'place-card';
    card.setAttribute('data-price', place.price); // pour filtrer

    card.innerHTML = `
      <h3>${place.title}</h3>
      <p>$${place.price} per night</p>
      <a href="place.html?id=${place.id}" class="details-button">View Details</a>
    `;

    placesList.appendChild(card);
  });
}

// fonction pour initialiser et gérer le filtre de prix
function setupPriceFilter() {
  const filter = document.getElementById('price-filter');
  const options = ['10', '50', '100', 'All'];

  if (filter.options.length === 0) {
    options.forEach(value => {
      const opt = document.createElement('option');
      opt.value = value;
      opt.textContent = value;
      filter.appendChild(opt);
    });
  }

  filter.addEventListener('change', (event) => {
    const maxPrice = event.target.value;
    const cards = document.querySelectorAll('.place-card');

    cards.forEach(card => {
      const price = parseInt(card.getAttribute('data-price'));
      if (maxPrice === 'All' || price <= parseInt(maxPrice)) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  });
}

// récupérer l'ID du lieu depuis l'URL
function getPlaceIdFromURL() {
  const query = window.location.search;
  const params = new URLSearchParams(query);
  return params.get('id');
}

// fetch des détails du lieu depuis l'API
async function fetchPlaceDetails(placeId, token) {
  try {
    const headers = {};
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
      method: 'GET',
      headers: headers
    });

    if (!response.ok) {
      throw new Error('Could not fetch place details');
    }

    const place = await response.json();
    displayPlaceDetails(place);
    displayReviews(place.reviews || []);

  } catch (error) {
    alert('Error: ' + error.message);
  }
}

// afficher les infos du lieu
function displayPlaceDetails(place) {
  const detailsSection = document.getElementById('place-details');
  detailsSection.innerHTML = ''; // reset

  const infoDiv = document.createElement('div');
  infoDiv.className = 'place-info';
  infoDiv.innerHTML = `
    <h2>${place.title}</h2>
    <p>Hosted by: ${place.owner ? place.owner.first_name + ' ' + place.owner.last_name : 'Unknown'}</p>
    <p>Price: $${place.price} per night</p>
    <p>${place.description}</p>
    <ul class="amenities">
      ${place.amenities && place.amenities.length > 0 ? place.amenities.map(amenity => `<li>${amenity.name || amenity}</li>`).join('') : '<li>No amenities listed</li>'}
    </ul>
  `;
  detailsSection.appendChild(infoDiv);
}

// afficher les avis
function displayReviews(reviews) {
  const reviewsSection = document.getElementById('reviews');
  reviewsSection.innerHTML = '';

  if (!reviews.length) {
    reviewsSection.innerHTML = '<p>No reviews yet.</p>';
    return;
  }

  reviews.forEach(review => {
    const card = document.createElement('div');
    card.className = 'review-card';
    card.innerHTML = `
      <p>"${review.text || review.comment}"</p>
      <p>- ${review.user_name || 'Anonymous'} ⭐${'⭐'.repeat(review.rating - 1)}</p>
    `;
    reviewsSection.appendChild(card);
  });
}
