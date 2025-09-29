from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def code_html():
    return '<html><body><h1>Bonjour</h1></body></html>'


if __name__ == '__main__':
    # Running the application in debug mode
    app.run(debug=True)