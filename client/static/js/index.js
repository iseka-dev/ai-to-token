window.onload = () => {
  const form = document.getElementById("introduce-prompt-form");

  form.addEventListener("submit", event => {
    event.preventDefault();

    const url = "http://localhost:8000/v1/generate-img-from-ai/";

    const data = { "input": document.getElementById("texto").value };

    const options = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    };

    fetch(url, options).then(response => {
      return response.text();
    })
    .then(html => {
    const container = document.getElementById("new-container");
    container.innerHTML = "";
    container.innerHTML = html;
    function loadJS(FILE_URL, async = true) {
        let scriptEle = document.createElement("script");
      
        scriptEle.setAttribute("src", FILE_URL);
        scriptEle.setAttribute("type", "text/javascript");
        scriptEle.setAttribute("async", async);
      
        document.body.appendChild(scriptEle);
      
        // success event 
        scriptEle.addEventListener("load", () => {
          console.log("File loaded")
        });
          // error event
        scriptEle.addEventListener("error", (ev) => {
          console.log("Error on loading file", ev);
        });
      }
      loadJS("../static/js/mint_nft.js", true);
    })
    .catch(error => console.error(error));
  });
};
