from flask import Flask, render_template, request
from DtSAlgotithm import *
import io
from pdfminer.high_level import extract_text

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
	word = ''
	sentence = ''
	result = []
	text = ''


	if request.method == 'POST':

		if request.form['func'] == '2':
			if request.form['word'] != '' and request.form['sentence'] != '':
				word = request.form['word']
				sentence = request.form['sentence']
				result.append(DtSAlgorithm(word, sentence))
				print(result)
				text = request.form['text']

				return render_template('index.html', word = word, sentence = sentence, result = result, text = text)

			elif request.form['word'] != '' and request.form['sentence'] == '':
				word = request.form['word']
				sentence = request.form['sentence']
				result = fullListOfSynsetDefinitionByWord(word)
				result = list(set(result))
				text = request.form['text']

				return render_template('index.html', word = word, sentence = sentence, result = result, text = text)
			else:
				result.append("Introdu cuvântul și propoziția")
				text = request.form['text']
				return render_template('index.html', word = word, sentence = sentence, result = result, text = text)

		elif request.form['func'] == '1':
			f = request.files['file']

			try:
				text = extract_text("file/" + f.filename)
			except:
				text = "Wrong format"
		
			return render_template('index.html', word = word, sentence = sentence, result = result, text = text)

		else:
			result.append("Introdu cuvântul și propoziția")

			return render_template('index.html', word = word, sentence = sentence, result = result, text = text)
		return render_template('index.html', word = word, sentence = sentence, result = result, text = text)
	else:
		return render_template('index.html', word = word, sentence = sentence, result = result)






if __name__ == "__main__":
	app.run(debug=True)
	