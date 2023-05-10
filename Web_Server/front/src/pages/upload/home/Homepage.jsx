import React from "react";
import "./Homepage.css";
import Navbar from "../../../components/navbar/Navbar";

// const footer = document.querySelector(".footer");

// window.addEventListener("scroll", () => {
//   if (window.pageYOffset > 100) {
//     footer.classList.add("visible");
//   } else {
//     footer.classList.remove("visible");
//   }
// });
function Homepage({ children, onStateChange }) {
  return (
    <>
      <Navbar />
      <div className="page-container">
        <div className="section-1 section">
          <h1>What we're all about?</h1>
          <p>
            Introducing our cutting-edge video indexing service designed to
            revolutionize your learning experience! With our advanced
            technology, you can easily search and access relevant video content
            in mere seconds, allowing you to focus on what truly matters -
            learning and expanding your knowledge.
          </p>
        </div>

        <div className="section-2 section">
          <p className="second-p">
            Our indexing system is lightning-fast, providing you with
            lightning-fast results and an intuitive user interface that is both
            user-friendly and visually stunning. Whether you're a student,
            teacher, or lifelong learner, our video indexing service is the
            ultimate tool for unlocking the full potential of online video
            content. Say goodbye to endless scrolling and hello to instant
            gratification with our video indexing service for learning!
          </p>
        </div>

        <div className="section-3 section">
          <h1>So how it works?</h1>
          <p>Lorem ipsum...</p>
        </div>

        <div className="section-4 section">
          <h1>Lorem ipsu...</h1>
          <button className="get-started-button">Get Started!</button>
        </div>
      </div>
      <footer className="footer">
        <a className="contact-btn">contact us</a>
        <a className="contact-btn">contact us2</a>
        <a className="contact-btn">contact us3</a>
      </footer>
    </>
  );
}

export default Homepage;