import spacy
from nltk.tokenize import word_tokenize


text = """Tratamentul glaucomului cunoaște o evoluție și aduce vești bune pentru pacienții cu această boală. Glaucomul este una dintre afecțiunile oftalmologice grave care necesită o grijă aparte."""


def partOfSentence(text):
	listText = []

	nlp = spacy.load('ro_core_news_lg')

	partText = nlp(text)

	for d in partText:
		listText.append(d.pos_)

	return listText


print(partOfSentence(text))