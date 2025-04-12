### title: 
Machine-Learning-Based-Smart-Book-Recommendation-System


---

### description: >
  A smart book recommendation system built using Machine Learning.
  This web application helps users discover relevant books based on
  their interests, using genre-based filtering and intelligent recommendations.


---

### technologies_used:
  frontend:
    - React (Core React, no Vite)
    - CSS for styling (modularized by component)
  backend:
    - Flask (Python)
    - JWT Authentication
    - RESTful API design
  database:
    - MongoDB


---


### features:
  - User authentication (Signup & Login)
  - JWT-based protected routes
  - Genre-based book recommendation system
  - Viewing previously saved recommendations
  - Filtering and sorting functionality
  - Simple and intuitive UI
  - Responsive design
  - Logout functionality
  - Static About Us and Contact Us pages

---


### project_structure:
  - backend/
    - app.py
    - recommendation_routes.py
    - jwt_helper.py
    - config.py
  - frontend/
    - components/
      - Navbar.js
      - PrivateRoute.js
    - pages/
      - Home.js
      - Login.js
      - Signup.js
      - Recommendations.js
      - AboutUs.js
      - ContactUs.js
    - styles/
      - Navbar.css
      - Login.css
      - Signup.css
      - Recommendations.css
      - AboutUs.css
      - ContactUs.css
  - public/
    - index.html
  - App.js
  - index.js

---


### installation:
  frontend:
    - Run `npm install`
    - Start server: `npm start`
  backend:
    - Create virtual environment
    - Install dependencies: `pip install -r requirements.txt`
    - Run server: `python app.py`

---


### routes:
  public:
    - / (Home)
    - /login
    - /signup
    - /about
    - /contact
  protected (JWT):
    - /recommendations

---


### authors:
  - Rutuj Raul (Project Developer)
  - rutujraul19@gmail.com

---


### license: 
MIT

---
