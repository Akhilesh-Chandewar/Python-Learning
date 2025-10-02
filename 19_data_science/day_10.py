import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------
# 1. Load dataset
# -----------------------
@st.cache_data
def load_data():
    df = pd.read_csv("day_8_books.csv")
    return df


df = load_data()


# -----------------------
# 2. Compute TF-IDF and cosine similarity
# -----------------------
@st.cache_resource
def compute_cosine_sim(df):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(df["description"])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim


cosine_sim = compute_cosine_sim(df)

# -----------------------
# 3. Map book titles to indices
# -----------------------
indices = pd.Series(df.index, index=df["title"]).to_dict()


# -----------------------
# 4. Recommendation function
# -----------------------
def get_recommendations(title, cosine_sim=cosine_sim, top_n=5):
    if title not in indices:
        return f"Title '{title}' not found in dataset."

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1 : top_n + 1]  # exclude the book itself

    book_indices = [i[0] for i in sim_scores]
    return df["title"].iloc[np.array(book_indices)].tolist()


# -----------------------
# 5. Streamlit UI
# -----------------------
st.title("Book Recommendation System")
st.write("Enter a book title to get similar book recommendations based on description:")

book_input = st.text_input("Book Title:")

if st.button("Get Recommendations"):
    if not book_input.strip():
        st.warning("Please enter a book title!")
    else:
        recommendations = get_recommendations(book_input)
        if isinstance(recommendations, str):
            st.error(recommendations)
        else:
            st.success("Recommended Books:")
            for i, rec in enumerate(recommendations, start=1):
                st.write(f"{i}. {rec}")

# -----------------------
# Optional: Show dataset
# -----------------------
if st.checkbox("Show Book Dataset"):
    st.write(df)
