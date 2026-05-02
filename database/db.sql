CREATE DATABASE study_planner;

USE study_planner;

CREATE TABLE subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    difficulty INT,
    hours INT
);