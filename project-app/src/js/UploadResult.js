import React from "react";
import { useLocation } from "react-router-dom";

function UploadResult() {
  const location = useLocation();
  const { result } = location.state || {}; // Access the result passed from the previous page

  return (
    <div className="container">
      <h1>Upload Result</h1>
      {result ? (
        <div>
          <h3>Processed Image Details:</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre> {/* Display result */}
        </div>
      ) : (
        <p>No result to display.</p>
      )}
    </div>
  );
}

export default UploadResult;
