from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_bp
from routes.recommendation_routes import rec_bp

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(rec_bp, url_prefix="/api")

@app.route("/", methods=["GET"])
def home():
    return {"message": "📚 Smart Book Recommendation System Backend is Running!"}

if __name__ == "__main__":
    app.run(debug=True)
