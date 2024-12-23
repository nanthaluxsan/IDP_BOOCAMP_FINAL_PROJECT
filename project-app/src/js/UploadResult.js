import React from "react";
import { useLocation } from "react-router-dom";
import CustomCircularGauge from "./CustomCircularGauge";

function UploadResult() {
  const location = useLocation();
  const { result } = location.state || {}; // Access the result passed from the previous page

  // Extract confidence, label, and id safely
  const confidence = result && result[0] ? result[0]["confidence"] : null;
  const label = result && result[0] ? result[0]["label"] : null;
  const id = result && result[0] ? result[0]["id"] : null;

  return (
    <div className="container">
      <h1>Upload Result</h1>
      {result ? (
        <div>
          <h3>Processed Image Details:</h3>

          {label && (
            <div>
              <h4>Label: {label}</h4>
              <p>
                {label === "non_hateful"
                  ? "This content is non-hateful."
                  : "This content might contain hateful material."}
              </p>
            </div>
          )}
          {/* Display confidence and circular gauge */}
          {confidence !== null ? (
            <div>
              <CustomCircularGauge percent_hate={confidence} />
            </div>
          ) : (
            <p>No confidence data available.</p>
          )}
          {/* Display ID */}
          {id && (
            <p>
              <strong>Name of the meme:</strong> {id}
            </p>
          )}
        </div>
      ) : (
        <p>No result to display.</p>
      )}
    </div>
  );
}

export default UploadResult;
