DROP DATABASE IF EXISTS revou_review;
CREATE DATABASE revou_user_review;
USE revou_user_review;


CREATE TABLE user (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(191) NOT NULL,
    username VARCHAR(191) NOT NULL,
    email VARCHAR(191) NOT NULL,
	password VARCHAR(191) NOT NULL, 
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_review (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(191) NOT NULL,
    username VARCHAR(191) NOT NULL,
    email VARCHAR(191) NOT NULL,
    review_content TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product (
	id INTEGER PRIMARY KEY auto_increment,
    name VARCHAR(100) NOT NULL,
    price INTEGER NOT NULL,
    description TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_review (
	id INTEGER PRIMARY KEY auto_increment,
    product_id INTEGER NOT NULL,
    email VARCHAR(100) NOT NULL,
    rating INTEGER NOT NULL,
    review_content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

