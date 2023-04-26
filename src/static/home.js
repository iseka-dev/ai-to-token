window.onload = () => {
    const form = document.getElementById("introduce-prompt-form");

    form.addEventListener("submit", event => {
        event.preventDefault();

        const url = "http://localhost:8000/generate-img";

        const data = { "input": document.getElementById("texto").value };

        console.log(data)

        const options = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
        };

        fetch(url, options)
        .then(response => {
            return response.text();
        })
        .then(html => {
            console.log(html);
            const container = document.getElementById("new-container");
            container.innerHTML = "";
            container.innerHTML = html;
        })
        .catch(error => console.error(error));
    });
};
