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
                # Récupération des données du formulaire
                nom_habitat_wtf = form.nom_habitat_wtf.data
                description_habitat = nom_habitat_wtf.lower()

                # Constitution du dictionnaire de valeurs
                valeurs_insertion_dictionnaire = {"Description": description_habitat}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                # Insertion dans la base de données
                strsql_insert_habitat = """INSERT INTO t_habitat (Description) VALUES (%(Description)s);"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_habitat, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse (DESC)
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
    if request.method == "GET":
        id_habitat_update = request.args.get('id_habitat')
    else:
        id_habitat_update = request.form.get('id_habitat_btn_edit_html')

    print(f"Valeur de id_habitat_update (GET ou POST) : {id_habitat_update}")

    if not id_habitat_update:
        flash("Aucun ID d'habitat n'a été fourni pour la mise à jour.", "danger")
        return redirect(url_for('habitat_afficher', order_by="ASC", id_habitat_sel=0))

    form_update = FormWTFUpdatehabitat()
    try:
        if request.method == "POST":
            print("Requête POST détectée")
            print(f"Contenu du formulaire POST: {request.form}")
            if form_update.validate_on_submit():
                print("Le formulaire est validé")
                name_habitat_update = form_update.nom_habitat_update_wtf.data
                name_habitat_update = name_habitat_update.lower()

                valeur_update_dictionnaire = {
                    "id_habitat": id_habitat_update,
                    "Description": name_habitat_update
                }

                print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

                str_sql_update_intitulehabitat = """
                    UPDATE t_habitat 
                    SET Description = %(Description)s 
                    WHERE id_habitat = %(id_habitat)s 
                """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_update_intitulehabitat, valeur_update_dictionnaire)

                flash("Donnée mise à jour !!", "success")
                print("Donnée mise à jour !!")

                return redirect(url_for('habitat_afficher', order_by="ASC", id_habitat_sel=id_habitat_update))
            else:
                print("Le formulaire n'est pas validé")
                print(f"Erreurs du formulaire : {form_update.errors}")

        elif request.method == "GET":
            str_sql_id_habitat = "SELECT id_habitat, Description FROM t_habitat WHERE id_habitat = %(value_id_habitat)s"
            valeur_select_dictionnaire = {"value_id_habitat": id_habitat_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_habitat, valeur_select_dictionnaire)
                data_nom_habitat = mybd_conn.fetchone()

                if data_nom_habitat:
                    print("data_nom_habitat ", data_nom_habitat, " type ", type(data_nom_habitat))
                    form_update.nom_habitat_update_wtf.data = data_nom_habitat["Description"]
                else:
                    flash(f"L'habitat avec l'ID {id_habitat_update} n'existe pas.", "danger")
                    return redirect(url_for('habitat_afficher', order_by="ASC", id_habitat_sel=0))

    except Exception as Exception_habitat_update_wtf:
        raise ExceptionGenreUpdateWtf(
            f"fichier : {Path(__file__).name}  ;  "
            f"{habitat_update_wtf.__name__} ; "
            f"{Exception_habitat_update_wtf}"
        )

    return render_template("habitat/habitat_update_wtf.html", form_update=form_update, id_habitat=id_habitat_update)


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
















from pathlib import Path

from flask import redirect, request, session, url_for, render_template, flash

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.habitat.gestion_habitat_wtf_forms import FormWTFAjouterLiaison, FormWTFUpdateLiaison, FormWTFDeleteLiaison

@app.route("/plantes_habitat_afficher/<string:order_by>/<int:id_plante_habitat_sel>", methods=['GET', 'POST'])
def plantes_habitat_afficher(order_by, id_plante_habitat_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_plante_habitat_sel == 0:
                    strsql_plantes_habitat_afficher = """SELECT 
                                                            ph.ID_Plantes_Habitat, 
                                                            p.ID_Plante, 
                                                            p.Nom_Commun, 
                                                            p.Nom_Scientifique, 
                                                            p.Famille, 
                                                            h.ID_Habitat, 
                                                            h.Description 
                                                        FROM 
                                                            t_plantes p
                                                        JOIN 
                                                            t_plantes_habitat ph ON p.ID_Plante = ph.FK_plantes_habitat
                                                        JOIN 
                                                            t_habitat h ON ph.FK_habitat_plantes = h.ID_Habitat
                                                        ORDER BY 
                                                            ph.ID_Plantes_Habitat ASC;"""
                    mc_afficher.execute(strsql_plantes_habitat_afficher)
                elif order_by == "ASC":
                    valeur_id_habitat_selected_dictionnaire = {"value_id_plante_habitat_selected": id_plante_habitat_sel}
                    strsql_plantes_habitat_afficher = """SELECT 
                                                            ph.ID_Plantes_Habitat, 
                                                            p.ID_Plante, 
                                                            p.Nom_Commun, 
                                                            p.Nom_Scientifique, 
                                                            p.Famille, 
                                                            h.ID_Habitat, 
                                                            h.Description 
                                                        FROM 
                                                            t_plantes p
                                                        JOIN 
                                                            t_plantes_habitat ph ON p.ID_Plante = ph.FK_plantes_habitat
                                                        JOIN 
                                                            t_habitat h ON ph.FK_habitat_plantes = h.ID_Habitat
                                                        WHERE 
                                                            ph.ID_Plantes_Habitat = %(value_id_plante_habitat_selected)s
                                                        ORDER BY 
                                                            ph.ID_Plantes_Habitat ASC;"""
                    mc_afficher.execute(strsql_plantes_habitat_afficher, valeur_id_habitat_selected_dictionnaire)
                else:
                    strsql_plantes_habitat_afficher = """SELECT 
                                                            ph.ID_Plantes_Habitat, 
                                                            p.ID_Plante, 
                                                            p.Nom_Commun, 
                                                            p.Nom_Scientifique, 
                                                            p.Famille, 
                                                            h.ID_Habitat, 
                                                            h.Description 
                                                        FROM 
                                                            t_plantes p
                                                        JOIN 
                                                            t_plantes_habitat ph ON p.ID_Plante = ph.FK_plantes_habitat
                                                        JOIN 
                                                            t_habitat h ON ph.FK_habitat_plantes = h.ID_Habitat
                                                        ORDER BY 
                                                            ph.ID_Plantes_Habitat ASC;"""
                    mc_afficher.execute(strsql_plantes_habitat_afficher)

                data_habitat = mc_afficher.fetchall()

                if not data_habitat and id_plante_habitat_sel == 0:
                    flash("La table est vide.", "warning")
                elif not data_habitat and id_plante_habitat_sel > 0:
                    flash("La liaison demandée n'existe pas !!", "warning")
                else:
                    flash("Données affichées !!", "success")

        except Exception as Exception_habitat_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{plantes_habitat_afficher.__name__} ; "
                                          f"{Exception_habitat_afficher}")

    return render_template("habitat/plantes_habitat_afficher.html", data=data_habitat)


@app.route("/liaison_ajouter", methods=['GET', 'POST'])
def liaison_ajouter_wtf():
    form = FormWTFAjouterLiaison()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                fk_plantes_habitat = form.fk_plantes_habitat_wtf.data
                fk_habitat_plantes = form.fk_habitat_plantes_wtf.data

                valeurs_insertion_dictionnaire = {"fk_plantes_habitat": fk_plantes_habitat, "fk_habitat_plantes": fk_habitat_plantes}

                strsql_insert_liaison = """INSERT INTO t_plantes_habitat (FK_plantes_habitat, FK_habitat_plantes) VALUES (%(fk_plantes_habitat)s, %(fk_habitat_plantes)s);"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_liaison, valeurs_insertion_dictionnaire)

                flash("Liaison ajoutée !!", "success")
                return redirect(url_for('plantes_habitat_afficher', order_by='DESC', id_plante_habitat_sel=0))

        except Exception as Exception_liaison_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{liaison_ajouter_wtf.__name__} ; "
                                            f"{Exception_liaison_ajouter_wtf}")

    return render_template("habitat/liaison_ajouter_wtf.html", form=form)

