document.getElementById("logoutButton").addEventListener("click", async () => {
  const response = await fetch("/api/logout", {
    method: "POST",
  });

  if (response.ok) {
    window.location.href = "http://storage.cloudsite.thm/";
  } else {
    console.error("Logout failed");
  }
});

// Function to handle response data and display messages in divs
function handleResponse(data, targetDiv) {
  console.log(data); // Log the response data
  // Update the target div with the message received in the response
  document.querySelector(targetDiv).innerHTML =
    `<p>Success: ${data.message}</p><p>File path: ${data.path}</p>`;
}

// Function to handle errors and display error messages in divs
function handleError(targetDiv) {
  console.error("Error:", error);
  // Display an error message in the target div
  document.querySelector(targetDiv).innerHTML =
    `<p style="color: red;">An error occurred while processing the request.</p>`;
}

// Event listener for file upload form submission
document
  .getElementById("uploadForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(); // Create FormData object
    formData.append("file", document.getElementById("fileInput").files[0]); // Append file to FormData

    // Use fetch to send FormData directly
    fetch("/api/upload", {
      method: "POST",
      body: formData, // Send FormData object directly
    })
      .then((response) => response.json())
      .then((data) => handleResponse(data, ".uploadLocalhost")) // Call handleResponse with target div
      .catch(() => handleError(".uploadLocalhost")); // Call handleError with target div
  });

// Event listener for URL form submission
document.getElementById("urlForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent default form submission

  const url = document.getElementById("urlInput").value;

  // Use fetch to send URL as JSON
  fetch("/api/store-url", {
    method: "POST",
    body: JSON.stringify({ url: url }), // Serialize URL as JSON
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => handleResponse(data, ".uploadUrl")) // Call handleResponse with target div
    .catch(() => handleError(".uploadUrl")); // Call handleError with target div
});

// Fetch files from the /api/uploads endpoint
fetch("/api/uploads")
  .then((response) => response.json())
  .then((files) => {
    const fileContainer = document.getElementById("fileContainer");

    files.forEach((file) => {
      // Create a div for each file
      const fileDiv = document.createElement("div");
      fileDiv.className = "file-item";

      // Create an anchor element for the file link
      const fileLink = document.createElement("a");
      fileLink.href = `/api/uploads/${file}`;
      fileLink.textContent = file;

      // Append the link to the div
      fileDiv.appendChild(fileLink);

      // Append the div to the container
      fileContainer.appendChild(fileDiv);
    });
  })
  .catch((error) => {
    console.error("Error fetching files:", error);
    const fileContainer = document.getElementById("fileContainer");
    fileContainer.innerHTML =
      "<p>Error loading files. Please try again later.</p>";
  });
