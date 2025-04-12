from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(db, username, email, password):
    users = db["users"]
    if users.find_one({"email": email}):
        return None  # Email already exists

    hashed_password = generate_password_hash(password)
    user = {
        "username": username,
        "email": email,
        "password": hashed_password,
        "saved_recommendations": []  # You can use this later
    }
    result = users.insert_one(user)
    return str(result.inserted_id)

def get_user_by_email(db, email):
    return db["users"].find_one({"email": email})

def verify_user_password(user, password):
    return check_password_hash(user["password"], password)
