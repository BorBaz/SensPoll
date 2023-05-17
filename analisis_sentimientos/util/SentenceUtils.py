import time

from langdetect import detect
from googletrans import Translator


def obtain_data():
    sentences = populate_sentences()
    if sentence_is_not_in_english(sentences):
        translated_sentences = []
        for sentence in sentences:
            translated_sentences.append(translate(str(sentence), 'es', 'en'))
        sentences = translated_sentences

    return sentences


def populate_sentences():
    sentences = [
        'Odio los lunes',
        'Me encanta el peso muerto',
        'Hola Mundo'
    ]
    return sentences


def sentence_is_not_in_english(sentences):
    language = detect(sentences[0])
    return language != 'en'


def translate(sentence, src, dest):
    time.sleep(2)
    translator = Translator()
    return translator.translate(sentence, src=src, dest=dest).text


sentences = [
    'Odio los lunes',
    'Me encanta el peso muerto',
    'Hola Mundo'
]

for s in sentences:
    print(translate(s, 'es', 'en'))
