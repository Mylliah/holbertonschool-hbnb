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

document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");
  if (loginForm) {
    // Listener sur le submit
    loginForm.addEventListener("submit", async (event) => {
      event.preventDefault(); // empêcher rechargement par défaut

      // Récupération des champs email/password
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      try {
        // Requête AJAX vers l'API
        const response = await fetch(
          "http://127.0.0.1:5000/api/v1/auth/login",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json", // obligatoire pour JSON
            },
            body: JSON.stringify({ email, password }), // envoi du corps JSON
          }
        );

        // Traitement de la réponse
        if (response.ok) {
          const data = await response.json();

          // Stockage du JWT dans un cookie
          document.cookie = `token=${data.access_token}; path=/; max-age=3600`;

          // Redirection vers index.html
          window.location.href = "index.html";
        } else {
          // Gestion d'erreur
          alert("Login failed: " + response.statusText);
        }
      } catch (error) {
        alert("Login failed: " + error.message); // gestion d'erreur réseau
      }
    });
  }

  const currentPage = window.location.pathname;
});
