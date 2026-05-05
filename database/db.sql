-- Create Database
CREATE DATABASE study_planner;

-- Select Database
USE study_planner;

-- Subjects Table (for extra data)
CREATE TABLE subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    difficulty INT,
    hours INT
);

-- Tasks Table (MAIN table used in your app)
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject VARCHAR(100),
    topic VARCHAR(255),
    difficulty INT,
    deadline DATE,
    status VARCHAR(50)
);