@app.route("/liaison_update", methods=['GET', 'POST'])
def liaison_update_wtf():
    form_update = FormWTFUpdateLiaison()

    if request.method == "GET":
        id_liaison_update = request.args.get('id_liaison')
        if id_liaison_update:
            # Charger les données existantes pour remplir le formulaire
            str_sql_liaison = """SELECT ID_Plantes_Habitat, FK_plantes_habitat, FK_habitat_plantes 
                                 FROM t_plantes_habitat 
                                 WHERE ID_Plantes_Habitat = %(value_id_liaison)s"""
            valeur_select_dictionnaire = {"value_id_liaison": id_liaison_update}
            try:
                with DBconnection() as mybd_conn:
                    mybd_conn.execute(str_sql_liaison, valeur_select_dictionnaire)
                    data_liaison = mybd_conn.fetchone()

                    if data_liaison:
                        form_update.id_liaison.data = data_liaison["ID_Plantes_Habitat"]
                        form_update.fk_plantes_habitat_wtf.data = data_liaison["FK_plantes_habitat"]
                        form_update.fk_habitat_plantes_wtf.data = data_liaison["FK_habitat_plantes"]
                    else:
                        flash(f"La liaison avec l'ID {id_liaison_update} n'existe pas.", "danger")
                        return redirect(url_for('plantes_habitat_afficher', order_by="ASC", id_plante_habitat_sel=0))
            except Exception as Exception_liaison_update_wtf:
                raise ExceptionGenreUpdateWtf(
                    f"fichier : {Path(__file__).name}  ;  "
                    f"{liaison_update_wtf.__name__} ; "
                    f"{Exception_liaison_update_wtf}"
                )

    elif request.method == "POST":
        id_liaison_update = form_update.id_liaison.data  # Récupérer l'ID depuis le champ caché
        if not id_liaison_update:
            flash("Aucun ID de liaison n'a été fourni pour la mise à jour.", "danger")
            return redirect(url_for('plantes_habitat_afficher', order_by="ASC", id_plante_habitat_sel=0))

        if form_update.validate_on_submit():
            fk_plantes_habitat = form_update.fk_plantes_habitat_wtf.data
            fk_habitat_plantes = form_update.fk_habitat_plantes_wtf.data

            valeur_update_dictionnaire = {
                "ID_Plantes_Habitat": id_liaison_update,
                "FK_plantes_habitat": fk_plantes_habitat,
                "FK_habitat_plantes": fk_habitat_plantes
            }

            str_sql_update_liaison = """UPDATE t_plantes_habitat 
                                        SET FK_plantes_habitat = %(FK_plantes_habitat)s, FK_habitat_plantes = %(FK_habitat_plantes)s 
                                        WHERE ID_Plantes_Habitat = %(ID_Plantes_Habitat)s"""
            try:
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_update_liaison, valeur_update_dictionnaire)
                flash("Liaison mise à jour !!", "success")
                return redirect(url_for('plantes_habitat_afficher', order_by="ASC", id_plante_habitat_sel=id_liaison_update))
            except Exception as Exception_liaison_update_wtf:
                raise ExceptionGenreUpdateWtf(
                    f"fichier : {Path(__file__).name}  ;  "
                    f"{liaison_update_wtf.__name__} ; "
                    f"{Exception_liaison_update_wtf}"
                )

    return render_template("habitat/liaison_update_wtf.html", form_update=form_update, id_liaison=id_liaison_update)

