"""Gestion des "routes" FLASK et des données pour les exigences_de_croissance.
Fichier : gestion_exigences_de_croissance_crud.py
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
from APP_FILMS_164.exigences_de_croissance.gestion_exigences_de_croissance_wtf_forms import FormWTFAjouterexigences_de_croissance
from APP_FILMS_164.exigences_de_croissance.gestion_exigences_de_croissance_wtf_forms import FormWTFDeleteexigences_de_croissance
from APP_FILMS_164.exigences_de_croissance.gestion_exigences_de_croissance_wtf_forms import FormWTFUpdateexigences_de_croissance

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /exigences_de_croissance_afficher
    
    Test : ex : http://127.0.0.1:5575/exigences_de_croissance_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                ID_Exigence_sel = 0 >> tous les exigences_de_croissance.
                ID_Exigence_sel = "n" affiche le exigences_de_croissance dont l'id est "n"
"""


@app.route("/exigences_de_croissance_afficher/<string:order_by>/<int:ID_Exigence_sel>", methods=['GET', 'POST'])
def exigences_de_croissance_afficher(order_by, ID_Exigence_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and ID_Exigence_sel == 0:
                    strsql_exigences_de_croissance_afficher = """SELECT * FROM t_exigences_de_croissance"""
                    mc_afficher.execute(strsql_exigences_de_croissance_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_exigences_de_croissance"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du exigences_de_croissance sélectionné avec un nom de variable
                    valeur_ID_Exigence_selected_dictionnaire = {"value_ID_Exigence_selected": ID_Exigence_sel}
                    strsql_exigences_de_croissance_afficher = """SELECT * FROM t_exigences_de_croissance"""

                    mc_afficher.execute(strsql_exigences_de_croissance_afficher, valeur_ID_Exigence_selected_dictionnaire)
                else:
                    strsql_exigences_de_croissance_afficher = """SELECT * FROM t_exigences_de_croissance"""

                    mc_afficher.execute(strsql_exigences_de_croissance_afficher)

                data_exigences_de_croissance = mc_afficher.fetchall()

                print("data_exigences_de_croissance ", data_exigences_de_croissance, " Type : ", type(data_exigences_de_croissance))

                # Différencier les messages si la table est vide.
                if not data_exigences_de_croissance and ID_Exigence_sel == 0:
                    flash("""La table "t_exigences_de_croissance" est vide. !!""", "warning")
                elif not data_exigences_de_croissance and ID_Exigence_sel > 0:
                    # Si l'utilisateur change l'ID_Exigence dans l'URL et que le exigences_de_croissance n'existe pas,
                    flash(f"Le exigences_de_croissance demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_exigences_de_croissance" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données exigences_de_croissance affichés !!", "success")

        except Exception as Exception_exigences_de_croissance_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{exigences_de_croissance_afficher.__name__} ; "
                                          f"{Exception_exigences_de_croissance_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("exigences_de_croissance/exigences_de_croissance_afficher.html", data=data_exigences_de_croissance)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /exigences_de_croissance_ajouter
    
    Test : ex : http://127.0.0.1:5575/exigences_de_croissance_ajouter
    
    Paramètres : sans
    
    But : Ajouter un exigences_de_croissance pour un film
    
    Remarque :  Dans le champ "name_exigences_de_croissance_html" du formulaire "exigences_de_croissance/exigences_de_croissance_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/exigences_de_croissance_ajouter", methods=['GET', 'POST'])
def exigences_de_croissance_ajouter_wtf():
    form = FormWTFAjouterexigences_de_croissance()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_exigences_de_croissance_wtf = form.nom_exigences_de_croissance_wtf.data
                name_exigences_de_croissance = name_exigences_de_croissance_wtf.lower()
                valeurs_insertion_dictionnaire = {"value_intitule_exigences_de_croissance": name_exigences_de_croissance}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_exigences_de_croissance = """INSERT INTO t_exigences_de_croissance (ID_Exigence, Lumière, Eau, Type_De_Sol) VALUES (NULL,%(value_intitule_exigences_de_croissance)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_exigences_de_croissance, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('exigences_de_croissance_afficher', order_by='ASC', ID_Exigence_sel=0))

        except Exception as Exception_exigences_de_croissance_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{exigences_de_croissance_ajouter_wtf.__name__} ; "
                                            f"{Exception_exigences_de_croissance_ajouter_wtf}")

    return render_template("exigences_de_croissance/exigences_de_croissance_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /exigences_de_croissance_update
    
    Test : ex cliquer sur le menu "exigences_de_croissance" puis cliquer sur le bouton "EDIT" d'un "exigences_de_croissance"
    
    Paramètres : sans
    
    But : Editer(update) un exigences_de_croissance qui a été sélectionné dans le formulaire "exigences_de_croissance_afficher.html"
    
    Remarque :  Dans le champ "nom_exigences_de_croissance_update_wtf" du formulaire "exigences_de_croissance/exigences_de_croissance_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/exigences_de_croissance_update", methods=['GET', 'POST'])
def exigences_de_croissance_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "ID_Exigence"
    ID_Exigence_update = request.values['ID_Exigence_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateexigences_de_croissance()
    try:
        # 2023.05.14 OM S'il y a des listes déroulantes dans le formulaire
        # La validation pose quelques problèmes
        if request.method == "POST" and form_update.submit.data:
            # Récupèrer la valeur du champ depuis "exigences_de_croissance_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            name_exigences_de_croissance_update = form_update.nom_exigences_de_croissance_update_wtf.data
            name_exigences_de_croissance_update = name_exigences_de_croissance_update.lower()
            date_exigences_de_croissance_essai = form_update.date_exigences_de_croissance_wtf_essai.data

            valeur_update_dictionnaire = {"value_ID_Exigence": ID_Exigence_update,
                                          "value_name_exigences_de_croissance": name_exigences_de_croissance_update,
                                          "value_date_exigences_de_croissance_essai": date_exigences_de_croissance_essai
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_intituleexigences_de_croissance = """UPDATE t_exigences_de_croissance SET intitule_exigences_de_croissance = %(value_name_exigences_de_croissance)s, 
            date_ins_exigences_de_croissance = %(value_date_exigences_de_croissance_essai)s WHERE ID_Exigence = %(value_ID_Exigence)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_intituleexigences_de_croissance, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"ID_Exigence_update"
            return redirect(url_for('exigences_de_croissance_afficher', order_by="ASC", ID_Exigence_sel=ID_Exigence_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "ID_Exigence" et "intitule_exigences_de_croissance" de la "t_exigences_de_croissance"
            str_sql_ID_Exigence = "SELECT ID_Exigence, intitule_exigences_de_croissance, date_ins_exigences_de_croissance FROM t_exigences_de_croissance " \
                               "WHERE ID_Exigence = %(value_ID_Exigence)s"
            valeur_select_dictionnaire = {"value_ID_Exigence": ID_Exigence_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_ID_Exigence, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom exigences_de_croissance" pour l'UPDATE
            data_nom_exigences_de_croissance = mybd_conn.fetchone()
            print("data_nom_exigences_de_croissance ", data_nom_exigences_de_croissance, " type ", type(data_nom_exigences_de_croissance), " exigences_de_croissance ",
                  data_nom_exigences_de_croissance["intitule_exigences_de_croissance"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "exigences_de_croissance_update_wtf.html"
            form_update.nom_exigences_de_croissance_update_wtf.data = data_nom_exigences_de_croissance["intitule_exigences_de_croissance"]
            form_update.date_exigences_de_croissance_wtf_essai.data = data_nom_exigences_de_croissance["date_ins_exigences_de_croissance"]

    except Exception as Exception_exigences_de_croissance_update_wtf:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{exigences_de_croissance_update_wtf.__name__} ; "
                                      f"{Exception_exigences_de_croissance_update_wtf}")

    return render_template("exigences_de_croissance/exigences_de_croissance_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /exigences_de_croissance_delete
    
    Test : ex. cliquer sur le menu "exigences_de_croissance" puis cliquer sur le bouton "DELETE" d'un "exigences_de_croissance"
    
    Paramètres : sans
    
    But : Effacer(delete) un exigences_de_croissance qui a été sélectionné dans le formulaire "exigences_de_croissance_afficher.html"
    
    Remarque :  Dans le champ "nom_exigences_de_croissance_delete_wtf" du formulaire "exigences_de_croissance/exigences_de_croissance_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/exigences_de_croissance_delete", methods=['GET', 'POST'])
def exigences_de_croissance_delete_wtf():
    data_films_attribue_exigences_de_croissance_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "ID_Exigence"
    ID_Exigence_delete = request.values['ID_Exigence_btn_delete_html']

    # Objet formulaire pour effacer le exigences_de_croissance sélectionné.
    form_delete = FormWTFDeleteexigences_de_croissance()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("exigences_de_croissance_afficher", order_by="ASC", ID_Exigence_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "exigences_de_croissance/exigences_de_croissance_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_films_attribue_exigences_de_croissance_delete = session['data_films_attribue_exigences_de_croissance_delete']
                print("data_films_attribue_exigences_de_croissance_delete ", data_films_attribue_exigences_de_croissance_delete)

                flash(f"Effacer le exigences_de_croissance de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer exigences_de_croissance" qui va irrémédiablement EFFACER le exigences_de_croissance
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_ID_Exigence": ID_Exigence_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_films_exigences_de_croissance = """DELETE FROM t_exigences_de_croissance_film WHERE fk_exigences_de_croissance = %(value_ID_Exigence)s"""
                str_sql_delete_idexigences_de_croissance = """DELETE FROM t_exigences_de_croissance WHERE ID_Exigence = %(value_ID_Exigence)s"""
                # Manière brutale d'effacer d'abord la "fk_exigences_de_croissance", même si elle n'existe pas dans la "t_exigences_de_croissance_film"
                # Ensuite on peut effacer le exigences_de_croissance vu qu'il n'est plus "lié" (INNODB) dans la "t_exigences_de_croissance_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_films_exigences_de_croissance, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idexigences_de_croissance, valeur_delete_dictionnaire)

                flash(f"exigences_de_croissance définitivement effacé !!", "success")
                print(f"exigences_de_croissance définitivement effacé !!")

                # afficher les données
                return redirect(url_for('exigences_de_croissance_afficher', order_by="ASC", ID_Exigence_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_ID_Exigence": ID_Exigence_delete}
            print(ID_Exigence_delete, type(ID_Exigence_delete))

            # Requête qui affiche tous les films_exigences_de_croissance qui ont le exigences_de_croissance que l'utilisateur veut effacer
            str_sql_exigences_de_croissance_films_delete = """SELECT ID_Exigence_film, nom_film, ID_Exigence, intitule_exigences_de_croissance FROM t_exigences_de_croissance_film 
                                            INNER JOIN t_film ON t_exigences_de_croissance_film.fk_film = t_film.id_film
                                            INNER JOIN t_exigences_de_croissance ON t_exigences_de_croissance_film.fk_exigences_de_croissance = t_exigences_de_croissance.ID_Exigence
                                            WHERE fk_exigences_de_croissance = %(value_ID_Exigence)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_exigences_de_croissance_films_delete, valeur_select_dictionnaire)
                data_films_attribue_exigences_de_croissance_delete = mydb_conn.fetchall()
                print("data_films_attribue_exigences_de_croissance_delete...", data_films_attribue_exigences_de_croissance_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "exigences_de_croissance/exigences_de_croissance_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_films_attribue_exigences_de_croissance_delete'] = data_films_attribue_exigences_de_croissance_delete

                # Opération sur la BD pour récupérer "ID_Exigence" et "intitule_exigences_de_croissance" de la "t_exigences_de_croissance"
                str_sql_ID_Exigence = "SELECT ID_Exigence, intitule_exigences_de_croissance FROM t_exigences_de_croissance WHERE ID_Exigence = %(value_ID_Exigence)s"

                mydb_conn.execute(str_sql_ID_Exigence, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom exigences_de_croissance" pour l'action DELETE
                data_nom_exigences_de_croissance = mydb_conn.fetchone()
                print("data_nom_exigences_de_croissance ", data_nom_exigences_de_croissance, " type ", type(data_nom_exigences_de_croissance), " exigences_de_croissance ",
                      data_nom_exigences_de_croissance["intitule_exigences_de_croissance"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "exigences_de_croissance_delete_wtf.html"
            form_delete.nom_exigences_de_croissance_delete_wtf.data = data_nom_exigences_de_croissance["intitule_exigences_de_croissance"]

            # Le bouton pour l'action "DELETE" dans le form. "exigences_de_croissance_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_exigences_de_croissance_delete_wtf:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{exigences_de_croissance_delete_wtf.__name__} ; "
                                      f"{Exception_exigences_de_croissance_delete_wtf}")

    return render_template("exigences_de_croissance/exigences_de_croissance_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_exigences_de_croissance_delete)





@app.route("/plantes_exigences_de_croissance_afficher/<string:order_by>/<int:id_plante_exigences_de_croissance_sel>", methods=['GET', 'POST'])
def plantes_exigences_de_croissance_afficher(order_by, id_plante_exigences_de_croissance_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_plante_exigences_de_croissance_sel == 0:
                    strsql_plantes_exigences_de_croissance_afficher = """SELECT 
    p.*, 
    e.*
FROM 
    t_plantes p
JOIN 
    t_plantes_exigence_de_croissance pe ON p.id_plante = pe.FK_plantes_Exigence
JOIN 
    t_exigences_de_croissance e ON pe.FK_Exigence_plantes = e.id_Exigence
ORDER BY 
    p.id_plante;"""
                    mc_afficher.execute(strsql_plantes_exigences_de_croissance_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_exigences_de_croissance"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du exigences_de_croissance sélectionné avec un nom de variable
                    valeur_ID_Exigence_selected_dictionnaire = {"value_ID_Exigence_selected": id_plante_exigences_de_croissance_sel}
                    strsql_plantes_exigences_de_croissance_afficher = """SELECT 
    p.*, 
    e.*
FROM 
    t_plantes p
JOIN 
    t_plantes_exigence_de_croissance pe ON p.id_plante = pe.FK_plantes_Exigence
JOIN 
    t_exigences_de_croissance e ON pe.FK_Exigence_plantes = e.id_Exigence
ORDER BY 
    p.id_plante;"""

                    mc_afficher.execute(strsql_plantes_exigences_de_croissance_afficher, valeur_ID_Exigence_selected_dictionnaire)
                else:
                    strsql_plantes_exigences_de_croissance_afficher = """SELECT 
    p.*, 
    e.*
FROM 
    t_plantes p
JOIN 
    t_plantes_exigence_de_croissance pe ON p.id_plante = pe.FK_plantes_Exigence
JOIN 
    t_exigences_de_croissance e ON pe.FK_Exigence_plantes = e.id_Exigence
ORDER BY 
    p.id_plante;"""

                    mc_afficher.execute(strsql_plantes_exigences_de_croissance_afficher)

                data_exigences_de_croissance = mc_afficher.fetchall()

                print("data_exigences_de_croissance ", data_exigences_de_croissance, " Type : ", type(data_exigences_de_croissance))

                # Différencier les messages si la table est vide.
                if not data_exigences_de_croissance and id_plante_exigences_de_croissance_sel == 0:
                    flash("""La table "t_exigences_de_croissance" est vide. !!""", "warning")
                elif not data_exigences_de_croissance and id_plante_exigences_de_croissance_sel > 0:
                    # Si l'utilisateur change l'ID_Exigence dans l'URL et que le exigences_de_croissance n'existe pas,
                    flash(f"Le exigences_de_croissance demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_exigences_de_croissance" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données exigences_de_croissance affichés !!", "success")

        except Exception as Exception_exigences_de_croissance_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{exigences_de_croissance_afficher.__name__} ; "
                                          f"{Exception_exigences_de_croissance_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("exigences_de_croissance/plantes_exigences_de_croissance_afficher.html", data=data_exigences_de_croissance)