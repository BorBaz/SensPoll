class AnalyzedSentence:
    def __init__(self, id, sentence, polarity):
        self.id = id
        self.sentence = sentence
        self.polarity = polarity

    def __str__(self) -> str:
        return f' {self.id} - {self.sentence} - {self.polarity}'
