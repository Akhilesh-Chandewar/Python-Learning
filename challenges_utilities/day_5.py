emoji_map = {
    "happy" : ":)",
    "sad" : ":(",
    "excited" : ":D",
    "angry" : ":|",
    "confused" : ":/"
}

message = input("Enter your message: ").strip().lower()

for word in message.split():
    if word in emoji_map:
        print(emoji_map[word] , end=" ")
    else:
        print(word , end=" ")

