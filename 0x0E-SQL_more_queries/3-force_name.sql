-- Script that creates the MySQL server user user_0d_1.

-- Create table
CREATE TABLE IF NOT EXISTS `force_name` (
  `id` INT, 
  -- NOT NULL, Constrain column value to be not NULL --
  `name` VARCHAR(256) NOT NULL
);
