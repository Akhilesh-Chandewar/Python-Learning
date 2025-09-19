def friendship_score(name1: str, name2: str) -> int:
    name1 = name1.lower().strip()
    name2 = name2.lower().strip()
    shared_letters  = set(name1) & set(name2)
    vowels = set("aeiou")
    score = 0
    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10
    return min(score, 100)

name1 = input("Enter name 1: ")
name2 = input("Enter name 2: ")
score = friendship_score(name1, name2)
print(f"Friendship score between {name1} and {name2}: {score}")