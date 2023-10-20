document
  .querySelector("form")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    // Get the selected files
    const xmlFile = document.querySelector('input[name="xml_file"]').files[0];
    const imageFile = document.querySelector('input[name="image_file"]')
      .files[0];

    // Create a FormData object and append files to it
    const formData = new FormData();
    formData.append("xml_file", xmlFile);
    formData.append("image_file", imageFile);

    // Send a POST request to the server
    const response = await fetch("/detect", {
      method: "POST",
      body: formData,
    });

    // Parse the JSON response
    const responseData = await response.json();

    // Display the image with bounding boxes
    const detectedObjectsDiv = document.getElementById("detected_objects");
    detectedObjectsDiv.innerHTML = `<h2>Detected Objects:</h2><img src="${responseData.image_path}" alt="Detected Objects">`;
  });
