SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cars_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `cars_db` ;

-- -----------------------------------------------------
-- Schema cars_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cars_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci ;
USE `cars_db` ;

-- -----------------------------------------------------
-- Table `cars_db`.`brands`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cars_db`.`brands` ;

CREATE TABLE IF NOT EXISTS `cars_db`.`brands` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NOT NULL,
  `country` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cars_db`.`cars`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cars_db`.`cars` ;

CREATE TABLE IF NOT EXISTS `cars_db`.`cars` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `model` VARCHAR(100) NOT NULL,
  `price` INT NOT NULL,
  `brand_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_car_brand_idx` (`brand_id` ASC) VISIBLE,
  CONSTRAINT `fk_car_brand`
    FOREIGN KEY (`brand_id`)
    REFERENCES `cars_db`.`brands` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cars_db`.`colors`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cars_db`.`colors` ;

CREATE TABLE IF NOT EXISTS `cars_db`.`colors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cars_db`.`car_has_color`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cars_db`.`car_has_color` ;

CREATE TABLE IF NOT EXISTS `cars_db`.`car_has_color` (
  `car_id` INT NOT NULL,
  `color_id` INT NOT NULL,
  PRIMARY KEY (`car_id`, `color_id`),
  INDEX `fk_car_has_color_color1_idx` (`color_id` ASC) VISIBLE,
  INDEX `fk_car_has_color_car1_idx` (`car_id` ASC) VISIBLE,
  CONSTRAINT `fk_car_has_color_car1`
    FOREIGN KEY (`car_id`)
    REFERENCES `cars_db`.`cars` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_car_has_color_color1`
    FOREIGN KEY (`color_id`)
    REFERENCES `cars_db`.`colors` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
