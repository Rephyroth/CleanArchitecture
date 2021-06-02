CREATE TABLE author(
	id_author INT GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(50),
	tel VARCHAR(15),
	PRIMARY KEY (id_author)
);

CREATE TABLE publisher(
	id_publisher INT GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(50),
	tel VARCHAR(15),
	address VARCHAR(100),
	PRIMARY KEY (id_publisher)
);


CREATE TABLE book(
	id_book INT GENERATED ALWAYS AS IDENTITY,
	title VARCHAR(100),
	isbn VARCHAR(50),
	author INT,
	publisher INT,
	genre VARCHAR(50),
	num_pages VARCHAR(10),
	year VARCHAR(10),
	PRIMARY KEY (id_book),
	CONSTRAINT fk_author
		FOREIGN KEY(author)
			REFERENCES author(id_author),
	CONSTRAINT fk_publisher
		FOREIGN KEY(publisher)
			REFERENCES publisher(id_publisher)
);