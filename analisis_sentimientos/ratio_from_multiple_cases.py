from textblob import TextBlob
from analisis_sentimientos.domain.AnalyzedSentence import AnalyzedSentence
from analisis_sentimientos.util import SentenceUtils
from matplotlib_lib.MatPlotScatter.MatPlotScatter import MatPlotScatterData, MatPlotScatter

sentences = SentenceUtils.obtain_data()

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
