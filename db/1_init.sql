CREATE DATABASE IF NOT EXISTS eventapp;
CREATE DATABASE IF NOT EXISTS todoapp;
CREATE DATABASE IF NOT EXISTS portfolioapp;
CREATE DATABASE IF NOT EXISTS blogapp;

CREATE USER IF NOT EXISTS 'eventappuser'@'%' IDENTIFIED BY 'pass123';
CREATE USER IF NOT EXISTS 'todoappuser'@'%' IDENTIFIED BY 'pass123';
CREATE USER IF NOT EXISTS 'portfolioappuser'@'%' IDENTIFIED BY 'pass123';
CREATE USER IF NOT EXISTS 'blogappuser'@'%' IDENTIFIED BY 'pass123';

GRANT ALL PRIVILEGES ON eventapp.* TO 'eventappuser'@'%';
GRANT ALL PRIVILEGES ON todoapp.* TO 'todoappuser'@'%';
GRANT ALL PRIVILEGES ON portfolioapp.* TO 'portfolioappuser'@'%';
GRANT ALL PRIVILEGES ON blogapp.* TO 'blogappuser'@'%';

FLUSH PRIVILEGES;

