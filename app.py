from flask import Flask, render_template, request,make_response, redirect
app = Flask(__name__)
def get_locale():
    """ retourne la valeur du cookie s'il est enregistré """
    return request.cookies.get('langue', 'fr')
@app.route('/')
def index():
    """Récupère les paramètres régionaux pour afficher la page d'accueil"""
    # Récupérer le cookie langue
    langue = request.cookies.get('langue', 'fr')   
    return render_template('Accueil.jinja')
@app.route('/choisir_langue')
def choisir_langue():
    """ Modifie les paramètres régionaux """
    langue = request.args.get("langue", default="fr")
    response = make_response(redirect('/'))
    response.set_cookie('langue', langue)
    return response

if __name__ == '__main__':
    app.run(debug=True)