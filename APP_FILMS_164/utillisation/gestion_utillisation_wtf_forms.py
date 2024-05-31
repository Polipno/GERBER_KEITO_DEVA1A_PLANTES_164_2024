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
    nom_utillisation_wtf = StringField("Description", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_utillisation_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    submit = SubmitField("Enregistrer")


class FormWTFUpdateutillisation(FlaskForm):
    nom_utillisation_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_utillisation_update_wtf = StringField("Description", validators=[
        Length(min=2, max=20, message="min 2 max 20"),
        Regexp(nom_utillisation_update_regexp, message="Pas de chiffres, de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")
    ])
    submit = SubmitField("Update")



from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField



class FormWTFDeleteutillisation(FlaskForm):
    """
        Dans le formulaire "utillisation_delete_wtf.html"

        nom_utillisation_delete_wtf : Champ qui reçoit la valeur du utillisation, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "utillisation".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_utillisation".
    """
    nom_utillisation_delete_wtf = StringField("Effacer cette Utillisation", validators=[DataRequired()])
    submit_btn_del = SubmitField("Effacer Utillisation")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")





class FormWTFAjouterPlanteUtilisation(FlaskForm):
    id_plante_wtf = StringField("ID Plante", validators=[DataRequired()])
    id_utilisation_wtf = StringField("ID Utilisation", validators=[DataRequired()])
    submit = SubmitField("Ajouter")




class FormWTFUpdatePlanteUtilisation(FlaskForm):
    id_plante_update_wtf = StringField("ID de la plante", validators=[DataRequired()])
    id_utilisation_update_wtf = StringField("ID de l'utilisation", validators=[DataRequired()])
    submit = SubmitField("Mettre à jour")






class FormWTFDeletePlanteUtilisation(FlaskForm):
    nom_plante_utilisation_delete_wtf = StringField("Effacer cette association", render_kw={'readonly': True})
    submit_btn_del = SubmitField("Effacer association")
    submit_btn_conf_del = SubmitField("Effacer association")
    submit_btn_annuler = SubmitField("Annuler")
