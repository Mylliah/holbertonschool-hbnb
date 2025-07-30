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

// fonction pour déconnecter l'utilisateur
function logoutUser() {
  // Supprimer le cookie token
  document.cookie = "token=; path=/; max-age=0";
  // Recharger la page pour mettre à jour l'interface
  window.location.reload();
}

document.addEventListener("DOMContentLoaded", () => {
  const currentPage = window.location.pathname;

  if (currentPage.includes("place.html")) {
    const placeId = getPlaceIdFromURL();
    const token = getCookie("token");
    const addReviewSection = document.getElementById("add-review");
    const loginLink = document.querySelector(".login-button");
    const connected = document.querySelector(".connected");
    const logoutButton = document.querySelector(".logout-button");
    const review = document.getElementById("add-review");

    if (!token) {
      loginLink.style.display = "block"; // Non connecté
      connected.style.display = "none";
      if (logoutButton) logoutButton.style.display = "none";
      review.style.display = "none";
    } else {
      loginLink.style.display = "none"; // Connecté
      connected.style.display = "block";
      if (logoutButton) logoutButton.style.display = "block";
      review.style.display = "block";

      const welcome = document.createElement("p");
      welcome.innerHTML = `Connected`;
      connected.appendChild(welcome);

      loadHTMLWithScripts("add-review", "add_review.html");
    }
    fetchPlaceDetails(placeId, token);
  }
});

// récupérer l'ID du lieu depuis l'URL
function getPlaceIdFromURL() {
  const query = window.location.search;
  const params = new URLSearchParams(query);
  return params.get("id");
}

// fetch des détails du lieu depuis l'API
async function fetchPlaceDetails(placeId, token) {
  try {
    const headers = {};
    if (token) {
      headers["Authorization"] = `Bearer ${token}`;
    }

    const response = await fetch(
      `http://127.0.0.1:5000/api/v1/places/${placeId}`,
      {
        method: "GET",
        headers: headers,
      }
    );

    if (!response.ok) {
      throw new Error("Could not fetch place details");
    }

    const place = await response.json();
    displayPlaceDetails(place);
    displayPlacePicture(place);
    displayReviews(place.reviews || []);
  } catch (error) {
    alert("Error: " + error.message);
  }
}

// afficher les infos du lieu
function displayPlaceDetails(place) {
  const detailsSection = document.getElementById("place-details");
  detailsSection.innerHTML = ""; // reset

  const infoDiv = document.createElement("div");
  infoDiv.className = "place-info";
  infoDiv.innerHTML = `
    <h2>${place.title}</h2>
    <p>Hosted by: ${
      place.owner
        ? place.owner.first_name + " " + place.owner.last_name
        : "Unknown"
    }</p>
    <p>Price: $${place.price} per night</p>
    <p>${place.description}</p>
    <ul class="amenities">
      ${
        place.amenities && place.amenities.length > 0
          ? place.amenities
              .map((amenity) => `<li>${amenity.name || amenity}</li>`)
              .join("")
          : "<li>No amenities listed</li>"
      }
    </ul>
  `;
  detailsSection.appendChild(infoDiv);
}

// afficher l'image du lieu
function displayPlacePicture(place) {
  const pictureSection = document.getElementById("place-picture");
  pictureSection.innerHTML = ""; // reset

  if (place.picture) {
    const img = document.createElement("img");
    img.src = place.picture;
    img.alt = place.title || "Place image";
    pictureSection.appendChild(img);
  } else {
    // Image par défaut si aucune image n'est fournie
    const img = document.createElement("img");
    img.src =
      "https://www.archi-wiki.org/images/thumb/1/16/Gommersdorf_%28pignon%29_DSC04951.jpg/300px-Gommersdorf_%28pignon%29_DSC04951.jpg";
    img.alt = "Default place image";
    pictureSection.appendChild(img);
  }
}

// afficher les avis
function displayReviews(reviews) {
  const reviewsSection = document.getElementById("reviews");
  reviewsSection.innerHTML = "";

  // Ajouter un titre à la section
  const title = document.createElement("h3");
  title.textContent = "Reviews";
  reviewsSection.appendChild(title);

  if (!reviews.length) {
    reviewsSection.innerHTML += "<p>No reviews yet.</p>";
    return;
  }

  reviews.forEach((review) => {
    const card = document.createElement("div");
    card.className = "review-card";
    card.innerHTML = `
      <p>"${review.text || review.comment}"</p>
      <p>- ${review.user.first_name || "Anonymous"} ⭐${"⭐".repeat(
      review.rating - 1
    )}</p>
    `;
    reviewsSection.appendChild(card);
  });
}

async function loadHTMLWithScripts(containerId, url) {
  const container = document.getElementById(containerId);
  const response = await fetch(url);
  const html = await response.text();

  const temp = document.createElement("div");
  temp.innerHTML = html;

  // Séparer les scripts avant d'insérer le HTML
  const scripts = temp.querySelectorAll("script");
  scripts.forEach((script) => script.remove());

  // Insérer le HTML SANS les <script>
  container.innerHTML = temp.innerHTML;

  // Puis insérer les <script> un par un, ce qui les exécute
  scripts.forEach((script) => {
    const newScript = document.createElement("script");
    if (script.src) {
      // Ajoute un paramètre pour forcer le rechargement (évite cache)
      newScript.src = script.src + "?v=" + Date.now();
      newScript.async = false;
    } else {
      newScript.textContent = script.textContent;
    }
    document.body.appendChild(newScript); // ou container.appendChild
  });
}
