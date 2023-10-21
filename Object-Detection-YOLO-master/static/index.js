window.onload = () => {
  $("#sendbutton").click(() => {
    imagebox = $("#imagebox");
    input = $("#imageinput")[0];
    if (input.files && input.files[0]) {
      let formData = new FormData();
      formData.append("image", input.files[0]);
      imagebox.hide(); //ซ่อนรูป
      $.ajax({
        url: "http://localhost:5000/detectObject", // fix this to your liking
        type: "POST",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        error: function (data) {
          console.log("upload error", data);
          console.log(data.getAllResponseHeaders());
        },
        success: function (data) {
          console.log(data);
          //bytestring = data["status"];
          // image = bytestring.split("'")[1];
          //imagebox.attr("src", "data:image/jpeg;base64," + image);

          // Display the count of detected persons
          let personCount = data["person_count"];
          let chair_count = data["chair_count"];
          $("#personCount").text(`Detected Persons: ${personCount}`);
          $("#chairCount").text("Number of chairs detected: " + chair_count);

          // แสดงตำแหน่งของผู้คนและเก้าอี้
          let person_positions = data["person_positions"];
          let chair_positions = data["chair_positions"];

          // แสดงผลใน HTML elements
          $("#person_positions").html(
            `Person Positions:<br>${JSON.stringify(person_positions)
              .split("},{")
              .join("},<br>{")}`
          );
          $("#chair_positions").html(
            `Chair Positions:<br>${JSON.stringify(chair_positions)
              .split("},{")
              .join("},<br>{")}`
          );
        },
      });
    }
  });
};

function readUrl(input) {
  imagebox = $("#imagebox");
  console.log("evoked readUrl");
  if (input.files && input.files[0]) {
    let reader = new FileReader();
    reader.onload = function (e) {
      // console.log(e)

      imagebox.attr("src", e.target.result);
      imagebox.height(500);
      imagebox.width(800);
    };
    reader.readAsDataURL(input.files[0]);
  }
}
