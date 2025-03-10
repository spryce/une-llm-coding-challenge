// Scripts for the index.html template

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
    responseDiv.innerHTML = `<p>${data.response}</p>`;
});
