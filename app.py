import random
from flask import Flask, render_template, request,make_response, redirect


import mysql.connector

import bd
app = Flask(__name__)

def lister_routes():
    """Liste les routes pour le menu"""
    return [
        {
            'route' : '/',
            'nom' : 'Accueil'
        },
        {
            'route' : '/ajout',
            'nom' : 'ajout'
        },
        {
            'route' : '/services',
            'nom' : 'services'
        },
        {
            'route' : '/service',
            'nom' : 'service'
        },
        {
            'route' : '/edit-service',
            'nom' : 'À propos'
        },
        {
            'route' : '/confirmation',
            'nom' : 'confirmation'
        }
    ]
def get_locale():
    """ retourne la valeur du cookie s'il est enregistré """
    return request.cookies.get('langue', 'fr')
@app.route('/')
def index():
    """Récupère les paramètres régionaux pour afficher la page d'accueil"""
    # Récupérer le cookie langue
    langue = request.cookies.get('langue', 'fr')   
    return render_template('base.jinja')
@app.route('/choisir_langue')
def choisir_langue():
    """ Modifie les paramètres régionaux """
    langue = request.args.get("langue", default="fr")
    response = make_response(redirect('/'))
    response.set_cookie('langue', langue)
    return response

@app.route('/ajout')
def ajout():
    """Affichage d'une liste"""

    return render_template(
        'ajout.jinja', titre_onglet="Ajout_service",
        routes=lister_routes()
    )
    

    @app.route('/services')
def services():
    """Affichage d'une liste"""
    les_services = 
    return render_template(
        'services.jinja',
        titre='Une liste!',
        liste=les_services,
        titre_onglet="services",
        routes=lister_routes()
    )

@app.route('/sercice')
def detail():
    """Affichage d'une liste"""
    return render_template(
        'service.jinja',
        titre_onglet="service",
        routes=lister_routes()
    )

@app.route('/confirmation')
def confirmation():
    """Affichage d'une liste"""
    return render_template(
        'confirmation.jinja',
        titre_onglet="confirmation",
        routes=lister_routes()
    )
@app.route('/edit_service')
def edit():
    """Affichage d'une liste"""
    return render_template(
        'edit_service.jinja',
        titre_onglet="modification",
        routes=lister_routes()
    )

if __name__ == '__main__':
    app.run(debug=True)