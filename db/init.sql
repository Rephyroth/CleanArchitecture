CREATE TABLE book(
	id_book SERIAL NOT NULL,
	title VARCHAR(100),
	isbn VARCHAR(50),
	author INTEGER(11),
	publisher INTEGER(11),
	genre VARCHAR(50),
	num_pages VARCHAR(10),
	year VARCHAR(10),
	PRIMARY KEY (id_book),
);