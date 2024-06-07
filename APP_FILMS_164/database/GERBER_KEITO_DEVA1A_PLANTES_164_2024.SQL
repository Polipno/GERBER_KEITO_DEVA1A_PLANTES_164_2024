-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.30 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour gerber_keito_deva1a_plantes_164_2024
DROP DATABASE IF EXISTS `gerber_keito_deva1a_plantes_164_2024`;
CREATE DATABASE IF NOT EXISTS `gerber_keito_deva1a_plantes_164_2024` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `gerber_keito_deva1a_plantes_164_2024`;

-- Listage de la structure de table gerber_keito_deva1a_plantes_164_2024. t_exigences_de_croissance
DROP TABLE IF EXISTS `t_exigences_de_croissance`;
CREATE TABLE IF NOT EXISTS `t_exigences_de_croissance` (
  `ID_Exigence` int NOT NULL AUTO_INCREMENT COMMENT 'Identifiant de la plante.',
  `Lumière` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'Les besoins en lumière.',
  `Eau` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'Les besoins en eau',
  `Type_De_Sol` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'Le type de sol préféré.',
  PRIMARY KEY (`ID_Exigence`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Cette table détaille les conditions requises pour la croissance de chaque plante.';

-- Listage des données de la table gerber_keito_deva1a_plantes_164_2024.t_exigences_de_croissance : ~19 rows (environ)
INSERT INTO `t_exigences_de_croissance` (`ID_Exigence`, `Lumière`, `Eau`, `Type_De_Sol`) VALUES
	(2, 'plein soleil à mi-ombre', 'modérée', 'bien drainé'),
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
	(19, 'Ombre à mi-ombre', 'Abondante', 'Humide'),
	(23, 'mi-ombre', 'modérée', 'humide');

-- Listage de la structure de table gerber_keito_deva1a_plantes_164_2024. t_habitat
DROP TABLE IF EXISTS `t_habitat`;
CREATE TABLE IF NOT EXISTS `t_habitat` (
  `ID_Habitat` int NOT NULL AUTO_INCREMENT COMMENT 'Un identifiant unique pour chaque habitat.',
  `Description` text COMMENT 'Description de l''habitat',
  PRIMARY KEY (`ID_Habitat`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Cette table contient des informations sur l''habitat naturel des plantes.';

-- Listage des données de la table gerber_keito_deva1a_plantes_164_2024.t_habitat : ~8 rows (environ)
INSERT INTO `t_habitat` (`ID_Habitat`, `Description`) VALUES
	(1, 'forêts'),
	(2, 'prairies'),
	(3, 'Sous-bois'),
	(4, 'Jardins'),
	(5, 'Collines rocheuses'),
	(6, 'Forêts tropicales'),
	(7, 'Eaux douces stagnantes'),
	(8, 'Pelouses');

-- Listage de la structure de table gerber_keito_deva1a_plantes_164_2024. t_plantes
DROP TABLE IF EXISTS `t_plantes`;
CREATE TABLE IF NOT EXISTS `t_plantes` (
  `ID_Plante` int NOT NULL AUTO_INCREMENT COMMENT 'Un identifiant unique pour chaque plante.',
  `Nom_Commun` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'Le nom commun de la plante.',
  `Nom_Scientifique` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'Le nom scientifique de la plante.',
  `Famille` varchar(100) DEFAULT NULL COMMENT 'La famille botanique à laquelle appartient la plante.',
  PRIMARY KEY (`ID_Plante`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Cette table contiendra les informations de base sur chaque plante.';

-- Listage des données de la table gerber_keito_deva1a_plantes_164_2024.t_plantes : ~49 rows (environ)
INSERT INTO `t_plantes` (`ID_Plante`, `Nom_Commun`, `Nom_Scientifique`, `Famille`) VALUES
	(1, 'physocarpus', 'physocarpus opulifolius', 'rosaceae'),
	(2, 'crocus', 'crocus sativus', 'iridaceae'),
	(3, 'hépatique', 'hepatica nobilis', 'ranunculaceae'),
	(4, 'violette', 'viola odorata', 'violaceae'),
	(5, 'Primevère', 'Primula vulgaris', 'Primulaceae'),
	(6, 'jonquille', '	narcissus pseudonarcissus', 'amaryllidaceae'),
	(7, 'Narcisse', 'Narcissus spp.', 'Amaryllidaceae'),
	(8, 'Pervenche', 'Vinca minor', 'Apocynaceae'),
	(9, 'Scille', 'Scilla spp.', '	Asparagaceae'),
	(10, 'Pivoine', 'Paeonia spp.', '	Paeoniaceae'),
	(11, 'cœur-de-marie', 'dicentra spectabilis', 'papaveraceae'),
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
	(33, 'Weigela', 'Weigela', 'Caprifoliaceae'),
	(35, 'gaillarde', 'gaillardia', 'asteraceae'),
	(36, 'lagerstroemia', 'lagerstroemia indica', 'lythraceae'),
	(37, 'campanule', 'campanula', 'campanulaceae'),
	(38, 'orchidée', 'orchidaceae', 'orchidaceae'),
	(39, 'lupin', 'lupinus', 'fabaceae'),
	(40, 'bouton d\'or', 'ranunculus acris', 'ranunculaceae'),
	(41, 'marguerite', 'leucanthemum vulgare', 'asteraceae'),
	(42, 'astilbe', 'astilbe', 'saxifragaceae'),
	(43, 'fingerhut', 'digitalis purpurea', 'plantaginaceae'),
	(44, 'salvia', 'salvia', 'lamiaceae'),
	(45, 'raisiner', 'viburnum opulus', 'adoxaceae'),
	(46, 'anémone', 'anemone nemorosa', 'ranunculaceae'),
	(47, 'phlox', 'phlox', 'polemoniaceae'),
	(48, 'oeillet', 'dianthus', 'caryophyllaceae'),
	(49, 'forsythia', 'forsythia', 'oleaceae'),
	(51, 'pommier', 'malus domestica', 'rosaceae'),
	(62, 'fougère', 'pteridophyta', 'dryopteridaceae');

-- Listage de la structure de table gerber_keito_deva1a_plantes_164_2024. t_plantes_exigence_de_croissance
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
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table gerber_keito_deva1a_plantes_164_2024.t_plantes_exigence_de_croissance : ~48 rows (environ)
INSERT INTO `t_plantes_exigence_de_croissance` (`ID_Plantes_Exigence_De_Coissance`, `FK_Plantes_Exigence`, `FK_Exigence_Plantes`) VALUES
	(2, 2, 2),
	(5, 5, 3),
	(6, 6, 2),
	(7, 7, 2),
	(8, 8, 3),
	(9, 9, 2),
	(10, 10, 5),
	(11, 11, 6),
	(12, 12, 7),
	(13, 13, 8),
	(14, 14, 9),
	(15, 15, 10),
	(16, 16, 2),
	(17, 17, 2),
	(18, 18, 2),
	(19, 19, 12),
	(20, 20, 5),
	(21, 21, 13),
	(22, 22, 14),
	(23, 23, 15),
	(25, 25, 17),
	(26, 26, 2),
	(27, 27, 3),
	(28, 28, 18),
	(29, 29, 6),
	(30, 30, 7),
	(31, 31, 8),
	(42, 62, 17),
	(44, 3, 23),
	(45, 4, 23),
	(46, 33, 2),
	(47, 35, 5),
	(48, 36, 9),
	(49, 37, 3),
	(50, 38, 8),
	(51, 39, 2),
	(52, 40, 8),
	(53, 41, 2),
	(54, 42, 8),
	(55, 43, 6),
	(56, 44, 2),
	(57, 45, 8),
	(58, 46, 3),
	(59, 47, 2),
	(60, 48, 5),
	(61, 49, 2),
	(62, 51, 7),
	(64, 24, 14);

-- Listage de la structure de table gerber_keito_deva1a_plantes_164_2024. t_plantes_habitat
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
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table gerber_keito_deva1a_plantes_164_2024.t_plantes_habitat : ~50 rows (environ)
INSERT INTO `t_plantes_habitat` (`ID_Plantes_Habitat`, `FK_Habitat_Plantes`, `FK_Plantes_Habitat`) VALUES
	(1, 3, 1),
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
	(18, 1, 18),
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
	(35, 2, 35),
	(37, 2, 37),
	(38, 1, 38),
	(39, 2, 39),
	(40, 2, 40),
	(51, 1, 62),
	(52, 3, 19),
	(53, 4, 33),
	(54, 4, 36),
	(55, 2, 41),
	(56, 3, 42),
	(57, 1, 43),
	(58, 4, 44),
	(59, 1, 45),
	(60, 3, 46),
	(61, 4, 47),
	(62, 5, 48),
	(63, 4, 49),
	(64, 4, 51),
	(69, 3, 33);

-- Listage de la structure de table gerber_keito_deva1a_plantes_164_2024. t_plantes_utilisation
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
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table gerber_keito_deva1a_plantes_164_2024.t_plantes_utilisation : ~49 rows (environ)
INSERT INTO `t_plantes_utilisation` (`ID_Plantes_Utilisation`, `FK_Utilisation_Plantes`, `FK_Plantes_Utilisation`) VALUES
	(24, 2, 24),
	(31, 3, 31),
	(55, 42, 62),
	(56, 42, 1),
	(57, 42, 2),
	(58, 42, 3),
	(59, 42, 4),
	(60, 42, 5),
	(61, 42, 6),
	(62, 42, 7),
	(63, 42, 8),
	(64, 42, 9),
	(65, 42, 10),
	(66, 42, 11),
	(67, 42, 12),
	(68, 42, 13),
	(69, 42, 14),
	(70, 42, 15),
	(71, 42, 16),
	(72, 42, 17),
	(73, 42, 18),
	(74, 42, 19),
	(75, 42, 20),
	(76, 42, 21),
	(77, 42, 22),
	(78, 42, 23),
	(79, 42, 25),
	(80, 42, 26),
	(81, 42, 27),
	(82, 42, 28),
	(83, 42, 29),
	(84, 42, 30),
	(86, 42, 33),
	(88, 42, 35),
	(89, 42, 36),
	(90, 42, 37),
	(91, 42, 38),
	(92, 42, 39),
	(93, 42, 40),
	(94, 42, 41),
	(95, 42, 42),
	(96, 42, 43),
	(97, 2, 44),
	(98, 42, 45),
	(99, 42, 46),
	(100, 42, 47),
	(101, 42, 48),
	(102, 42, 49),
	(103, 3, 51);

-- Listage de la structure de table gerber_keito_deva1a_plantes_164_2024. t_utillisation
DROP TABLE IF EXISTS `t_utillisation`;
CREATE TABLE IF NOT EXISTS `t_utillisation` (
  `ID_Utillisation` int NOT NULL AUTO_INCREMENT COMMENT 'Un identifiant unique pour chaque utilisation.',
  `Description_Utilisation` text COMMENT 'Description de l''utilisation de la plante.',
  PRIMARY KEY (`ID_Utillisation`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Informations sur l''utilisation des plantes, par exemple à des fins médicinales ou culinaires.';

-- Listage des données de la table gerber_keito_deva1a_plantes_164_2024.t_utillisation : ~3 rows (environ)
INSERT INTO `t_utillisation` (`ID_Utillisation`, `Description_Utilisation`) VALUES
	(2, 'Culinaire'),
	(3, 'fruitier'),
	(42, 'decoratif');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
