import rowordnet
from nltk.tokenize import word_tokenize
import spacy



listOfStopWordsRO = ["a","abia","acea","aceasta","această","aceea","aceeași","acei","aceia","acel",
					"acela","același","acele","acelea","acest","acesta","aceste","acestea","acestei",
					"acestia","acestui","aceşti","aceştia","acolo","acord","acum","adica","adică","ai","aia","aibă",
					"aici","aiurea","al","ala","alături","ale","alea","alt","alta","alta","altceva","altcineva","alte",
					"altfel","alti","altii","altul","am","anume","apoi","ar","are","as","asa","asemenea","asta","ăsta",
					"astazi","astea","astfel","astăzi","asupra","atare","atât","atâta","atâtea","atâția","ați",
					"atit","atita","atitea","atitia","atunci","au","avea","avem","aveţi","avut","azi","aş","aşadar",
					"aţi","b","ba","bine","bucur","bună","c","ca","cam","cand","capat","care","careia","carora","caruia",
					"cât","către","caut","ce","cea","ceea","cei","ceilalti","cel","cele","celor","ceva","chiar","ci","cinci",
					"cind","cine","cineva","cât","cita","cite","citeva","citi","citiva","conform","contra","cu","cui","cum",
					"cumva","curând","curînd","când","cât","câte","câtva","câţi","cînd","cît","cîte","cîtva","cîţi","că",
					"căci","cărei","căror","cărui","către","d","da","daca","dacă","dar","dat","datorită","dată","dau","de",
					"deasupra","deci","decât","degrabă","deja","deoarece","departe","deși","despre","din","dinaintea","dinainte"
					"dintr","dintr-o","dintre","doar","doi","doilea","două","drept","dupa","după","dă","e","ea","ei","el","ele",
					"era","eram","este","eu","exact","eşti","f","face","fara","fața","față","fel","fi","fie","fiecare","fii","fim",
					"fiu","fiţi","foarte","fost","frumos","fără","g","geaba","graţie","h","halbă","i","ia","iar","ieri","ii","îi"
					"il","îl","îmi","imi","in","inainte","inapoi","inca","incit","insa","intr","intre","iți","j","k","l","la","le",
					"li","lor","lui","lângă","lîngă","m","ma","mai","mare","mea","mei","mele","mereu","meu","mi","mie","mine",
					"mod","mult","multa","multe","multi","multă","mulţi","mulţumesc","mâine","mîine","mă","n","ne","nevoie","ni",
					"nici","niciodata","nicăieri","nimeni","nimeri","nimic","niste","nişte","noastre","noastră","noi","noroc",
					"noștri","nostru","nou","noua","nouă","noştri","nu","numai","nu-i","nu-l","niș","o","opt","or","ori","oricare","orice","oricine",
					"oricum","oricând","oricât","oricînd","oricît","oriunde","p","pai","parca","patra","patru","patrulea","pe",
					"pentru","peste","pic","până","plus","poate","pot","prea","prima","primul","prin","printr-o","printr-un","puțini","puţin",
					"puţina","puţină","până","pînă","r","rog","s","sa","sa-mi","sa-ti","sai","sale","sau","se","si","sint",
					"sintem","spate","spre","sub","sunt","suntem","sunteţi","sus","sută","sînt","sîntem","sînteţi","să","săi",
					"său","t","ta","tale","te","ti","timp","tine","toata","toate","toată","tocmai","tot","toti","totul","totusi",
					"totuşi","toţi","trei","treia","treilea","tu","tuturor","tăi","tău","u","ul","ului","un","una","unde",
					"undeva","unei","uneia","unele","uneori","unii","unor","unora","unu","unui","unuia","unul","v",
					"va","vi","voastre","voastră","voi","vom","vor","vostru","vouă","voştri","vreme","vreo","vreun","vă","x","z",
					"zece","zero","zi","zice","împotriva","în","înainte","înaintea","încotro","încât","încît",
					"între","întrucât","întrucît","îţi","înapoi","înca","ăla","ălea","ăsta","ăstea","ăştia","şapte","şase","şi","ştiu","ţi","ţie","s-a",
					"s-au","l-am","l-ai","își","într-o","într-un","dintr-un","și-a","șia","și","dintro"]


SYMBOLS = ['{','}','(',')','[',']','.',',',':',';','+','-','*','/','&','|','<','>','=','~','$',
			"'",'"','%','!','?','<','>','/','”','`','@','.','_']

rwn = rowordnet.RoWordNet()
lemm = spacy.load('ro_core_news_lg', disable=['parser', 'ner'])

##	Print list of stop words RO
def printListOfStopWordsRO():
	print(listOfStopWordsRO)


##	Print the numeber of items in the list od stop words RO
def printLenListOfStopWordsRO():
	print(len(listOfStopWordsRO))


##	Remove stop words from list /// return list
def removeStopWordsROSymbolsDigits(textList):
	for word in list(textList):
		if word.lower() in listOfStopWordsRO or word in SYMBOLS or word.isdigit():
			textList.remove(word)
	return textList

