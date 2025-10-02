import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

# =======================
# 1. Load Dataset
# =======================
dataframe = pd.read_csv("day_5_comments.csv")

# Drop missing rows (if any)
dataframe = dataframe.dropna(subset=["comment", "label"])

# Normalize labels (remove spaces, lowercase)
dataframe["label"] = dataframe["label"].str.strip().str.lower()

# =======================
# 2. Encode Labels
# =======================
encoder = LabelEncoder()
dataframe["label"] = encoder.fit_transform(dataframe["label"])
# supportive -> 0, toxic -> 1 (consistent mapping)

# =======================
# 3. Train-Test Split
# =======================
X_train, X_test, y_train, y_test = train_test_split(
    dataframe["comment"],
    dataframe["label"],
    test_size=0.3,  # keep 30% for testing
    random_state=42,
    stratify=dataframe["label"],  # keep class balance
)

# =======================
# 4. Build Pipeline
# =======================
model = Pipeline(
    [
        ("vectorizer", CountVectorizer()),  # text → counts
        ("tfidf", TfidfTransformer()),  # counts → TF-IDF
        (
            "classifier",
            LogisticRegression(
                solver="liblinear", class_weight="balanced"  # handle imbalance
            ),
        ),
    ]
)

# =======================
# 5. Train Model
# =======================
model.fit(X_train, y_train)

# =======================
# 6. Evaluate
# =======================
score = model.score(X_test, y_test)
print(f"Model Accuracy: {score * 100:.2f}%")

y_pred = model.predict(X_test)

print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print(
    "\nClassification Report:\n",
    classification_report(y_test, y_pred, target_names=encoder.classes_),
)

# =======================
# 7. Try Predictions
# =======================
samples = ["You are amazing, keep going!", "This is the dumbest thing ever."]
preds = model.predict(samples)
print("\nSample Predictions:")
for text, label in zip(samples, preds):
    print(f"{text}  --->  {encoder.inverse_transform([label])[0]}")
