drop database airflow_db;
CREATE DATABASE airflow_db;

CREATE USER airflow_user WITH PASSWORD '123456';
GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow_user;
GRANT ALL ON SCHEMA public TO airflow_user;
