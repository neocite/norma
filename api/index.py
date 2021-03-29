from flask import Flask, jsonify
from models import category

app = Flask(__name__)


@app.route('/categorize/<text>')
def categorize(text):
    classification = category.classify(text)
    return jsonify(classification)


if __name__ == '__main__':
    app.run()
