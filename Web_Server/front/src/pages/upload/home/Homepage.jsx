import React from "react";
import "./Homepage.css";
import Navbar from "../../../components/navbar/Navbar";
// import sec1 from "../../../assets/backgrounds/sec1.jpg";
// import sec2 from "../../../assets/backgrounds/sec2.jpg";
function Homepage({ children, onStateChange }) {
  return (
    <>
      <Navbar />
      <div className="page-container">
        <div className="section-1 section">
          <h1>Lorem ipsu...</h1>
          <p>Lorem ipsum...</p>
        </div>

        <div className="section-2 section">
          <h1>Lorem ipsu...</h1>
          <p>Lorem ipsum...</p>
        </div>

        <div className="section-3 section">
          <h1>Lorem ipsu...</h1>
          <p>Lorem ipsum...</p>
        </div>

        <div className="section-4 section">
          <h1>Lorem ipsu...</h1>
          <p>Lorem ipsum...</p>
        </div>
      </div>
    </>
  );
}

export default Homepage;
