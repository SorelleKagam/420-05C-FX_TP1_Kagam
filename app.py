from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def accueil():
    return render_template ('accueil.jinja')


if __name__ == '__main__':
    # Running the application in debug mode
    app.run(debug=True)