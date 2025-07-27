// fonction utilitaire pour lire un cookie
function getCookie(name) {
  const cookieString = document.cookie;
  const cookies = cookieString.split("; ");
  for (let cookie of cookies) {
    const [key, value] = cookie.split("=");
    if (key === name) {
      return value;
    }
  }
  return null;
}

// fonction pour décoder le JWT et vérifier l'expiration
function isTokenExpired(token) {
  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    const currentTime = Math.floor(Date.now() / 1000);
    return payload.exp < currentTime;
  } catch (error) {
    console.error("Error decoding token:", error);
    return true; // Considérer comme expiré si erreur de décodage
  }
}

// fonction pour déconnecter l'utilisateur
function logoutUser() {
  // Supprimer le cookie token
  document.cookie = "token=; path=/; max-age=0";
  // Recharger la page pour mettre à jour l'interface
  window.location.reload();
}

document.addEventListener("DOMContentLoaded", () => {
  const currentPage = window.location.pathname;

  if (currentPage.includes("index.html")) {
    const token = getCookie("token");
    const loginLink = document.querySelector(".login-button");
    const connected = document.querySelector(".connected");

    // Vérifier si le token existe et n'est pas expiré
    if (!token || isTokenExpired(token)) {
      // Token inexistant ou expiré - déconnecter l'utilisateur
      if (token) {
        logoutUser();
        return; // Arrêter l'exécution car la page va se recharger
      }
      loginLink.style.display = "block"; // Non connecté
      connected.style.display = "none";
    } else {
      loginLink.style.display = "none"; // Connecté
      connected.style.display = "block";

      const welcome = document.createElement("p");
      welcome.innerHTML = `Connected`;
      connected.appendChild(welcome);
    }
    fetchPlaces(); // récupérer les lieux 
    setupPriceFilter(); // initialiser le filtre de prix
  }
});

// fetch des lieux depuis l'API
async function fetchPlaces() {
  try {
    const response = await fetch("http://127.0.0.1:5000/api/v1/places", {
      method: "GET",
    });

    if (!response.ok) {
      throw new Error("Failed to fetch places");
    }

    const data = await response.json();
    displayPlaces(data.places); // afficher les lieux
  } catch (error) {
    alert("Error: " + error.message);
  }
}

function displayPlaces(places) {
  const placesList = document.getElementById("places-list");
  placesList.innerHTML = ""; // reset

  places.forEach((place) => {
    const card = document.createElement("div");
    card.className = "place-card";
    card.setAttribute("data-price", place.price); // pour filtrer

    card.innerHTML = `
      <img src="${place.picture}" alt="${place.title}">
      <div class="place-card-content">
        <h3>${place.title}</h3>
        <p class="price">$${place.price} per night</p>
        <a href="place.html?id=${place.id}" class="details-button">View Details</a>
      </div>
    `;

    placesList.appendChild(card);
  });
}

// fonction pour initialiser et gérer le filtre de prix
function setupPriceFilter() {
  const filter = document.getElementById("price-filter");
  const options = ["All", "10", "50", "100"];

  if (filter.options.length === 0) {
    options.forEach((value) => {
      const opt = document.createElement("option");
      opt.value = value;
      opt.textContent = value;
      filter.appendChild(opt);
    });
    // Définir "All" comme valeur par défaut
    filter.value = "All";
  }

  filter.addEventListener("change", (event) => {
    const maxPrice = event.target.value;
    const cards = document.querySelectorAll(".place-card");

    cards.forEach((card) => {
      const price = parseInt(card.getAttribute("data-price"));
      if (maxPrice === "All" || price <= parseInt(maxPrice)) {
        card.classList.remove("hidden");
      } else {
        card.classList.add("hidden");
      }
    });
  });
}
