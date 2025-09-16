class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw = "water , milk , ginger , honey"

print(ChaiUtils.clean_ingredients(raw))