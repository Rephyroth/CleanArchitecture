CREATE TABLE book(
	id_book INT GENERATED ALWAYS AS IDENTITY,
	title VARCHAR(100),
	isbn VARCHAR(50),
	author VARCHAR(50),
	publisher VARCHAR(50),
	genre VARCHAR(50),
	num_pages VARCHAR(10),
	year VARCHAR(10),
	PRIMARY KEY (id_book),
);