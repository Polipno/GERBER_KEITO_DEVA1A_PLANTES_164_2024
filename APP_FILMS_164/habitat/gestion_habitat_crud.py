"""Gestion des "routes" FLASK et des données pour les habitat.
Fichier : gestion_habitat_crud.py
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
from APP_FILMS_164.habitat.gestion_habitat_wtf_forms import FormWTFAjouterhabitat
from APP_FILMS_164.habitat.gestion_habitat_wtf_forms import FormWTFDeletehabitat
from APP_FILMS_164.habitat.gestion_habitat_wtf_forms import FormWTFUpdatehabitat

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /habitat_afficher
    
    Test : ex : http://127.0.0.1:5575/habitat_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_habitat_sel = 0 >> tous les habitat.
                id_habitat_sel = "n" affiche le habitat dont l'id est "n"
"""


@app.route("/habitat_afficher/<string:order_by>/<int:id_habitat_sel>", methods=['GET', 'POST'])
def habitat_afficher(order_by, id_habitat_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_habitat_sel == 0:
                    strsql_habitat_afficher = """SELECT * FROM t_habitat"""
                    mc_afficher.execute(strsql_habitat_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_habitat"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du habitat sélectionné avec un nom de variable
                    valeur_id_habitat_selected_dictionnaire = {"value_id_habitat_selected": id_habitat_sel}
                    strsql_habitat_afficher = """SELECT * FROM t_habitat"""

                    mc_afficher.execute(strsql_habitat_afficher, valeur_id_habitat_selected_dictionnaire)
                else:
                    strsql_habitat_afficher = """SELECT * FROM t_habitat"""

                    mc_afficher.execute(strsql_habitat_afficher)

                data_habitat = mc_afficher.fetchall()

                print("data_habitat ", data_habitat, " Type : ", type(data_habitat))

                # Différencier les messages si la table est vide.
                if not data_habitat and id_habitat_sel == 0:
                    flash("""La table "t_habitat" est vide. !!""", "warning")
                elif not data_habitat and id_habitat_sel > 0:
                    # Si l'utilisateur change l'id_habitat dans l'URL et que le habitat n'existe pas,
                    flash(f"Le habitat demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_habitat" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données habitat affichés !!", "success")

        except Exception as Exception_habitat_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{habitat_afficher.__name__} ; "
                                          f"{Exception_habitat_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("habitat/habitat_afficher.html", data=data_habitat)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /habitat_ajouter
    
    Test : ex : http://127.0.0.1:5575/habitat_ajouter
    
    Paramètres : sans
    
    But : Ajouter un habitat pour un film
    
    Remarque :  Dans le champ "name_habitat_html" du formulaire "habitat/habitat_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/habitat_ajouter", methods=['GET', 'POST'])
def habitat_ajouter_wtf():
    form = FormWTFAjouterhabitat()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_habitat_wtf = form.nom_habitat_wtf.data
                name_habitat = name_habitat_wtf.lower()
                valeurs_insertion_dictionnaire = {"value_intitule_habitat": name_habitat}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_habitat = """INSERT INTO t_habitat (ID_habitat, Nom_Commun, Nom_Scientifique, Famille) VALUES (NULL,%(value_intitule_habitat)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_habitat, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('habitat_afficher', order_by='DESC', id_habitat_sel=0))

        except Exception as Exception_habitat_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{habitat_ajouter_wtf.__name__} ; "
                                            f"{Exception_habitat_ajouter_wtf}")

    return render_template("habitat/habitat_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /habitat_update
    
    Test : ex cliquer sur le menu "habitat" puis cliquer sur le bouton "EDIT" d'un "habitat"
    
    Paramètres : sans
    
    But : Editer(update) un habitat qui a été sélectionné dans le formulaire "habitat_afficher.html"
    
    Remarque :  Dans le champ "nom_habitat_update_wtf" du formulaire "habitat/habitat_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/habitat_update", methods=['GET', 'POST'])
def habitat_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_habitat"
    id_habitat_update = request.values['id_habitat_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdatehabitat()
    try:
        # 2023.05.14 OM S'il y a des listes déroulantes dans le formulaire
        # La validation pose quelques problèmes
        if request.method == "POST" and form_update.submit.data:
            # Récupèrer la valeur du champ depuis "habitat_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            name_habitat_update = form_update.nom_habitat_update_wtf.data
            name_habitat_update = name_habitat_update.lower()
            date_habitat_essai = form_update.date_habitat_wtf_essai.data

            valeur_update_dictionnaire = {"value_id_habitat": id_habitat_update,
                                          "value_name_habitat": name_habitat_update,
                                          "value_date_habitat_essai": date_habitat_essai
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_intitulehabitat = """UPDATE t_habitat SET intitule_habitat = %(value_name_habitat)s, 
            date_ins_habitat = %(value_date_habitat_essai)s WHERE id_habitat = %(value_id_habitat)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_intitulehabitat, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_habitat_update"
            return redirect(url_for('habitat_afficher', order_by="ASC", id_habitat_sel=id_habitat_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_habitat" et "intitule_habitat" de la "t_habitat"
            str_sql_id_habitat = "SELECT id_habitat, intitule_habitat, date_ins_habitat FROM t_habitat " \
                               "WHERE id_habitat = %(value_id_habitat)s"
            valeur_select_dictionnaire = {"value_id_habitat": id_habitat_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_habitat, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom habitat" pour l'UPDATE
            data_nom_habitat = mybd_conn.fetchone()
            print("data_nom_habitat ", data_nom_habitat, " type ", type(data_nom_habitat), " habitat ",
                  data_nom_habitat["intitule_habitat"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "habitat_update_wtf.html"
            form_update.nom_habitat_update_wtf.data = data_nom_habitat["intitule_habitat"]
            form_update.date_habitat_wtf_essai.data = data_nom_habitat["date_ins_habitat"]

    except Exception as Exception_habitat_update_wtf:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{habitat_update_wtf.__name__} ; "
                                      f"{Exception_habitat_update_wtf}")

    return render_template("habitat/habitat_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /habitat_delete
    
    Test : ex. cliquer sur le menu "habitat" puis cliquer sur le bouton "DELETE" d'un "habitat"
    
    Paramètres : sans
    
    But : Effacer(delete) un habitat qui a été sélectionné dans le formulaire "habitat_afficher.html"
    
    Remarque :  Dans le champ "nom_habitat_delete_wtf" du formulaire "habitat/habitat_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/habitat_delete", methods=['GET', 'POST'])
def habitat_delete_wtf():
    data_films_attribue_habitat_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_habitat"
    id_habitat_delete = request.values['id_habitat_btn_delete_html']

    # Objet formulaire pour effacer le habitat sélectionné.
    form_delete = FormWTFDeletehabitat()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("habitat_afficher", order_by="ASC", id_habitat_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "habitat/habitat_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_films_attribue_habitat_delete = session['data_films_attribue_habitat_delete']
                print("data_films_attribue_habitat_delete ", data_films_attribue_habitat_delete)

                flash(f"Effacer le habitat de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer habitat" qui va irrémédiablement EFFACER le habitat
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_habitat": id_habitat_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_films_habitat = """DELETE FROM t_habitat_film WHERE fk_habitat = %(value_id_habitat)s"""
                str_sql_delete_idhabitat = """DELETE FROM t_habitat WHERE id_habitat = %(value_id_habitat)s"""
                # Manière brutale d'effacer d'abord la "fk_habitat", même si elle n'existe pas dans la "t_habitat_film"
                # Ensuite on peut effacer le habitat vu qu'il n'est plus "lié" (INNODB) dans la "t_habitat_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_films_habitat, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idhabitat, valeur_delete_dictionnaire)

                flash(f"habitat définitivement effacé !!", "success")
                print(f"habitat définitivement effacé !!")

                # afficher les données
                return redirect(url_for('habitat_afficher', order_by="ASC", id_habitat_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_habitat": id_habitat_delete}
            print(id_habitat_delete, type(id_habitat_delete))

            # Requête qui affiche tous les films_habitat qui ont le habitat que l'utilisateur veut effacer
            str_sql_habitat_films_delete = """SELECT id_habitat_film, nom_film, id_habitat, intitule_habitat FROM t_habitat_film 
                                            INNER JOIN t_film ON t_habitat_film.fk_film = t_film.id_film
                                            INNER JOIN t_habitat ON t_habitat_film.fk_habitat = t_habitat.id_habitat
                                            WHERE fk_habitat = %(value_id_habitat)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_habitat_films_delete, valeur_select_dictionnaire)
                data_films_attribue_habitat_delete = mydb_conn.fetchall()
                print("data_films_attribue_habitat_delete...", data_films_attribue_habitat_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "habitat/habitat_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_films_attribue_habitat_delete'] = data_films_attribue_habitat_delete

                # Opération sur la BD pour récupérer "id_habitat" et "intitule_habitat" de la "t_habitat"
                str_sql_id_habitat = "SELECT id_habitat, intitule_habitat FROM t_habitat WHERE id_habitat = %(value_id_habitat)s"

                mydb_conn.execute(str_sql_id_habitat, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom habitat" pour l'action DELETE
                data_nom_habitat = mydb_conn.fetchone()
                print("data_nom_habitat ", data_nom_habitat, " type ", type(data_nom_habitat), " habitat ",
                      data_nom_habitat["intitule_habitat"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "habitat_delete_wtf.html"
            form_delete.nom_habitat_delete_wtf.data = data_nom_habitat["intitule_habitat"]

            # Le bouton pour l'action "DELETE" dans le form. "habitat_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_habitat_delete_wtf:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{habitat_delete_wtf.__name__} ; "
                                      f"{Exception_habitat_delete_wtf}")

    return render_template("habitat/habitat_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_habitat_delete)
