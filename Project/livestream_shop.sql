-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema livestream_shop
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `livestream_shop` ;

-- -----------------------------------------------------
-- Schema livestream_shop
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `livestream_shop` DEFAULT CHARACTER SET utf8 ;
USE `livestream_shop` ;

-- -----------------------------------------------------
-- Table `livestream_shop`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `livestream_shop`.`users` ;

CREATE TABLE IF NOT EXISTS `livestream_shop`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `pw` VARCHAR(255) NULL,
  `confirm_pw` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `livestream_shop`.`cards`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `livestream_shop`.`cards` ;

CREATE TABLE IF NOT EXISTS `livestream_shop`.`cards` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(155) NULL,
  `set` VARCHAR(155) NULL,
  `market_price` INT NULL,
  `rarity` VARCHAR(155) NULL,
  `num_of_copies` INT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `update_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
