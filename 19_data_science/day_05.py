import pandas as pd
import numpy as np

# Toxic comments (negative, offensive, rude)
toxic_comments = [
    "You're so dumb, I can’t believe you wrote this.",
    "This is the worst thing I’ve ever read.",
    "Nobody cares about your opinion.",
    "Stop talking, you sound pathetic.",
    "What a useless post, you should just quit.",
]

# Supportive comments (positive, kind, encouraging)
supportive_comments = [
    "This is a really thoughtful post, thank you for sharing.",
    "Great job! You explained that really well.",
    "I appreciate the effort you put into this.",
    "Keep going, you’re doing amazing!",
    "That’s a smart perspective, I learned something new.",
]

data = pd.DataFrame(
    {
        "comment": toxic_comments + supportive_comments,
        "label": ["toxic"] * len(toxic_comments)
        + ["supportive"] * len(supportive_comments),
    }
)

data.to_csv("day_5_comments.csv", index=False)