// Scripts for the index.html template

let sessionId = localStorage.getItem("session_id");
if (!sessionId) {
    // We could generate an ID here but it's a bit hacky. We should have set one from the server.
    console.error("Error: No session id found in local storage");
}

document.getElementById("chat-form").addEventListener("submit", async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const responseDiv = document.getElementById("response");

    responseDiv.innerHTML = `<p>Waiting for AI response...</p>`;

    const response = await fetch("/chat", {
        method: "POST",
        body: formData,
    });

    const data = await response.json();
    if (data.session_id) {
        sessionId = data.session_id;
        localStorage.setItem("session_id", sessionId);
    }

    responseDiv.innerHTML = `<p>${data.response}</p>`;
});
