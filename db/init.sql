CREATE TABLE book(
	id_book INT GENERATED ALWAYS AS IDENTITY,
	title VARCHAR(200),
	isbn VARCHAR(200),
	author VARCHAR(200),
	publisher VARCHAR(200),
	genre VARCHAR(200),
	num_pages VARCHAR(200),
	year VARCHAR(200),
	PRIMARY KEY (id_book)
);