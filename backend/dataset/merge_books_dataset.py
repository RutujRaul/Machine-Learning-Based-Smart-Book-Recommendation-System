import pandas as pd
import json
from collections import defaultdict

# Load CSV files
books_df = pd.read_csv('books.csv')
book_tags_df = pd.read_csv('book_tags.csv')
tags_df = pd.read_csv('tags.csv')

# Merge book_tags with tags to get tag names
merged_tags = pd.merge(book_tags_df, tags_df, on='tag_id')

# Group tags for each goodreads_book_id
book_tags_dict = defaultdict(set)
for _, row in merged_tags.iterrows():
    book_id = row['goodreads_book_id']
    tag_name = row['tag_name']
    if isinstance(tag_name, str):
        book_tags_dict[book_id].add(tag_name.lower())

# Build cleaned book data
book_data = []
for _, row in books_df.iterrows():
    goodreads_id = row['book_id']  # maps to goodreads_book_id in book_tags

    book_entry = {
        "book_id": int(row['id']),
        "title": row['title'],
        "authors": row['authors'],
        "average_rating": float(row['average_rating']),
        "ratings_count": int(row['ratings_count']),
        "image_url": row['image_url'],
        "genres": list(book_tags_dict.get(goodreads_id, []))
    }

    book_data.append(book_entry)

# Save to JSON
with open('cleaned_books.json', 'w', encoding='utf-8') as f:
    json.dump(book_data, f, indent=4)

print(f"[✅] cleaned_books.json created with {len(book_data)} entries")
