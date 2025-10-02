import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------
# 1. Load dataset
# -----------------------
df = pd.read_csv("day_8_books.csv")

# -----------------------
# 2. TF-IDF vectorization
# -----------------------
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["description"])

# -----------------------
# 3. Compute cosine similarity
# -----------------------
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# -----------------------
# 4. Create mapping from book title to index
# -----------------------
indices = pd.Series(df.index, index=df["title"]).to_dict()


# -----------------------
# 5. Recommendation function
# -----------------------
def get_recommendations(title, cosine_sim=cosine_sim, top_n=5):
    if title not in indices:
        return f"Title '{title}' not found in dataset."

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1 : top_n + 1]

    book_indices = [i[0] for i in sim_scores]

    return df["title"].iloc[np.array(book_indices)].tolist()


# -----------------------
# 6. Example usage
# -----------------------
book_title = "The Hobbit"
recommendations = get_recommendations(book_title)
print(f"Books similar to '{book_title}':")
for rec in recommendations:
    print("-", rec)
