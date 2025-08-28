import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("stopwords")


class Preprocessor:
    def __init__(self, stop_words=None):
        self.stop_words = stop_words or set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text: str):
        """
        Cleans text:
        - Removes punctuation and unique symbols
        - Converts to lowercase
        - Removes tabs, extra spaces, and stop words
        - Performs lemmatization
        """
        text = text.lower()
        text = "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in text)
        words = text.strip().split()
        words = [self.lemmatizer.lemmatize(w) for w in words if w not in self.stop_words]
        return " ".join(words)


if __name__ == "__main__":
    preprocessor = Preprocessor()

    sample_text = "The cats are sitting on the mat, and the dogs are running!"
    cleaned_text = preprocessor.clean_text(sample_text)

    print("Original Text:")
    print(sample_text)
    print("\nCleaned Text:")
    print(cleaned_text)
