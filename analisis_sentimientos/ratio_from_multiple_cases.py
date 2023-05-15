from faker import Faker
from textblob import TextBlob
from googletrans import Translator

from analisis_sentimientos.domain.AnalyzedSentence import AnalyzedSentence
from analisis_sentimientos.util import SentenceUtils
from matplotlib_lib.MatPlotScatter.MatPlotScatter import MatPlotScatterData, MatPlotScatter

fake = Faker()
# sentences = [fake.sentence() for _ in range(10)] crear de forma aleatorio

sentences = [
    "I love spending time with my family.",
    "The beach is my favorite place to relax.",
    "I am really excited about my new job.",
    "My favorite hobby is playing the guitar.",
    "I always feel happy when I eat ice cream.",
    "The movie I watched last night was very boring.",
    "I am so tired of this rainy weather.",
    "I can't wait to travel to Europe next summer.",
    "I feel really stressed out about my upcoming exam.",
    "My best friend always knows how to make me laugh."
]

if SentenceUtils.sentence_is_not_in_english(sentences):
    translator = Translator()
    translated_sentences = []

    for sentence in sentences:
        translated_sentences.append(translator.translate(sentence, src='en', dest='es'))

    sentences = translated_sentences

formalized_sentences = []

for index, sentence in enumerate(sentences):
    blob = TextBlob(sentence)
    analyzed = AnalyzedSentence(index, sentence, blob.polarity)
    formalized_sentences.append(analyzed)

graphic_data = []

for sentence in formalized_sentences:
    graphic_data.append(MatPlotScatterData(sentence.id, sentence.polarity))

scatter = MatPlotScatter(graphic_data)
scatter.plot()
print(sentences)
