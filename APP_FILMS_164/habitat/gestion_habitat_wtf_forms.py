"""
    Fichier : gestion_habitat_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterhabitat(FlaskForm):
    """
        Dans le formulaire "habitat_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_habitat_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_habitat_wtf = StringField("Clavioter le habitat ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_habitat_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    submit = SubmitField("Enregistrer habitat")

class FormWTFUpdatehabitat(FlaskForm):
    nom_habitat_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_habitat_update_wtf = StringField("Clavioter le habitat ", validators=[
        Length(min=2, max=20, message="min 2 max 20"),
        Regexp(nom_habitat_update_regexp, message="Pas de chiffres, de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")
    ])
    submit = SubmitField("Update habitat")


class FormWTFDeletehabitat(FlaskForm):
    """
        Dans le formulaire "habitat_delete_wtf.html"

        nom_habitat_delete_wtf : Champ qui reçoit la valeur du habitat, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "habitat".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_habitat".
    """
    nom_habitat_delete_wtf = StringField("Effacer ce habitat")
    submit_btn_del = SubmitField("Effacer habitat")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
