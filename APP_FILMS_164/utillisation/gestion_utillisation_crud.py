"""Gestion des "routes" FLASK et des données pour les utillisation.
Fichier : gestion_utillisation_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.utillisation.gestion_utillisation_wtf_forms import FormWTFAjouterutillisation, \
    FormWTFDeletePlanteUtilisation, FormWTFUpdatePlanteUtilisation, FormWTFAjouterPlanteUtilisation, \
    FormWTFDeleteutillisation

from APP_FILMS_164.utillisation.gestion_utillisation_wtf_forms import FormWTFUpdateutillisation

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /utillisation_afficher
    
    Test : ex : http://127.0.0.1:5575/utillisation_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                ID_Utillisation_sel = 0 >> tous les utillisation.
                ID_Utillisation_sel = "n" affiche le utillisation dont l'id est "n"
"""


@app.route("/utillisation_afficher/<string:order_by>/<int:ID_Utillisation_sel>", methods=['GET', 'POST'])
def utillisation_afficher(order_by, ID_Utillisation_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and ID_Utillisation_sel == 0:
                    strsql_utillisation_afficher = """SELECT * FROM t_utillisation"""
                    mc_afficher.execute(strsql_utillisation_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_utillisation"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du utillisation sélectionné avec un nom de variable
                    valeur_ID_Utillisation_selected_dictionnaire = {"value_ID_Utillisation_selected": ID_Utillisation_sel}
                    strsql_utillisation_afficher = """SELECT * FROM t_utillisation"""

                    mc_afficher.execute(strsql_utillisation_afficher, valeur_ID_Utillisation_selected_dictionnaire)
                else:
                    strsql_utillisation_afficher = """SELECT * FROM t_utillisation"""

                    mc_afficher.execute(strsql_utillisation_afficher)

                data_utillisation = mc_afficher.fetchall()

                print("data_utillisation ", data_utillisation, " Type : ", type(data_utillisation))

                # Différencier les messages si la table est vide.
                if not data_utillisation and ID_Utillisation_sel == 0:
                    flash("""La table "t_utillisation" est vide. !!""", "warning")
                elif not data_utillisation and ID_Utillisation_sel > 0:
                    # Si l'utilisateur change l'ID_Utillisation dans l'URL et que le utillisation n'existe pas,
                    flash(f"Le utillisation demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_utillisation" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données utillisation affichés !!", "success")

        except Exception as Exception_utillisation_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{utillisation_afficher.__name__} ; "
                                          f"{Exception_utillisation_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("utillisation/utillisation_afficher.html", data=data_utillisation)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /utillisation_ajouter
    
    Test : ex : http://127.0.0.1:5575/utillisation_ajouter
    
    Paramètres : sans
    
    But : Ajouter un utillisation pour un film
    
    Remarque :  Dans le champ "name_utillisation_html" du formulaire "utillisation/utillisation_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/utillisation_ajouter", methods=['GET', 'POST'])
def utillisation_ajouter_wtf():
    form = FormWTFAjouterutillisation()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_utillisation_wtf = form.nom_utillisation_wtf.data
                name_utillisation = name_utillisation_wtf.lower()
                valeurs_insertion_dictionnaire = {"Description_Utilisation": name_utillisation}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_utillisation = """INSERT INTO t_utillisation (ID_Utillisation, Description_Utilisation) VALUES (NULL,%(Description_Utilisation)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_utillisation, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('utillisation_afficher', order_by='ASC', ID_Utillisation_sel=0))

        except Exception as Exception_utillisation_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{utillisation_ajouter_wtf.__name__} ; "
                                            f"{Exception_utillisation_ajouter_wtf}")

    return render_template("utillisation/utillisation_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /utillisation_update
    
    Test : ex cliquer sur le menu "utillisation" puis cliquer sur le bouton "EDIT" d'un "utillisation"
    
    Paramètres : sans
    
    But : Editer(update) un utillisation qui a été sélectionné dans le formulaire "utillisation_afficher.html"
    
    Remarque :  Dans le champ "nom_utillisation_update_wtf" du formulaire "utillisation/utillisation_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""

@app.route("/utillisation_update", methods=['GET', 'POST'])
def utillisation_update_wtf():
    ID_Utillisation_update = request.values['ID_Utillisation_btn_edit_html']

    form_update = FormWTFUpdateutillisation()
    try:
        if request.method == "POST" and form_update.submit.data:
            name_utillisation_update = form_update.nom_utillisation_update_wtf.data.lower()

            valeur_update_dictionnaire = {
                "ID_Utillisation": ID_Utillisation_update,
                "Description_Utilisation": name_utillisation_update
            }

            str_sql_update_intituleutillisation = """
                UPDATE t_utillisation 
                SET Description_Utilisation = %(Description_Utilisation)s 
                WHERE ID_Utillisation = %(ID_Utillisation)s
            """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_intituleutillisation, valeur_update_dictionnaire)

            flash("Donnée mise à jour !!", "success")

            return redirect(url_for('utillisation_afficher', order_by="ASC", ID_Utillisation_sel=ID_Utillisation_update))
        elif request.method == "GET":
            str_sql_ID_Utillisation = """
                SELECT ID_Utillisation, Description_Utilisation 
                FROM t_utillisation 
                WHERE ID_Utillisation = %(ID_Utillisation)s
            """
            valeur_select_dictionnaire = {"ID_Utillisation": ID_Utillisation_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_ID_Utillisation, valeur_select_dictionnaire)
                data_nom_utillisation = mybd_conn.fetchone()

            form_update.nom_utillisation_update_wtf.data = data_nom_utillisation["Description_Utilisation"]

    except Exception as Exception_utillisation_update_wtf:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{utillisation_update_wtf.__name__} ; "
                                      f"{Exception_utillisation_update_wtf}")

    return render_template("utillisation/utillisation_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /utillisation_delete
    
    Test : ex. cliquer sur le menu "utillisation" puis cliquer sur le bouton "DELETE" d'un "utillisation"
    
    Paramètres : sans
    
    But : Effacer(delete) un utillisation qui a été sélectionné dans le formulaire "utillisation_afficher.html"
    
    Remarque :  Dans le champ "nom_utillisation_delete_wtf" du formulaire "utillisation/utillisation_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/utillisation_delete", methods=['GET', 'POST'])
def utillisation_delete_wtf():
    data_films_attribue_utillisation_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "ID_Utillisation"
    ID_Utillisation_delete = request.values['ID_Utillisation_btn_delete_html']

    # Objet formulaire pour effacer le utillisation sélectionné.
    form_delete = FormWTFDeleteutillisation()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("utillisation_afficher", order_by="ASC", ID_Utillisation_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "utillisation/utillisation_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_films_attribue_utillisation_delete = session['data_films_attribue_utillisation_delete']
                print("data_films_attribue_utillisation_delete ", data_films_attribue_utillisation_delete)

                flash(f"Effacer le utillisation de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer utillisation" qui va irrémédiablement EFFACER le utillisation
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_ID_Utillisation": ID_Utillisation_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_films_utillisation = """DELETE FROM t_plantes_utilisation WHERE FK_Utilisation_Plantes = %(value_ID_Utillisation)s"""
                str_sql_delete_idutillisation = """DELETE FROM t_utillisation WHERE ID_Utillisation = %(value_ID_Utillisation)s"""
                # Manière brutale d'effacer d'abord la "fk_utillisation", même si elle n'existe pas dans la "t_utillisation_film"
                # Ensuite on peut effacer le utillisation vu qu'il n'est plus "lié" (INNODB) dans la "t_utillisation_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_films_utillisation, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idutillisation, valeur_delete_dictionnaire)

                flash(f"utillisation définitivement effacé !!", "success")
                print(f"utillisation définitivement effacé !!")

                # afficher les données
                return redirect(url_for('utillisation_afficher', order_by="ASC", ID_Utillisation_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_ID_Utillisation": ID_Utillisation_delete}
            print(ID_Utillisation_delete, type(ID_Utillisation_delete))

            # Requête qui affiche tous les films_utillisation qui ont le utillisation que l'utilisateur veut effacer
            str_sql_utillisation_films_delete = """SELECT ID_Plantes_Utilisation, Nom_Commun, ID_Utillisation, Description_Utilisation FROM t_plantes_utilisation 
                                            INNER JOIN t_plantes ON t_plantes_utilisation.FK_Plantes_Utilisation = t_plantes.id_plante
                                            INNER JOIN t_utillisation ON t_plantes_utilisation.FK_Utilisation_Plantes = t_utillisation.ID_Utillisation
                                            WHERE FK_Utilisation_Plantes = %(value_ID_Utillisation)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_utillisation_films_delete, valeur_select_dictionnaire)
                data_films_attribue_utillisation_delete = mydb_conn.fetchall()
                print("data_films_attribue_utillisation_delete...", data_films_attribue_utillisation_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "utillisation/utillisation_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_films_attribue_utillisation_delete'] = data_films_attribue_utillisation_delete

                # Opération sur la BD pour récupérer "ID_Utillisation" et "intitule_utillisation" de la "t_utillisation"
                str_sql_ID_Utillisation = "SELECT ID_Utillisation, Description_Utilisation FROM t_utillisation WHERE ID_Utillisation = %(value_ID_Utillisation)s"

                mydb_conn.execute(str_sql_ID_Utillisation, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom utillisation" pour l'action DELETE
                data_nom_utillisation = mydb_conn.fetchone()
                print("data_nom_utillisation ", data_nom_utillisation, " type ", type(data_nom_utillisation), " utillisation ",
                      data_nom_utillisation["Description_Utilisation"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "utillisation_delete_wtf.html"
            form_delete.nom_utillisation_delete_wtf.data = data_nom_utillisation["Description_Utilisation"]
            # Le bouton pour l'action "DELETE" dans le form. "utillisation_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_utillisation_delete_wtf:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{utillisation_delete_wtf.__name__} ; "
                                      f"{Exception_utillisation_delete_wtf}")

    return render_template("utillisation/utillisation_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_utillisation_delete)


@app.route("/plantes_utillisation_afficher/<string:order_by>/<int:ID_Plante_Utillisation_sel>", methods=['GET', 'POST'])
def plantes_utillisation_afficher(order_by, ID_Plante_Utillisation_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and ID_Plante_Utillisation_sel == 0:
                    strsql_plantes_utillisation_afficher = """
                        SELECT p.ID_Plante, p.Nom_Commun, p.Nom_Scientifique, p.Famille, 
                               u.ID_Utillisation, u.Description_Utilisation, pu.ID_Plantes_Utilisation
                        FROM t_plantes p
                        JOIN t_plantes_utilisation pu ON p.ID_Plante = pu.FK_Plantes_Utilisation
                        JOIN t_utillisation u ON pu.FK_Utilisation_Plantes = u.ID_Utillisation
                        ORDER BY pu.ID_Plantes_Utilisation ASC
                    """
                    mc_afficher.execute(strsql_plantes_utillisation_afficher)
                elif order_by == "ASC":
                    valeur_ID_Utillisation_selected_dictionnaire = {"value_ID_Utillisation_selected": ID_Plante_Utillisation_sel}
                    strsql_plantes_utillisation_afficher = """
                        SELECT p.ID_Plante, p.Nom_Commun, p.Nom_Scientifique, p.Famille, 
                               u.ID_Utillisation, u.Description_Utilisation, pu.ID_Plantes_Utilisation
                        FROM t_plantes p
                        JOIN t_plantes_utilisation pu ON p.ID_Plante = pu.FK_Plantes_Utilisation
                        JOIN t_utillisation u ON pu.FK_Utilisation_Plantes = u.ID_Utillisation
                        WHERE pu.ID_Plantes_Utilisation = %(value_ID_Utillisation_selected)s
                        ORDER BY pu.ID_Plantes_Utilisation ASC
                    """
                    mc_afficher.execute(strsql_plantes_utillisation_afficher, valeur_ID_Utillisation_selected_dictionnaire)
                else:
                    strsql_plantes_utillisation_afficher = """
                        SELECT p.ID_Plante, p.Nom_Commun, p.Nom_Scientifique, p.Famille, 
                               u.ID_Utillisation, u.Description_Utilisation, pu.ID_Plantes_Utilisation
                        FROM t_plantes p
                        JOIN t_plantes_utilisation pu ON p.ID_Plante = pu.FK_Plantes_Utilisation
                        JOIN t_utillisation u ON pu.FK_Utilisation_Plantes = u.ID_Utillisation
                        ORDER BY pu.ID_Plantes_Utilisation ASC
                    """
                    mc_afficher.execute(strsql_plantes_utillisation_afficher)

                data_utillisation = mc_afficher.fetchall()

                if not data_utillisation and ID_Plante_Utillisation_sel == 0:
                    flash("""La table "t_utillisation" est vide. !!""", "warning")
                elif not data_utillisation and ID_Plante_Utillisation_sel > 0:
                    flash(f"Le utillisation demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données utillisation affichées !!", "success")

        except Exception as Exception_utillisation_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{utillisation_afficher.__name__} ; "
                                          f"{Exception_utillisation_afficher}")

    return render_template("utillisation/plantes_utillisation_afficher.html", data=data_utillisation)

class ExceptionPlanteUtilisationAjouter(Exception):
    pass


@app.route("/plantes_utillisation_ajouter", methods=['GET', 'POST'])
def plantes_utillisation_ajouter_wtf():
    form = FormWTFAjouterPlanteUtilisation()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                id_plante = form.id_plante_wtf.data
                id_utillisation = form.id_utilisation_wtf.data
                valeurs_insertion_dictionnaire = {
                    "FK_Plantes_Utilisation": id_plante,
                    "FK_Utilisation_Plantes": id_utillisation
                }
                strsql_insert_association = """INSERT INTO t_plantes_utilisation 
                                                (FK_Plantes_Utilisation, FK_Utilisation_Plantes) 
                                                VALUES (%(FK_Plantes_Utilisation)s, %(FK_Utilisation_Plantes)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_association, valeurs_insertion_dictionnaire)

                flash(f"Association ajoutée avec succès !!", "success")
                return redirect(url_for('plantes_utillisation_afficher', order_by='ASC', ID_Plante_Utillisation_sel=0))

        except Exception as Exception_ajouter_association:
            raise ExceptionPlanteUtilisationAjouter(f"fichier : {Path(__file__).name}  ;  "
                                                    f"{plantes_utillisation_ajouter_wtf.__name__} ; "
                                                    f"{str(Exception_ajouter_association)}")

    return render_template("utillisation/plantes_utilisation_ajouter_wtf.html", form=form)

class ExceptionPlanteUtilisationModifier(Exception):
    pass


@app.route("/plantes_utillisation_modifier", methods=['GET', 'POST'])
def plantes_utillisation_modifier_wtf():
    try:
        id_plante_utilisation_update = request.args.get('ID_Plantes_Utilisation_btn_edit_html', None)
        if id_plante_utilisation_update is None:
            raise KeyError("ID_Plantes_Utilisation_btn_edit_html")

        form_update = FormWTFUpdatePlanteUtilisation()

        if request.method == "POST" and form_update.validate_on_submit():
            id_plante = form_update.id_plante_update_wtf.data
            id_utilisation = form_update.id_utilisation_update_wtf.data
            valeur_update_dictionnaire = {
                "ID_Plantes_Utilisation": id_plante_utilisation_update,
                "FK_Plantes_Utilisation": id_plante,
                "FK_Utilisation_Plantes": id_utilisation
            }
            str_sql_update_association = """
                UPDATE t_plantes_utilisation 
                SET FK_Plantes_Utilisation = %(FK_Plantes_Utilisation)s, 
                    FK_Utilisation_Plantes = %(FK_Utilisation_Plantes)s 
                WHERE ID_Plantes_Utilisation = %(ID_Plantes_Utilisation)s
            """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_association, valeur_update_dictionnaire)

            flash("Association mise à jour avec succès !!", "success")
            return redirect(url_for('plantes_utillisation_afficher', order_by="ASC", ID_Plante_Utillisation_sel=id_plante_utilisation_update))

        elif request.method == "GET":
            str_sql_id_association = """
                SELECT * FROM t_plantes_utilisation 
                WHERE ID_Plantes_Utilisation = %(ID_Plantes_Utilisation)s
            """
            valeur_select_dictionnaire = {"ID_Plantes_Utilisation": id_plante_utilisation_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_association, valeur_select_dictionnaire)
                data_association = mybd_conn.fetchone()
                if data_association:
                    form_update.id_plante_update_wtf.data = data_association["FK_Plantes_Utilisation"]
                    form_update.id_utilisation_update_wtf.data = data_association["FK_Utilisation_Plantes"]
                else:
                    flash("Liaison non trouvée.", "danger")
                    return redirect(url_for('plantes_utillisation_afficher', order_by="ASC", ID_Plante_Utillisation_sel=0))

    except KeyError as e:
        flash(f"Erreur : {str(e)}. Clé non trouvée dans la requête.", "danger")
        return redirect(url_for('plantes_utillisation_afficher', order_by="ASC", ID_Plante_Utillisation_sel=0))
    except Exception as e:
        raise ExceptionPlanteUtilisationModifier(f"fichier : {Path(__file__).name}  ;  "
                                                 f"{plantes_utillisation_modifier_wtf.__name__} ; "
                                                 f"{str(e)}")

    return render_template("utillisation/plantes_utilisation_modifier_wtf.html", form_update=form_update)

class ExceptionPlanteUtilisationSupprimer(Exception):
    pass


@app.route("/plantes_utillisation_supprimer", methods=['GET', 'POST'])
def plantes_utillisation_supprimer_wtf():
    id_plante_utilisation_delete = request.values.get('ID_Plantes_Utilisation_btn_delete_html')
    form_delete = FormWTFDeletePlanteUtilisation()
    try:
        if request.method == "POST":
            if form_delete.submit_btn_annuler.data:
                return redirect(url_for('plantes_utillisation_afficher', order_by='ASC', ID_Plante_Utillisation_sel=0))

            if form_delete.submit_btn_conf_del.data:
                valeur_delete_dictionnaire = {"value_ID_Plantes_Utilisation": id_plante_utilisation_delete}
                str_sql_delete_association = """DELETE FROM t_plantes_utilisation 
                                                WHERE ID_Plantes_Utilisation = %(value_ID_Plantes_Utilisation)s"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_association, valeur_delete_dictionnaire)

                flash(f"Association supprimée avec succès !!", "success")
                return redirect(url_for('plantes_utillisation_afficher', order_by="ASC", ID_Plante_Utillisation_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_ID_Plantes_Utilisation": id_plante_utilisation_delete}
            str_sql_select_association = """SELECT * FROM t_plantes_utilisation 
                                            WHERE ID_Plantes_Utilisation = %(value_ID_Plantes_Utilisation)s"""
            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_select_association, valeur_select_dictionnaire)
                data_association = mydb_conn.fetchone()
                form_delete.nom_plante_utilisation_delete_wtf.data = f"{data_association['FK_Plantes_Utilisation']} - {data_association['FK_Utilisation_Plantes']}"

    except Exception as e:
        raise ExceptionPlanteUtilisationSupprimer(f"fichier : {Path(__file__).name}  ;  "
                                                  f"{plantes_utillisation_supprimer_wtf.__name__} ; "
                                                  f"{str(e)}")

    return render_template("utillisation/plantes_utilisation_supprimer_wtf.html",
                           form_delete=form_delete)
