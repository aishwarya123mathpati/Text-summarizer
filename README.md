# Text Summarizer App

This is a simple web application that provides text summarization functionality. It allows users to input a large body of text and receive a concise summary, making it easier to quickly grasp the main points of the content.

## Features

- User-friendly web interface
- Customizable summary length (number of sentences)
- Extractive summarization using NLTK
- Responsive design for various screen sizes

## Installation

1. Clone this repository:
   \`\`\`
   git clone https://github.com/yourusername/text-summarizer-app.git
   cd text-summarizer-app
   \`\`\`

2. Install the required packages:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`

## Usage

1. Run the Flask application:
   \`\`\`
   python app.py
   \`\`\`

2. Open a web browser and navigate to \`http://127.0.0.1:5000/\`

3. Enter your text in the provided text area, specify the desired number of sentences for the summary, and click "Summarize"

4. The summary will appear below the input form

## How it works

The application uses the Natural Language Toolkit (NLTK) to perform extractive summarization. Here's a brief overview of the process:

1. The input text is tokenized into sentences and words
2. Stop words are removed to focus on meaningful content
3. Word frequencies are calculated
4. Sentences are scored based on the frequency of their words
5. The top N sentences with the highest scores are selected to form the summary

## Project Structure

- \`app.py\`: Main Flask application file
- \`templates/index.html\`: HTML template for the web interface
- \`requirements.txt\`: List of Python package dependencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

