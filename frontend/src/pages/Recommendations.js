import React, { useState } from "react";
import axios from "axios";
import "./../styles/Recommendations.css";

function Recommendations() {
  const [keyword, setKeyword] = useState("");
  const [recommendations, setRecommendations] = useState([]);

  const fetchRecommendations = async () => {
    const token = localStorage.getItem("token");

    if (!token) {
      console.error("No token found");
      return;
    }

    try {
      const response = await axios.post(
        "http://localhost:5000/api/recommend",
        { keyword },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setRecommendations(response.data.recommendations || []);
      console.log("API Response:", response.data.recommendations);
    } catch (error) {
      console.error("Error fetching recommendations:", error);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.href = "/login";
  };

  return (
    <div className="recommendations-container">
      <div className="rec-header">
        <h2>Book Recommendations</h2>
        <button className="logout-btn" onClick={handleLogout}>Logout</button>
      </div>

      <input
        type="text"
        placeholder="Enter a genre or keyword (e.g., fiction)"
        value={keyword}
        onChange={(e) => setKeyword(e.target.value)}
      />
      <button onClick={fetchRecommendations}>Get Recommendations</button>

      <div className="book-grid">
        {recommendations.map((book, index) => (
          <div className="book-card" key={index}>
            <img src={book.image_url} alt={book.title} />
            <h3>{book.title}</h3>
            <p>By: {book.author}</p>
            <p>Rating: {book.average_rating}</p>
            {/* <div className="tags">
              {book.tags.map((tag, i) => (
                <span className="tag" key={i}>{tag}</span>
              ))}
            </div> */}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Recommendations;
