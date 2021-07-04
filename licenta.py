import rowordnet
from DtSAlgotithm import *
from nltk.tokenize import word_tokenize

rwn = rowordnet.RoWordNet()


# sentence = 'In luna martie înfloresc florile, cea mai frumoasa lună a anului.'
sentence = 'Zăpada a acoperit tot orașul peste noapte.'
# sentence = 'Telegrama îl anunţa pe doctor de sosirea mamei lui, a doua zi.'

word = 'zăpada'

# print(DtSAlgorithm(word, sentence))


sentence = word_tokenize(sentence)
sentence = removeStopWordsROSymbolsDigits(sentence)
# print(sentence)

listOfSynsetsDefinition = []
fullListOfSynsetDefinition = []
resultListOfWeight = []
countList = []

fullListOfSynsetDefinition = fullListOfSynsetDefinitionByWord(word)
listOfSynsetsDefinition = listOfSynsetDefinitionByWord(word)
# print(fullListOfSynsetDefinition)

resultListOfWeight, count = clculateTheWeightForEverySentence(sentence, listOfSynsetsDefinition, word)
print("Sentence: " + str(sentence))
print("ListOfSynsets: " + str(listOfSynsetsDefinition))
print("Word: " + word)

print(resultListOfWeight)

indexOfMaxWeight = checkMostBigestWeightOfSentence(resultListOfWeight, listOfSynsetsDefinition, count)
result = printTheContextualDefinition(indexOfMaxWeight, fullListOfSynsetDefinition)

print(result)