@app.route("/liaison_delete", methods=['GET', 'POST'])
def liaison_delete_wtf():
    data_plantes_habitat_delete = None
    id_liaison_delete = request.values.get('id_liaison')  # Utilisation de request.values.get

    form_delete = FormWTFDeleteLiaison()
    try:
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("plantes_habitat_afficher", order_by="ASC", id_plante_habitat_sel=0))

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_liaison": id_liaison_delete}
                str_sql_delete_liaison = """DELETE FROM t_plantes_habitat WHERE ID_Plantes_Habitat = %(value_id_liaison)s"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_liaison, valeur_delete_dictionnaire)

                flash(f"Liaison définitivement effacée !!", "success")

                return redirect(url_for('plantes_habitat_afficher', order_by="ASC", id_plante_habitat_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_liaison": id_liaison_delete}

            str_sql_liaison_delete = """SELECT ID_Plantes_Habitat, FK_plantes_habitat, FK_habitat_plantes 
                                        FROM t_plantes_habitat 
                                        WHERE ID_Plantes_Habitat = %(value_id_liaison)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_liaison_delete, valeur_select_dictionnaire)
                data_liaison = mydb_conn.fetchone()

                if data_liaison:
                    form_delete.fk_plantes_habitat_delete_wtf.data = data_liaison["FK_plantes_habitat"]
                    form_delete.fk_habitat_plantes_delete_wtf.data = data_liaison["FK_habitat_plantes"]

                    session['data_plantes_habitat_delete'] = data_liaison
                else:
                    flash(f"La liaison avec l'ID {id_liaison_delete} n'existe pas.", "danger")
                    return redirect(url_for('plantes_habitat_afficher', order_by="ASC", id_plante_habitat_sel=0))

    except Exception as Exception_liaison_delete_wtf:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{liaison_delete_wtf.__name__} ; "
                                      f"{Exception_liaison_delete_wtf}")

    return render_template("habitat/liaison_delete_wtf.html",
                           form_delete=form_delete,
                           data_liaison=data_plantes_habitat_delete)
