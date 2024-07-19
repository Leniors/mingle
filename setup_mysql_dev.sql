-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS mingle_db;
CREATE USER IF NOT EXISTS 'mingle_dev'@'localhost' IDENTIFIED BY 'Mingle-m1';
GRANT ALL PRIVILEGES ON `mingle_db`.* TO 'mingle_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'mingle_dev'@'localhost';
FLUSH PRIVILEGES;
