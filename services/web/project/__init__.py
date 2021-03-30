from flask import Flask, request
from models import category

app = Flask(__name__, instance_relative_config=True)


@app.route('/categorizer')
def categorizer():

    text = request.args.get('text')
    print(text)

    if text:
        categorization = category.classify(text)
        return categorization
