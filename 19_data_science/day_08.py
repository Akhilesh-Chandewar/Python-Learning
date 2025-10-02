import pandas as pd

# -----------------------
# 1. Create dataset
# -----------------------
data = [
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "description": "Set in the 1930s American South, this novel follows Scout Finch as she learns about justice, morality, and empathy while observing her father defend an innocent black man accused of a crime.",
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "description": "In a totalitarian society dominated by surveillance and propaganda, Winston Smith struggles to maintain his individuality and sanity while secretly questioning Big Brother's regime.",
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "description": "A tale of love, ambition, and wealth in 1920s New York, following the mysterious Jay Gatsby and his obsession with the beautiful Daisy Buchanan, exploring the decay of the American Dream.",
    },
    {
        "title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "genre": "Non-fiction",
        "description": "A sweeping overview of human history, from the emergence of Homo sapiens in the Stone Age to the development of agriculture, writing, empires, and modern society, exploring how biology and culture shaped civilizations.",
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "description": "Bilbo Baggins, a quiet hobbit, is thrust into an epic adventure with dwarves and wizards to reclaim treasure from the dragon Smaug, learning courage, friendship, and self-discovery along the way.",
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "description": "Elizabeth Bennet navigates societal expectations, love, and misunderstandings in early 19th-century England, encountering the proud Mr. Darcy and discovering the challenges of marrying for love versus duty.",
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Fiction",
        "description": "Holden Caulfield, a disillusioned teenager, wanders New York City after being expelled from school, struggling with identity, isolation, and the superficiality of the adult world.",
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "description": "Harry Potter discovers he is a wizard on his 11th birthday and attends Hogwarts School of Witchcraft and Wizardry, making friends, uncovering secrets, and confronting the dark wizard who killed his parents.",
    },
    {
        "title": "The Da Vinci Code",
        "author": "Dan Brown",
        "genre": "Thriller",
        "description": "Symbologist Robert Langdon and cryptologist Sophie Neveu uncover a trail of clues hidden in works of art and historical artifacts, leading them to a religious conspiracy that could shake the foundations of Christianity.",
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": "Philosophical",
        "description": "Santiago, a young shepherd from Spain, sets out on a journey to discover a hidden treasure, learning lessons about destiny, intuition, and the interconnectedness of all life along the way.",
    },
]

# -----------------------
# 2. Convert to DataFrame
# -----------------------
df = pd.DataFrame(data)

# -----------------------
# 3. Save to CSV
# -----------------------
df.to_csv("day_8_books.csv", index=False)
print("Saved day_8_books.csv with", len(df), "rows")
