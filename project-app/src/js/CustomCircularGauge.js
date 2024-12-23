import React from "react";
import Gauge from "react-gauge-component";
import "../CSS/CustomCircularGauge.css"; // Import the CSS file

function CustomCircularGauge({ percent_hate = 0 }) {
  return (
    <div className="containers">
      <div className="gauge-container">
        <h1>Confidence</h1>
        <Gauge
          value={percent_hate} // The value the pointer points to
          min={0} // Minimum value of the gauge
          max={100} // Maximum value of the gauge
          pointer={{
            // Pointer customization
            color: "#ff0000", // Pointer color
            length: 60, // Pointer length (as a percentage of radius)
            strokeWidth: 2, // Pointer thickness
          }}
        />
      </div>
    </div>
  );
}

export default CustomCircularGauge;
