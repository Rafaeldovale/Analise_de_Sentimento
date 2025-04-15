from textblob import TextBlob

with open('./inputs/sentencas.txt', 'r') as f:
    conteudo = f.read()
    secoes = conteudo.split('Sentenças de ')
    sentencas_terror = [s.strip() for s in secoes[1].split('\n') if s.strip()]
    sentencas_comedia = [s.strip() for s in secoes[2].split('\n') if s.strip()]

print("Análise de Sentimentos - Sentenças de Terror:")
resultados_terror = []
for sentenca in sentencas_terror:
    analise = TextBlob(sentenca)
    polaridade = analise.sentiment.polarity
    subjetividade = analise.sentiment.subjectivity
    resultados_terror.append([sentenca, polaridade, subjetividade])
    print(f"Sentença: {sentenca}")
    print(f"Polaridade: {polaridade:.2f}")
    print(f"Subjetividade: {analise.sentiment.subjectivity:.2f}\n")

print("\nAnálise de Sentimentos - Sentenças de Comédia:")
resultados_comedia = []
for sentenca in sentencas_comedia:
    analise = TextBlob(sentenca)
    polaridade = analise.sentiment.polarity
    subjetividade = analise.sentiment.subjectivity
    resultados_comedia.append([sentenca, polaridade, subjetividade])
    print(f"Sentença: {sentenca}")
    print(f"Polaridade: {analise.sentiment.polarity:.2f}")
    print(f"Subjetividade: {analise.sentiment.subjectivity:.2f}\n")

# Calculando as médias
def calcular_media(lista_resultados):
    polaridades = [res[1] for res in lista_resultados]
    subjetividades = [res[2] for res in lista_resultados]
    return sum(polaridades) / len(polaridades) if polaridades else 0, sum(subjetividades) / len(subjetividades) if subjetividades else 0

media_terror_polaridade, media_terror_subjetividade = calcular_media(resultados_terror)
media_comedia_polaridade, media_comedia_subjetividade = calcular_media(resultados_comedia)

print("\nMédia das Polaridades:")
print(f"Terror: {media_terror_polaridade:.2f}")
print(f"Comédia: {media_comedia_polaridade:.2f}")

print("\nMédia das Subjetividades:")
print(f"Terror: {media_terror_subjetividade:.2f}")
print(f"Comédia: {media_comedia_subjetividade:.2f}")