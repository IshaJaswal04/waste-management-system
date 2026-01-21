-- Create database
CREATE DATABASE IF NOT EXISTS waste_management;
USE waste_management;

-- Create bins Table
CREATE TABLE IF NOT EXISTS bins(
    id INT AUTO_INCREMENT PRIMARY KEY,
    area VARCHAR(50) NOT NULL,
    bin_id VARCHAR(20) NOT NULL UNIQUE,
    status ENUM('EMPTY','HALF','FULL') DEFAULT 'EMPTY',
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insert Sample
INSERT INTO bins (area,bin_id,status) VALUES
('West Side', 'DL-WS-001','EMPTY'),
('West Side', 'DL-WS-002','HALF'),
('West Side', 'DL-WS-003','FULL'),
('North Region', 'DL-NR-001','EMPTY'),
('North Region', 'DL-NR-002','HALF'),
('East Zone', 'DL-EZ-001','FULL');

CREATE TABLE bin_collections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bin_id VARCHAR(50),
    collected_by VARCHAR(50),   -- worker name or ID
    collected_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
