-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

-- Create database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Create table in specific database
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
  -- id should increment with every INSERT an not null
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(256) NOT NULL,
  -- Set id as Primary Key 
  PRIMARY KEY (`id`)
);
