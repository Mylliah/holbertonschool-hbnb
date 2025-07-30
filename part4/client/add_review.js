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

// fonction pour décoder le JWT et récupérer l'user id
function getUserIdFromToken(token) {
  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    return payload.sub;
  } catch (error) {
    console.error("Error decoding token:", error);
    return null;
  }
}

// récupérer l'ID du lieu depuis l'URL
function getPlaceIdFromURL() {
  const query = window.location.search;
  const params = new URLSearchParams(query);
  return params.get("id");
}

// initialisation du formulaire
document.addEventListener("DOMContentLoaded", () => {
  const placeId = getPlaceIdFromURL();
  const placeIdInput = document.getElementById("place_id");
  
  if (placeIdInput && placeId) {
    placeIdInput.value = placeId;
  }
});

// fonction pour soumettre l'avis
async function submitReview(event) {
  if (event) {
    event.preventDefault(); // empêcher le rechargement par défaut
    event.stopPropagation(); // empêcher la propagation de l'événement
  }
  
  const token = getCookie("token");
  
  if (!token) {
    alert("You must be logged in to submit a review.");
    return false;
  }

  // récupération de l'user_id depuis le JWT
  const userId = getUserIdFromToken(token);
  if (!userId) {
    alert("Invalid authentication token.");
    return false;
  }

  // récupération des données du formulaire
  const placeId = getPlaceIdFromURL();
  const text = document.getElementById("text").value.trim();
  const rating = parseInt(document.getElementById("rating").value);

  if (!placeId || !text || !rating) {
    alert("Please fill in all fields.");
    return false;
  }

  const reviewData = {
    place_id: placeId,
    text: text,
    rating: rating,
    user_id: userId
  };

  try {
    // requête AJAX vers l'API
    const response = await fetch("http://127.0.0.1:5000/api/v1/reviews/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify(reviewData)
    });

    if (response.ok) {
      const data = await response.json();
      
      // vider le formulaire
      document.getElementById("text").value = "";
      document.getElementById("rating").value = "";
      
      // rafraîchir la page en préservant l'ID du lieu dans l'URL
      const placeId = getPlaceIdFromURL();
      window.location.href = `place.html?id=${placeId}`;
      
    } else {
      const errorData = await response.json();
      let errorMessage = "Failed to submit review";
      
      if (errorData.message) {
        errorMessage = errorData.message;
      } else if (response.status === 403) {
        errorMessage = "You cannot review your own place";
      } else if (response.status === 409) {
        errorMessage = "You have already reviewed this place";
      } else if (response.status === 400) {
        errorMessage = "Invalid review data";
      }
      
      alert(errorMessage);
    }
  } catch (error) {
    console.error("Error submitting review:", error);
    alert("Network error: Unable to submit review");
  }
}