from flask import Flask, render_template, request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from heapq import nlargest

app = Flask(__name__)

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')


def summarize_text(text, num_sentences=3):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize words and remove stopwords
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]

    # Calculate word frequencies
    freq = FreqDist(words)

    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = freq[word]
                else:
                    sentence_scores[sentence] += freq[word]

    # Get the top N sentences with highest scores
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    # Join the top sentences to create the summary
    summary = ' '.join(summary_sentences)

    return summary


@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    original_text = ""
    num_sentences = 3
    if request.method == 'POST':
        original_text = request.form['text']
        num_sentences = int(request.form['num_sentences'])
        summary = summarize_text(original_text, num_sentences)
    return render_template('index.html', summary=summary, original_text=original_text, num_sentences=num_sentences)


if __name__ == '__main__':
    app.run(debug=True)

