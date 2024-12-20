import React, { useState } from "react";
import { useNavigate } from "react-router-dom"; // Import useNavigate from react-router-dom
import axios from "axios";
import "../CSS/style.css";

function PhotoUploadApp() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate(); // Initialize the useNavigate hook

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedFile(file);
      const filePreviewUrl = URL.createObjectURL(file);
      setPreview(filePreviewUrl);
    }
  };

  const handleSubmit = async () => {
    if (!selectedFile) {
      alert("Please select a file to submit!");
      return;
    }

    const formData = new FormData();
    formData.append("image", selectedFile);

    setLoading(true);

    try {
      const response = await axios.post(
        "http://localhost:5000/upload_image",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      // Navigate to result page and pass the response
      navigate("/result", { state: { result: response.data } });
    } catch (error) {
      console.error("Error uploading photo:", error);
      alert("Error uploading photo.");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Upload Your Photo</h1>
      <input type="file" accept="image/*" onChange={handleFileUpload} />
      {preview && (
        <div>
          <h3>Image Preview:</h3>
          <img src={preview} alt="Selected preview" className="image-preview" />
        </div>
      )}
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Uploading..." : "Submit"}
      </button>
    </div>
  );
}

export default PhotoUploadApp;