def removeSymbolsDigits(textList):
	result = []
	for symbol in list(textList):
		word = symbol
		for s in symbol:
			if s in SYMBOLS:
				word = symbol.replace(s, " ")
		result.append(word)
	return result

##	Return list of definition
def listOfSynsetDefinitionByWord(word):
	listOfSynsetsDefinition = []
	lemm1 = lemm(word.lower())

	for l in lemm1:
		word = l.lemma_
	synset_ids = rwn.synsets(literal = word)

	for synset_id in synset_ids:
		res = rwn.synset(synset_id)
		if word in res.literals:
			synsetDefinition = res.definition
			synsetDefinition = word_tokenize(synsetDefinition)
			synsetDefinition = removeStopWordsROSymbolsDigits(synsetDefinition)
			listOfSynsetsDefinition.append(synsetDefinition)
	return listOfSynsetsDefinition

def fullListOfSynsetDefinitionByWord(word):
	listOfSynsetsDefinition = []
	lemm1 = lemm(word.lower())

	for l in lemm1:
		word = l.lemma_

	synset_ids = rwn.synsets(literal = word)

	for synset_id in synset_ids:
		res = rwn.synset(synset_id)
		if word in res.literals:
			synsetDefinition = "" + str(res.pos) + "."
			synsetDefinition +=  " " + res.definition + " | "
			sinonime = removeSymbolsDigits(res.literals)

			synsetDefinition += "Sinonime: "
			for s in sinonime:
				synsetDefinition += " " + s + ";"
			
			listOfSynsetsDefinition.append(synsetDefinition)
	return listOfSynsetsDefinition

def clculateTheWeightForEverySentence(sentence, listOfSynsetsDefinition, word):
	resultListOfWeight = []
	countList = []

	for i in range(len(listOfSynsetsDefinition)):
		weight = 0.0
		count = 0
		
		for j in range(len(listOfSynsetsDefinition[i])):
			for k in range(len(sentence)):

				lemm1 = lemm(listOfSynsetsDefinition[i][j].lower())
				for l in lemm1:
					lemm1 = l.lemma_
				lemm2 = lemm(sentence[k].lower())
				for l in lemm2:
					lemm2 = l.lemma_
				lemm3 = lemm(word.lower())
				for l in lemm3:
					lemm3 = l.lemma_

				wordFromList1 = rwn.synsets(literal = lemm1)
				wordFromList2 = rwn.synsets(literal = lemm2)


				if lemm1 == lemm2 and lemm1 != lemm3:
					count += 1
					weight += 5.0

				if len(wordFromList1) > 0 and len(wordFromList2) > 0:			
					if rwn.lch_similarity(wordFromList2[0], wordFromList1[0]) != None:
						count += 1									
						weight += rwn.lch_similarity(wordFromList2[0], wordFromList1[0])
					
				print(lemm1 + "   " + lemm2 + "   " + str(weight))

		resultListOfWeight.append(weight)
		countList.append(count)

	return resultListOfWeight, countList


def checkMostBigestWeightOfSentence(resultListOfWeight, listOfSynsetsDefinition, countList):
	listOfWeightAferDivide = []

	for i in range(len(list(resultListOfWeight))):
		if resultListOfWeight[i] != 0:
			listOfWeightAferDivide.append(resultListOfWeight[i]/countList[i])
		else:
			listOfWeightAferDivide.append(0)
	print(listOfWeightAferDivide)
	if listOfWeightAferDivide != []:
		print(listOfWeightAferDivide.index(max(listOfWeightAferDivide)))
		return listOfWeightAferDivide.index(max(listOfWeightAferDivide))


def printTheContextualDefinition(indexOfMaxWeight, fullListOfSynsetDefinition):
	if len(fullListOfSynsetDefinition) == 1:
		print(fullListOfSynsetDefinition[indexOfMaxWeight])
		return fullListOfSynsetDefinition[indexOfMaxWeight]
	else:
		print(fullListOfSynsetDefinition[indexOfMaxWeight])
		return fullListOfSynsetDefinition[indexOfMaxWeight]


def DtSAlgorithm(word, sentence):
	listOfSynsetsDefinition = []
	fullListOfSynsetDefinition = []
	result = ''

	sentence = word_tokenize(sentence)
	sentence = removeStopWordsROSymbolsDigits(sentence)
	fullListOfSynsetDefinition = fullListOfSynsetDefinitionByWord(word)
	listOfSynsetsDefinition = listOfSynsetDefinitionByWord(word)

	
	resultListOfWeight, countList = clculateTheWeightForEverySentence(sentence, listOfSynsetsDefinition, word)
	indexOfMaxWeight = checkMostBigestWeightOfSentence(resultListOfWeight, listOfSynsetsDefinition, countList)

	result = printTheContextualDefinition(indexOfMaxWeight, fullListOfSynsetDefinition)

	return result
