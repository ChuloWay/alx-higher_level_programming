-- Script that creates the table id_not_null on your MySQL server.

-- Create table
CREATE TABLE IF NOT EXISTS `unique_id` (
  -- DEFAULT, set default value to 1 --
  `id` INT DEFAULT 1 UNIQUE,
  `name` VARCHAR(256)
);
