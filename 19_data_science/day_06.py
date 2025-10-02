import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

# -----------------------
# 1. Generate synthetic dataset
# -----------------------
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

# Create larger dataset by repeating and adding small variations
toxic_data = toxic_comments * 10  # 50 toxic comments
supportive_data = supportive_comments * 10  # 50 supportive comments

# Optional: add small variations for realism
toxic_data = [c + "!" if i % 2 == 0 else c for i, c in enumerate(toxic_data)]
supportive_data = [c + "!" if i % 2 == 0 else c for i, c in enumerate(supportive_data)]

# Combine into dataframe
data = pd.DataFrame(
    {
        "comment": toxic_data + supportive_data,
        "label": ["toxic"] * len(toxic_data) + ["supportive"] * len(supportive_data),
    }
)

# Save dataset (optional)
data.to_csv("day_5_comments.csv", index=False)

# -----------------------
# 2. Load and clean dataset
# -----------------------
dataframe = pd.read_csv("day_5_comments.csv")
dataframe = dataframe.dropna(subset=["comment", "label"])
dataframe["label"] = dataframe["label"].str.strip().str.lower()

# -----------------------
# 3. Encode labels
# -----------------------
encoder = LabelEncoder()
dataframe["label"] = encoder.fit_transform(
    dataframe["label"]
)  # supportive -> 0, toxic -> 1

# -----------------------
# 4. Train-test split
# -----------------------
X_train, X_test, y_train, y_test = train_test_split(
    dataframe["comment"],
    dataframe["label"],
    test_size=0.2,  # 20% test
    random_state=42,
    stratify=dataframe["label"],
)

# -----------------------
# 5. Build pipeline
# -----------------------
model = Pipeline(
    [
        ("vectorizer", CountVectorizer()),
        ("tfidf", TfidfTransformer()),
        ("classifier", LogisticRegression(solver="liblinear", class_weight="balanced")),
    ]
)

# -----------------------
# 6. Train model
# -----------------------
model.fit(X_train, y_train)

# -----------------------
# 7. Evaluate
# -----------------------
score = model.score(X_test, y_test)
print(f"Model Accuracy: {score * 100:.2f}%")

y_pred = model.predict(X_test)
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print(
    "\nClassification Report:\n",
    classification_report(y_test, y_pred, target_names=encoder.classes_),
)

# -----------------------
# 8. Sample predictions
# -----------------------
samples = [
    "You are amazing, keep going!",
    "This is the dumbest thing ever.",
    "I really appreciate your effort!",
    "Nobody wants to hear your opinion.",
]
preds = model.predict(samples)
print("\nSample Predictions:")
for text, label in zip(samples, preds):
    print(f"{text}  --->  {encoder.inverse_transform([label])[0]}")
