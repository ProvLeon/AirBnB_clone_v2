-- Prepares a MySQL server

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER 
  IF NOT EXISTS 'hbnb_dev'@'localhost' 
  IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant usage on all databases to the user
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';

-- Grant all privileges on hbnb_dev_db to the user
GRANT ALL PRIVILEGES 
  ON `hbnb_dev_db`.* 
  TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to the user
GRANT SELECT 
  ON `performance_schema`.* 
  TO 'hbnb_dev'@'localhost';

-- FLUSH applies all the privilege changes instantly
FLUSH PRIVILEGES;
