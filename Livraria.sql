
-- -----------------------------------------------------
-- Schema Livraria
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Livraria` ;

-- -----------------------------------------------------
-- Schema Livraria
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Livraria` DEFAULT CHARACTER SET utf8 ;
USE `Livraria` ;

-- -----------------------------------------------------
-- Table `Livraria`.`Livros`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Livraria`.`Livros` ;

CREATE TABLE IF NOT EXISTS `Livraria`.`Livros` (
  `idLivros` INT NOT NULL AUTO_INCREMENT,
  `Nome_Livro` VARCHAR(255) NOT NULL,
  `Gênero` VARCHAR(255) NOT NULL,
  `Ano_Publicação` VARCHAR(255) NOT NULL,
  `Valor_livro` DECIMAL NOT NULL,
  PRIMARY KEY (`idLivros`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Livraria`.`Autores`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Livraria`.`Autores` ;

CREATE TABLE IF NOT EXISTS `Livraria`.`Autores` (
  `idAutores` INT NOT NULL,
  `Nome_Autor` VARCHAR(255) NOT NULL,
  `Nacionalidade_Autor` VARCHAR(255) NOT NULL,
  `Nascimento_Autor` YEAR(4) NOT NULL,
  `Falecimento_Autor` YEAR(4) NOT NULL,
  PRIMARY KEY (`idAutores`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Livraria`.`Editora`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Livraria`.`Editora` ;

CREATE TABLE IF NOT EXISTS `Livraria`.`Editora` (
  `idEditora` INT NOT NULL,
  `Nome_Editora` VARCHAR(255) NOT NULL,
  `Fundação_Editora` YEAR(4) NOT NULL,
  `Num_Selos` INT NOT NULL,
  PRIMARY KEY (`idEditora`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Livraria`.`Publicados`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Livraria`.`Publicados` ;

CREATE TABLE IF NOT EXISTS `Livraria`.`Publicados` (
  `idPublicados` INT NOT NULL AUTO_INCREMENT,
  `fk_Livro` INT NOT NULL,
  `fk_Autor` INT NOT NULL,
  `fk_Editora` INT NOT NULL,
  PRIMARY KEY (`idPublicados`),
  INDEX `fk_Livro_idx` (`fk_Livro` ASC) VISIBLE,
  INDEX `fk_Autor_idx` (`fk_Autor` ASC) VISIBLE,
  INDEX `fk_Editora_idx` (`fk_Editora` ASC) VISIBLE,
  CONSTRAINT `fk_Livro`
    FOREIGN KEY (`fk_Livro`)
    REFERENCES `Livraria`.`Livros` (`idLivros`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Autor`
    FOREIGN KEY (`fk_Autor`)
    REFERENCES `Livraria`.`Autores` (`idAutores`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Editora`
    FOREIGN KEY (`fk_Editora`)
    REFERENCES `Livraria`.`Editora` (`idEditora`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
