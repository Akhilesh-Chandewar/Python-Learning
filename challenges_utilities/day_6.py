import datetime

entry = input("What did you learn today? ").strip()
rating = input("* Rate your productivity today (1-5), optional: ").strip()

now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d %H:%M:%S")

journal_entry = f"\n{date_str}\n{entry}\n"

# Add rating if valid
if rating:
    if rating.isdigit() and 1 <= int(rating) <= 5:
        journal_entry += f"Productivity Rating: {rating}/5\n"
    else:
        journal_entry += "Productivity Rating: (Invalid input)\n"

journal_entry += "_" * 80 + "\n"

with open("learning_journal.txt", "a", encoding="utf-8") as f:
    f.write(journal_entry)

print("\n✅ Journal entry saved successfully!")
