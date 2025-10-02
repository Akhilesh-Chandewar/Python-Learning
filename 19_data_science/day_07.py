import streamlit as st
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.preprocessing import LabelEncoder


# -----------------------
# 1. Load or create dataset
# -----------------------
@st.cache_data
def load_data():
    toxic_comments = [
        "You're so dumb, I can’t believe you wrote this.",
        "This is the worst thing I’ve ever read.",
        "Nobody cares about your opinion.",
        "Stop talking, you sound pathetic.",
        "What a useless post, you should just quit.",
    ]

    supportive_comments = [
        "This is a really thoughtful post, thank you for sharing.",
        "Great job! You explained that really well.",
        "I appreciate the effort you put into this.",
        "Keep going, you’re doing amazing!",
        "That’s a smart perspective, I learned something new.",
    ]

    # Repeat to enlarge dataset
    toxic_data = [
        c + "!" if i % 2 == 0 else c for i, c in enumerate(toxic_comments * 10)
    ]
    supportive_data = [
        c + "!" if i % 2 == 0 else c for i, c in enumerate(supportive_comments * 10)
    ]

    df = pd.DataFrame(
        {
            "comment": toxic_data + supportive_data,
            "label": ["toxic"] * len(toxic_data)
            + ["supportive"] * len(supportive_data),
        }
    )

    # Encode labels
    encoder = LabelEncoder()
    df["label"] = encoder.fit_transform(df["label"])

    return df, encoder


dataframe, encoder = load_data()


# -----------------------
# 2. Train model pipeline
# -----------------------
@st.cache_resource
def train_model(df):
    model = Pipeline(
        [
            ("vectorizer", CountVectorizer()),
            ("tfidf", TfidfTransformer()),
            (
                "classifier",
                LogisticRegression(solver="liblinear", class_weight="balanced"),
            ),
        ]
    )
    X_train = df["comment"]
    y_train = df["label"]
    model.fit(X_train, y_train)
    return model


model = train_model(dataframe)

# -----------------------
# 3. Streamlit UI
# -----------------------
st.title("Toxic vs Supportive Comment Classifier")
st.write("Enter a comment below to see if it is toxic or supportive:")

user_input = st.text_area("Your Comment:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a comment!")
    else:
        prediction = model.predict([user_input])[0]
        label = encoder.inverse_transform([prediction])[0]
        st.success(f"Prediction: **{label.upper()}**")

# -----------------------
# 4. Optional: show dataset sample
# -----------------------
if st.checkbox("Show Sample Dataset"):
    st.write(dataframe.sample(10))
