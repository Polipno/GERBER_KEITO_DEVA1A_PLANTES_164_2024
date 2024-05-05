-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: MACCAUD_OLIVIER_INFO1X_FILMS_164_2023

-- Destruction de la BD si elle existe.
-- Pour être certain d'avoir la dernière version des données

DROP DATABASE IF EXISTS GERBER_KEITO_DEVA1A_PLANTES_164_2024;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS GERBER_KEITO_DEVA1A_PLANTES_164_2024;

-- Utilisation de cette base de donnée

USE GERBER_KEITO_DEVA1A_PLANTES_164_2024;




-- Listage de la structure de table gerber_keito_deva1a_mpd_gestion_des_plantes. t_utillisation
DROP TABLE IF EXISTS `t_utillisation`;
CREATE TABLE IF NOT EXISTS `t_utillisation` (
  `ID_Utillisation` int NOT NULL AUTO_INCREMENT COMMENT 'Un identifiant unique pour chaque utilisation.',
  `Description_Utilisation` text COMMENT 'Description de l''utilisation de la plante.',
  PRIMARY KEY (`ID_Utillisation`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Informations sur l''utilisation des plantes, par exemple à des fins médicinales ou culinaires.';

-- Listage des données de la table gerber_keito_deva1a_mpd_gestion_des_plantes.t_utillisation : ~3 rows (environ)
INSERT INTO `t_utillisation` (`ID_Utillisation`, `Description_Utilisation`) VALUES
	(1, 'Ornemental'),
	(2, 'Culinaire'),
	(3, 'Fruitier');

-- Listage de la structure de table gerber_keito_deva1a_mpd_gestion_des_plantes. t_exigences_de_croissance
DROP TABLE IF EXISTS `t_exigences_de_croissance`;
CREATE TABLE IF NOT EXISTS `t_exigences_de_croissance` (
  `ID_Exigence` int NOT NULL AUTO_INCREMENT COMMENT 'Identifiant de la plante.',
  `Lumière` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'Les besoins en lumière.',
  `Eau` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'Les besoins en eau',
  `Type_De_Sol` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'Le type de sol préféré.',
  PRIMARY KEY (`ID_Exigence`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Cette table détaille les conditions requises pour la croissance de chaque plante.';

-- Listage des données de la table gerber_keito_deva1a_mpd_gestion_des_plantes.t_exigences_de_croissance : ~9 rows (environ)
INSERT INTO `t_exigences_de_croissance` (`ID_Exigence`, `Lumière`, `Eau`, `Type_De_Sol`) VALUES
	(1, 'Mi-ombre', 'Modérée', 'Humide'),
	(2, 'Plein soleil à mi-ombre', 'Modérée', 'Bien drainé'),
	(3, 'Mi-ombre à ombre', 'Modérée', 'Riche'),
	(4, 'Ombre à mi-ombre', 'Modérée', 'Riche'),
	(5, 'Plein soleil', 'Modérée', 'Riche'),
	(6, 'Mi-ombre', 'Modérée', 'Riche'),
	(7, 'Plein soleil', 'Modérée', 'Fertile'),
	(8, 'Mi-ombre', 'Abondante', 'Humide'),
	(9, 'Plein soleil', 'Modérée à humide', 'Bien drainé'),
	(10, 'Plein soleil', 'Abondante', 'Riche'),
	(11, 'Plein soleil à mi-ombre', 'Modérée', 'Acide'),
	(12, 'Plein soleil', 'Faible', 'Pauvre'),
	(13, 'Plein soleil à mi-ombre', 'Abondante', 'Riche'),
	(14, 'Plein soleil', 'Aquatique', 'Limoneux'),
	(15, 'Plein soleil à mi-ombre', 'Modérée', 'Varié'),
	(16, 'Plein solei', 'Modérée', 'Ordinaire'),
	(17, 'Plein soleil à mi-ombre', 'Modérée', 'Ordinaire'),
	(18, 'Plein soleil à mi-ombre', 'Modérée', 'Humide'),
	(19, 'Ombre à mi-ombre', 'Abondante', 'Humide');

-- Listage de la structure de table gerber_keito_deva1a_mpd_gestion_des_plantes. t_habitat
DROP TABLE IF EXISTS `t_habitat`;
CREATE TABLE IF NOT EXISTS `t_habitat` (
  `ID_Habitat` int NOT NULL AUTO_INCREMENT COMMENT 'Un identifiant unique pour chaque habitat.',
  `Description` text COMMENT 'Description de l''habitat',
  PRIMARY KEY (`ID_Habitat`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Cette table contient des informations sur l''habitat naturel des plantes.';

-- Listage des données de la table gerber_keito_deva1a_mpd_gestion_des_plantes.t_habitat : ~9 rows (environ)
INSERT INTO `t_habitat` (`ID_Habitat`, `Description`) VALUES
	(1, 'Forêts'),
	(2, 'Prairies'),
	(3, 'Sous-bois'),
	(4, 'Jardins'),
	(5, 'Collines rocheuses'),
	(6, 'Forêts tropicales'),
	(7, 'Eaux douces stagnantes'),
	(8, 'Pelouses'),
	(9, 'Zones boisées');

-- Listage de la structure de table gerber_keito_deva1a_mpd_gestion_des_plantes. t_plantes
DROP TABLE IF EXISTS `t_plantes`;
CREATE TABLE IF NOT EXISTS `t_plantes` (
  `ID_Plante` int NOT NULL AUTO_INCREMENT COMMENT 'Un identifiant unique pour chaque plante.',
  `Nom_Commun` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'Le nom commun de la plante.',
  `Nom_Scientifique` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'Le nom scientifique de la plante.',
  `Famille` varchar(100) DEFAULT NULL COMMENT 'La famille botanique à laquelle appartient la plante.',
  PRIMARY KEY (`ID_Plante`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Cette table contiendra les informations de base sur chaque plante.';

-- Listage des données de la table gerber_keito_deva1a_mpd_gestion_des_plantes.t_plantes : ~33 rows (environ)
INSERT INTO `t_plantes` (`ID_Plante`, `Nom_Commun`, `Nom_Scientifique`, `Famille`) VALUES
	(1, 'Perce-neige', 'Galanthus nivalis', 'Amaryllidaceae'),
	(2, 'Crocus', 'Crocus sativus', 'Iridaceae'),
	(3, 'Hépatique', '	Hepatica nobilis', 'Ranunculaceae'),
	(4, 'Violette', 'Viola odorata', 'Violaceae'),
	(5, 'Primevère', 'Primula vulgaris', 'Primulaceae'),
	(6, 'Jonquille', '	Narcissus pseudonarcissus', 'Amaryllidaceae'),
	(7, 'Narcisse', 'Narcissus spp.', 'Amaryllidaceae'),
	(8, 'Pervenche', 'Vinca minor', 'Apocynaceae'),
	(9, 'Scille', 'Scilla spp.', '	Asparagaceae'),
	(10, 'Pivoine', 'Paeonia spp.', '	Paeoniaceae'),
	(11, 'Cœur-de-Marie', 'Dicentra spectabilis', 'Papaveraceae'),
	(12, 'Lilas', 'Syringa vulgaris', 'Oleaceae'),
	(13, 'Hortensia', 'Hydrangea macrophylla', 'Hydrangeaceae'),
	(14, 'Iris', 'Iris spp.', 'Iridaceae'),
	(15, 'Les roses', 'Rosa spp.', 'Rosaceae'),
	(16, 'Fraise Sauvage', 'Fragaria vesca', '	Rosaceae'),
	(17, 'Lavande', '	Lavandula', 'Lamiaceae'),
	(18, 'Sapin', 'Abies	', 'Pinaceae'),
	(19, 'Arbre de Judée	', 'Cercis siliquastrum	', 'Fabaceae'),
	(20, 'Saxifrage', 'Saxifraga', 'Saxifragaceae'),
	(21, 'Corbeille d\'Argent	', 'Iberis sempervirens	', 'Brassicaceae'),
	(22, 'Chrysanthème', 'Chrysanthemum', 'Asteraceae'),
	(23, 'Bambou', 'Bambusoideae', 'Poaceae'),
	(24, 'Nénuphar', 'Nymphaea', 'Nymphaeaceae'),
	(25, 'Pissenlit', 'Taraxacum', 'Asteraceae'),
	(26, 'Pâquerette', 'Bellis perennis	', 'Asteraceae'),
	(27, 'Muscari', 'Muscari', 'Asparagaceae'),
	(28, 'Muguet	', 'Convallaria majalis	', 'Asparagaceae'),
	(29, 'Erable', 'Acer', 'Sapindaceae'),
	(30, 'Rose de Noël	', 'Helleborus', 'Ranunculaceae'),
	(31, 'Cerisier	', 'Prunus', 'Rosaceae'),
	(32, 'Fougère', 'Pteridium aquilinum	', 'Dennstaedtiaceae'),
	(33, 'Weigela', 'Weigela', 'Caprifoliaceae');

-- Listage de la structure de table gerber_keito_deva1a_mpd_gestion_des_plantes. t_plantes_exigence_de_croissance
DROP TABLE IF EXISTS `t_plantes_exigence_de_croissance`;
CREATE TABLE IF NOT EXISTS `t_plantes_exigence_de_croissance` (
  `ID_Plantes_Exigence_De_Coissance` int NOT NULL AUTO_INCREMENT,
  `FK_Plantes_Exigence` int DEFAULT NULL,
  `FK_Exigence_Plantes` int DEFAULT NULL,
  PRIMARY KEY (`ID_Plantes_Exigence_De_Coissance`),
  KEY `FK_t_plantes_exigence_de_croissance_t_plantes` (`FK_Plantes_Exigence`) USING BTREE,
  KEY `FK_t_plantes_exigence_de_croissance_t_exigences_de_croissance` (`FK_Exigence_Plantes`) USING BTREE,
  CONSTRAINT `FK_t_plantes_exigence_de_croissance_t_exigences_de_croissance` FOREIGN KEY (`FK_Exigence_Plantes`) REFERENCES `t_exigences_de_croissance` (`ID_Exigence`),
  CONSTRAINT `FK_t_plantes_exigence_de_croissance_t_plantes` FOREIGN KEY (`FK_Plantes_Exigence`) REFERENCES `t_plantes` (`ID_Plante`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table gerber_keito_deva1a_mpd_gestion_des_plantes.t_plantes_exigence_de_croissance : ~32 rows (environ)
INSERT INTO `t_plantes_exigence_de_croissance` (`ID_Plantes_Exigence_De_Coissance`, `FK_Plantes_Exigence`, `FK_Exigence_Plantes`) VALUES
	(1, 1, 1),
	(2, 2, 2),
	(3, 3, 1),
	(4, 4, 1),
	(5, 5, 3),
	(6, 6, 2),
	(7, 7, 2),
	(8, 8, 4),
	(9, 9, 2),
	(10, 10, 5),
	(11, 11, 6),
	(12, 12, 7),
	(13, 13, 8),
	(14, 14, 9),
	(15, 15, 10),
	(16, 16, 11),
	(17, 17, 2),
	(18, 18, 2),
	(19, 19, 12),
	(20, 20, 5),
	(21, 21, 13),
	(22, 22, 14),
	(23, 23, 15),
	(24, 24, 16),
	(25, 25, 17),
	(26, 26, 2),
	(27, 27, 3),
	(28, 28, 18),
	(29, 29, 6),
	(30, 30, 7),
	(31, 31, 7),
	(32, 32, 19);

-- Listage de la structure de table gerber_keito_deva1a_mpd_gestion_des_plantes. t_plantes_habitat
DROP TABLE IF EXISTS `t_plantes_habitat`;
CREATE TABLE IF NOT EXISTS `t_plantes_habitat` (
  `ID_Plantes_Habitat` int NOT NULL AUTO_INCREMENT,
  `FK_Habitat_Plantes` int DEFAULT NULL,
  `FK_Plantes_Habitat` int DEFAULT NULL,
  PRIMARY KEY (`ID_Plantes_Habitat`),
  KEY `FK_Plantes_Habitat` (`FK_Habitat_Plantes`) USING BTREE,
  KEY `FK_Habitat_Plantes` (`FK_Plantes_Habitat`) USING BTREE,
  CONSTRAINT `FK_t_plantes_habitat_t_habitat` FOREIGN KEY (`FK_Habitat_Plantes`) REFERENCES `t_habitat` (`ID_Habitat`),
  CONSTRAINT `FK_t_plantes_habitat_t_plantes` FOREIGN KEY (`FK_Plantes_Habitat`) REFERENCES `t_plantes` (`ID_Plante`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table gerber_keito_deva1a_mpd_gestion_des_plantes.t_plantes_habitat : ~0 rows (environ)
INSERT INTO `t_plantes_habitat` (`ID_Plantes_Habitat`, `FK_Habitat_Plantes`, `FK_Plantes_Habitat`) VALUES
	(1, 1, 1),
	(2, 4, 2),
	(3, 3, 3),
	(4, 1, 4),
	(5, 1, 5),
	(6, 2, 6),
	(7, 1, 7),
	(8, 1, 8),
	(9, 3, 9),
	(10, 4, 10),
	(11, 4, 11),
	(12, 4, 12),
	(13, 4, 13),
	(14, 4, 14),
	(15, 4, 15),
	(16, 2, 16),
	(17, 4, 17),
	(18, 4, 18),
	(19, 9, 19),
	(20, 5, 20),
	(21, 4, 21),
	(22, 4, 22),
	(23, 6, 23),
	(24, 7, 24),
	(25, 8, 25),
	(26, 8, 26),
	(27, 4, 27),
	(28, 1, 28),
	(29, 1, 29),
	(30, 4, 30),
	(31, 4, 31),
	(32, 1, 32);

-- Listage de la structure de table gerber_keito_deva1a_mpd_gestion_des_plantes. t_plantes_utilisation
DROP TABLE IF EXISTS `t_plantes_utilisation`;
CREATE TABLE IF NOT EXISTS `t_plantes_utilisation` (
  `ID_Plantes_Utilisation` int NOT NULL AUTO_INCREMENT,
  `FK_Utilisation_Plantes` int DEFAULT NULL,
  `FK_Plantes_Utilisation` int DEFAULT NULL,
  PRIMARY KEY (`ID_Plantes_Utilisation`),
  KEY `FK_Utilisation_Plantes` (`FK_Plantes_Utilisation`) USING BTREE,
  KEY `FK_Plantes_Utilisation` (`FK_Utilisation_Plantes`) USING BTREE,
  CONSTRAINT `FK_t_plantes_utilisation_t_plantes` FOREIGN KEY (`FK_Plantes_Utilisation`) REFERENCES `t_plantes` (`ID_Plante`),
  CONSTRAINT `FK_t_plantes_utilisation_t_utillisation` FOREIGN KEY (`FK_Utilisation_Plantes`) REFERENCES `t_utillisation` (`ID_Utillisation`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table gerber_keito_deva1a_mpd_gestion_des_plantes.t_plantes_utilisation : ~0 rows (environ)
INSERT INTO `t_plantes_utilisation` (`ID_Plantes_Utilisation`, `FK_Utilisation_Plantes`, `FK_Plantes_Utilisation`) VALUES
	(1, 1, 1),
	(2, 1, 2),
	(3, 1, 3),
	(4, 1, 4),
	(5, 1, 5),
	(6, 1, 6),
	(7, 1, 7),
	(8, 1, 8),
	(9, 1, 9),
	(10, 1, 10),
	(11, 1, 11),
	(12, 1, 12),
	(13, 1, 13),
	(14, 1, 14),
	(15, 1, 15),
	(16, 1, 16),
	(17, 1, 17),
	(18, 1, 18),
	(19, 1, 19),
	(20, 1, 20),
	(21, 1, 21),
	(22, 1, 22),
	(23, 1, 23),
	(24, 2, 24),
	(25, 1, 25),
	(26, 1, 26),
	(27, 1, 27),
	(28, 1, 28),
	(29, 1, 29),
	(30, 1, 30),
	(31, 3, 31),
	(32, 3, 32),
	(33, 1, 33);


/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT='utf8mb4' */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
