class Preprocessor:
    def __init__(self, stop_words=None):
        self.stop_words = stop_words or {
            "the", "is", "at", "on", "a", "an",
            "and", "to", "of", "in"
        }

    def clean_text(self, text: str):
        text = text.lower()

        cleaned = "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in text)

        words = cleaned.strip().split()
        words = [w for w in words if w not in self.stop_words]

        return " ".join(words)