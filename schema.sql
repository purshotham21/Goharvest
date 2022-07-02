CREATE DATABASE `agriculture` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE `accounts` (
  `uuid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `sellingprices` (
  `uuid` int NOT NULL AUTO_INCREMENT,
  `crop` varchar(255) NOT NULL,
  `price` float NOT NULL,
  `priceChange` float NOT NULL,
  `direction` varchar(45) NOT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `crop_UNIQUE` (`crop`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `analytics` (
  `uuid` int NOT NULL AUTO_INCREMENT,
  `intake` longtext,
  `results` longtext,
  `userid` int NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

