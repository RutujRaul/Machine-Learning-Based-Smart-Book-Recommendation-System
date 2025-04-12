import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["smartbookdb"]
collection = db["books"]

# Load JSON data
with open("cleaned_books.json", "r", encoding="utf-8") as file:
    books_data = json.load(file)

# Insert into MongoDB
result = collection.insert_many(books_data)
print(f"[✅] Inserted {len(result.inserted_ids)} books into MongoDB")
