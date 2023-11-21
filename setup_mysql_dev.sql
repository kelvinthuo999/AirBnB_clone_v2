#!/bin/bash

# MySQL server connection details
MYSQL_USER="root"
MYSQL_PASSWORD="your_mysql_root_password"
MYSQL_HOST="localhost"

# Database and user details
DB_NAME="hbnb_dev_db"
DB_USER="hbnb_dev"
DB_PASSWORD="hbnb_dev_pwd"

# Create the database
mysql -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" -h"${MYSQL_HOST}" -e "CREATE DATABASE IF NOT EXISTS ${DB_NAME};"

# Create the user
mysql -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" -h"${MYSQL_HOST}" -e "CREATE USER IF NOT EXISTS '${DB_USER}'@'localhost' IDENTIFIED BY '${DB_PASSWORD}';"

# Grant all privileges on the database to the user
mysql -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" -h"${MYSQL_HOST}" -e "GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO '${DB_USER}'@'localhost';"

# Grant SELECT privilege on performance_schema database to the user
mysql -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" -h"${MYSQL_HOST}" -e "GRANT SELECT ON performance_schema.* TO '${DB_USER}'@'localhost';"
