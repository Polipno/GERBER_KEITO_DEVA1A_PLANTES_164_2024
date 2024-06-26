"""
    Fichier : gestion_exigences_de_croissance_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp





class FormWTFAjouterexigences_de_croissance(FlaskForm):
    """
        Dans le formulaire "exigences_de_croissance_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    lumiere_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    lumiere_wtf = StringField("lumière ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(lumiere_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])

    eau_wtf = StringField("Eau", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(lumiere_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                 ])
    type_de_sol_wtf = StringField("Type de sol", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(lumiere_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                 ])
    submit = SubmitField("Enregistrer")


class FormWTFUpdateexigences_de_croissance(FlaskForm):
    """
        Dans le formulaire "exigences_de_croissance_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_exigences_de_croissance_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_exigences_de_croissance_update_wtf = StringField("lumière", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(nom_exigences_de_croissance_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    eau_wtf = StringField("Eau", validators=[DataRequired()])

    type_de_sol_wtf = StringField("Type de sol", validators=[DataRequired()])
    submit = SubmitField("Update")


class FormWTFDeleteexigences_de_croissance(FlaskForm):
    """
        Dans le formulaire "exigences_de_croissance_delete_wtf.html"

        nom_exigences_de_croissance_delete_wtf : Champ qui reçoit la valeur du exigences_de_croissance, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "exigences_de_croissance".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_exigences_de_croissance".
    """
    nom_exigences_de_croissance_delete_wtf = StringField("Effacer cette Exigences de croissance")
    submit_btn_del = SubmitField("Effacer Exigences de croissance")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")




class FormWTFAjouterLiaisonPlanteExigence(FlaskForm):
    id_plante_wtf = StringField("ID Plannte", validators=[DataRequired(message="Le champ ID Plante est requis")])
    id_exigence_de_croissance_wtf = StringField("ID Exigence de Croissance", validators=[DataRequired(message="Le champ ID Exigence de Croissance est requis")])
    submit = SubmitField("Ajouter")



class FormWTFUpdateLiaisonPlanteExigence(FlaskForm):
    fk_plantes_wtf = StringField("ID Plante", validators=[DataRequired()])
    fk_exigences_de_croissance_wtf = StringField("ID Exigence de Croissance", validators=[DataRequired()])
    submit = SubmitField("Mettre à jour")






class FormWTFDeleteLiaisonPlanteExigence(FlaskForm):
    id_liaison_wtf = StringField("ID Liaison", validators=[DataRequired()])
    submit_btn_del = SubmitField("Effacer Liaison")
    submit_btn_annuler = SubmitField("Annuler")