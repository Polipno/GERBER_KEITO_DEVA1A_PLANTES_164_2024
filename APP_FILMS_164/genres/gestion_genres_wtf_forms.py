from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, Regexp

class FormWTFAjouterGenres(FlaskForm):
    nom_genre_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_genre_wtf = StringField("Clavioter le genre", validators=[
        Length(min=2, max=20, message="min 2 max 20"),
        Regexp(nom_genre_regexp, message="Pas de chiffres, de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")
    ])
    nom_scientifique_wtf = StringField("Nom Scientifique", validators=[DataRequired()])
    famille_wtf = StringField("Famille", validators=[DataRequired()])
    submit = SubmitField("Enregistrer genre")

class FormWTFUpdateGenre(FlaskForm):
    nom_genre_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_genre_update_wtf = StringField("Clavioter le Nom commun ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(nom_genre_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    nom_scientifique_wtf = StringField("Nom Scientifique", validators=[DataRequired()])
    famille_wtf = StringField("Famille", validators=[DataRequired()])
    submit = SubmitField("Update genre")

class FormWTFDeleteGenre(FlaskForm):
    nom_genre_delete_wtf = StringField("Effacer ce genre", validators=[DataRequired()])
    submit_btn_del = SubmitField("Effacer genre")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
