from flask import Blueprint, request, jsonify
from config import get_db
from utils.jwt_helper import verify_token
from bson.objectid import ObjectId

rec_bp = Blueprint("recommendation", __name__)
db = get_db()

def get_books_by_genre(tag_keyword, limit=10):
    books_collection = db["books"]

    matching_genres = books_collection.find(
        {"genres": {"$regex": tag_keyword, "$options": "i"}}
    ).limit(limit)

    books = []
    for book in matching_genres:
        books.append({
            "title": book.get("title"),
            "author": book.get("authors"),
            "tags": book.get("genres", []),  # Use 'genres' as 'tags' in frontend
            "average_rating": book.get("average_rating"),
            "image_url": book.get("image_url")
        })

    return books

@rec_bp.route("/recommend", methods=["POST"])
def recommend_books():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"error": "Token missing"}), 401

    # Extract Bearer token
    token = auth_header.split(" ")[1] if auth_header.startswith("Bearer ") else auth_header

    user_id = verify_token(token)
    if not user_id:
        return jsonify({"error": "Invalid or expired token"}), 401

    data = request.get_json()
    tag_keyword = data.get("keyword")

    if not tag_keyword:
        return jsonify({"error": "Keyword is required"}), 400

    recommendations = get_books_by_genre(tag_keyword)

    # Save recommendations to user profile
    db["users"].update_one(
        {"_id": ObjectId(user_id)},
        {"$push": {
            "saved_recommendations": {
                "keyword": tag_keyword,
                "results": recommendations
            }
        }}
    )

    return jsonify({"recommendations": recommendations})
