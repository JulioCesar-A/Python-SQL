DROP DATABASE IF EXISTS livraria ;
CREATE DATABASE IF NOT EXISTS livraria;
USE livraria;

-- -----------------------------------------------------
-- Table Livros
-- -----------------------------------------------------
DROP TABLE IF EXISTS Livros ;

CREATE TABLE IF NOT EXISTS Livros (
  idLivros INT NOT NULL AUTO_INCREMENT,
  Nome_Livro VARCHAR(255) NOT NULL,
  Gênero VARCHAR(255) NOT NULL,
  Ano_Publicação VARCHAR(255) NOT NULL,
  Valor_livro DECIMAL NOT NULL,
  PRIMARY KEY (idLivros))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Autores
-- -----------------------------------------------------
DROP TABLE IF EXISTS Autores ;

CREATE TABLE IF NOT EXISTS Autores (
  idAutores INT NOT NULL,
  Nome_Autor VARCHAR(255) NOT NULL,
  Nacionalidade_Autor VARCHAR(255) NOT NULL,
  Nascimento_Autor YEAR(4) NOT NULL,
  Falecimento_Autor YEAR(4) NOT NULL,
  PRIMARY KEY (idAutores))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Editora
-- -----------------------------------------------------
DROP TABLE IF EXISTS Editora ;

CREATE TABLE IF NOT EXISTS Editora (
  idEditora INT NOT NULL,
  Nome_Editora VARCHAR(255) NOT NULL,
  Fundação_Editora YEAR(4) NOT NULL,
  Num_Selos INT NOT NULL,
  PRIMARY KEY (`idEditora`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Publicados
-- -----------------------------------------------------
DROP TABLE IF EXISTS Publicados ;

CREATE TABLE IF NOT EXISTS Publicados (
  idPublicados INT NOT NULL AUTO_INCREMENT,
  fk_Livro INT NOT NULL,
  fk_Autor INT NOT NULL,
  fk_Editora INT NOT NULL,
  PRIMARY KEY (idPublicados),
  CONSTRAINT fk_Livro
    FOREIGN KEY (fk_Livro)
    REFERENCES Livros (idLivros),
  CONSTRAINT fk_Autor
    FOREIGN KEY (fk_Autor)
    REFERENCES Autores (idAutores),
  CONSTRAINT fk_Editora
    FOREIGN KEY (fk_Editora)
    REFERENCES Editora (idEditora)
)
ENGINE = InnoDB;