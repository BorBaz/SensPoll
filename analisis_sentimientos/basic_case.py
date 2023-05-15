from textblob import TextBlob

# Define el texto a analizar
texto = "I fucking hate Pedro Sanchez"

# Crea un objeto TextBlob
blob = TextBlob(texto)

# Realiza el análisis de sentimiento
sentimiento = blob.sentiment.polarity

print(sentimiento)

# Imprime el resultado
if sentimiento > 0:
    print("El texto es positivo")
elif sentimiento < 0:
    print("El texto es negativo")
else:
    print("El texto es neutral")