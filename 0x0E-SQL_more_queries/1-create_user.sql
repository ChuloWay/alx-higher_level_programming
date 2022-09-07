-- Sscript that creates the table force_name on your MySQL server.

-- Create database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

-- Create user and set password
CREATE USER IF NOT EXISTS 'user_0d_2' @'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Give user_0d_2 SELECT privilege in the database hbtn_0d_2
GRANT 
SELECT 
  ON `hbtn_0d_2`.* TO 'user_0d_2' @'localhost';

-- For changes to take effect immediatelY
FLUSH PRIVILEGES;
