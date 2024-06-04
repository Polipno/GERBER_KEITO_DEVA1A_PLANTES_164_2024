-- Sélectionner toutes les plantes
SELECT * FROM `t_plantes`;

-- Sélectionner toutes les exigences de croissance
SELECT * FROM `t_exigences_de_croissance`;

-- Sélectionner les plantes d'une certaine famille
SELECT * FROM `t_plantes` WHERE `Famille` = 'Rosaceae';

-- Sélectionner les besoins en eau et en lumière des plantes
SELECT p.Nom_Commun, e.Eau, e.Lumière
FROM `t_plantes` p
JOIN `t_exigences_de_croissance` e ON p.ID_Plante = e.ID_Exigence;

-- Sélectionner les plantes qui nécessitent beaucoup de lumière
SELECT p.Nom_Commun, e.Lumière
FROM `t_plantes` p
JOIN `t_exigences_de_croissance` e ON p.ID_Plante = e.ID_Exigence
WHERE e.Lumière = 'Beaucoup';

-- Compter le nombre de plantes par famille
SELECT `Famille`, COUNT(*) AS `Nombre_De_Plantes`
FROM `t_plantes`
GROUP BY `Famille`;

-- Obtenir la moyenne des besoins en eau par type de sol
SELECT e.Type_De_Sol, AVG(e.Eau) AS Moyenne_Eau
FROM `t_exigences_de_croissance` e
GROUP BY e.Type_De_Sol;

-- Trouver les plantes avec des besoins en eau spécifique
SELECT p.Nom_Commun, e.Eau
FROM `t_plantes` p
JOIN `t_exigences_de_croissance` e ON p.ID_Plante = e.ID_Exigence
WHERE e.Eau = 'Modérée';

-- Sélectionner les plantes avec des besoins spécifiques de sol et de lumière
SELECT p.Nom_Commun, e.Type_De_Sol, e.Lumière
FROM `t_plantes` p
JOIN `t_exigences_de_croissance` e ON p.ID_Plante = e.ID_Exigence
WHERE e.Type_De_Sol = 'Argileux' AND e.Lumière = 'Faible';

-- Compter le nombre de plantes par type de sol
SELECT e.Type_De_Sol, COUNT(*) AS Nombre_De_Plantes
FROM `t_exigences_de_croissance` e
GROUP BY e.Type_De_Sol;

-- Trouver les plantes qui nécessitent peu de lumière et beaucoup d'eau
SELECT p.Nom_Commun, e.Lumière, e.Eau
FROM `t_plantes` p
JOIN `t_exigences_de_croissance` e ON p.ID_Plante = e.ID_Exigence
WHERE e.Lumière = 'Faible' AND e.Eau = 'Beaucoup';

-- Lister les exigences de croissance des plantes par famille
SELECT p.Famille, e.Lumière, e.Eau, e.Type_De_Sol
FROM `t_plantes` p
JOIN `t_exigences_de_croissance` e ON p.ID_Plante = e.ID_Exigence
ORDER BY p.Famille;

-- Trouver les plantes par nom commun contenant un certain mot
SELECT * FROM `t_plantes`
WHERE `Nom_Commun` LIKE '%rose%';

-- Compter le nombre de plantes par niveau de lumière requis
SELECT e.Lumière, COUNT(*) AS Nombre_De_Plantes
FROM `t_exigences_de_croissance` e
GROUP BY e.Lumière;

-- Trouver les plantes ayant des exigences de croissance similaires
SELECT p1.Nom_Commun AS Plante1, p2.Nom_Commun AS Plante2
FROM `t_exigences_de_croissance` e1
JOIN `t_exigences_de_croissance` e2 ON e1.Lumière = e2.Lumière AND e1.Eau = e2.Eau AND e1.Type_De_Sol = e2.Type_De_Sol
JOIN `t_plantes` p1 ON e1.ID_Exigence = p1.ID_Plante
JOIN `t_plantes` p2 ON e2.ID_Exigence = p2.ID_Plante
WHERE p1.ID_Plante <> p2.ID_Plante;

-- Lister les plantes et leurs exigences de croissance triées par type de sol
SELECT p.Nom_Commun, e.Type_De_Sol, e.Lumière, e.Eau
FROM `t_plantes` p
JOIN `t_exigences_de_croissance` e ON p.ID_Plante = e.ID_Exigence
ORDER BY e.Type_De_Sol;

-- Trouver les plantes nécessitant un certain type de sol
SELECT p.Nom_Commun, e.Type_De_Sol
FROM `t_plantes` p
JOIN `t_exigences_de_croissance` e ON p.ID_Plante = e.ID_Exigence
WHERE e.Type_De_Sol = 'Sableux';

-- Obtenir la liste des familles de plantes et le nombre de plantes dans chaque famille
SELECT `Famille`, COUNT(*) AS `Nombre_De_Plantes`
FROM `t_plantes`
GROUP BY `Famille`;



-- Obtenir les plantes nécessitant des conditions de croissance spéciales
SELECT p.Nom_Commun, e.Lumière, e.Eau, e.Type_De_Sol
FROM `t_plantes` p
JOIN `t_exigences_de_croissance` e ON p.ID_Plante = e.ID_Exigence
WHERE e.Lumière = 'Modérée' AND e.Eau = 'Modérée' AND e.Type_De_Sol = 'Humifère';

-- Trouver les plantes par nom latin avec un certain motif
SELECT * FROM `t_plantes`
WHERE `Nom_Scientifique` LIKE '%quercus%';

-- Compter les exigences de croissance par niveau d'eau
SELECT e.Eau, COUNT(*) AS Nombre_De_Exigences
FROM `t_exigences_de_croissance` e
GROUP BY e.Eau;
