"""
    Fichier : gestion_utillisation_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterutillisation(FlaskForm):
    """
        Dans le formulaire "utillisation_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_utillisation_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_utillisation_wtf = StringField("Clavioter la description", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_utillisation_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    submit = SubmitField("Enregistrer utillisation")


class FormWTFUpdateutillisation(FlaskForm):
    """
        Dans le formulaire "utillisation_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_utillisation_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_utillisation_update_wtf = StringField("Clavioter le utillisation ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(nom_utillisation_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    date_utillisation_wtf_essai = DateField("Essai date", validators=[InputRequired("Date obligatoire"),
                                                               DataRequired("Date non valide")])
    submit = SubmitField("Update utillisation")


class FormWTFDeleteutillisation(FlaskForm):
    """
        Dans le formulaire "utillisation_delete_wtf.html"

        nom_utillisation_delete_wtf : Champ qui reçoit la valeur du utillisation, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "utillisation".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_utillisation".
    """
    nom_utillisation_delete_wtf = StringField("Effacer ce utillisation")
    submit_btn_del = SubmitField("Effacer utillisation")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
