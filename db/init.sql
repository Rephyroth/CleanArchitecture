CREATE TABLE book(
	id_book INT GENERATED ALWAYS AS IDENTITY,
<<<<<<< HEAD
	title VARCHAR(200),
	isbn VARCHAR(200),
	author VARCHAR(200),
	publisher VARCHAR(200),
	genre VARCHAR(200),
	num_pages VARCHAR(200),
	year VARCHAR(200),
=======
	title VARCHAR(100),
	isbn VARCHAR(50),
	author VARCHAR(50),
	publisher VARCHAR(50),
	genre VARCHAR(50),
	num_pages VARCHAR(10),
	year VARCHAR(10),
>>>>>>> ed9c3e59d320a6e84707768f8cb315a73a133f18
	PRIMARY KEY (id_book)
);