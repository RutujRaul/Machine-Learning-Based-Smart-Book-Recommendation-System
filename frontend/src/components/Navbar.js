import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "./../styles/Navbar.css";

const Navbar = () => {
  const navigate = useNavigate();
  const isLoggedIn = localStorage.getItem("token");

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <nav className="navbar">
      <div className="navbar-logo">
        📖 SmartBookRec
      </div>
      <div className="navbar-links">
        <Link to="/">Home</Link>
        <Link to="/about">About Us</Link>
        <Link to="/contact">Contact Us</Link>
        {isLoggedIn ? (
          <>
            <Link to="/recommendations">Recommendations</Link>
            {/* Uncomment if you want to add a Logout button here */}
            {/* <button onClick={handleLogout}>Logout</button> */}
          </>
        ) : (
          <>
            <Link to="/login">Login</Link>
            <Link to="/signup">Signup</Link>
          </>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
