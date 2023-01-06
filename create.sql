CREATE TABLE Shows
(
	show_id  int NOT NULL,
	title    text   NOT NULL,
	release_year int NOT NULL,
	genre_id  int NOT NULL,
	duration  int NOT NULL,
	production_id  int NOT NULL
);
CREATE TABLE ShowScoreDate
(
	show_id   int NULL,
	last_update timestamp NULL,
	number_of_votes  int NULL,
	score   numeric NULL
);
CREATE TABLE Genres
(
	genre_id int NOT NULL,
	genre_name  text NOT NULL
);
CREATE TABLE Production
(
	production_id   int NOT NULL,
	production_name  text NOT NULL
);

ALTER TABLE Shows ADD PRIMARY KEY (show_id);
ALTER TABLE ShowScoreDate ADD PRIMARY KEY (show_id, last_update);
ALTER TABLE Genres ADD PRIMARY KEY (genre_id);
ALTER TABLE Production ADD PRIMARY KEY (production_id);


ALTER TABLE ShowScoreDate ADD CONSTRAINT FK_ShowScoreDate_Shows 
FOREIGN KEY (show_id) REFERENCES Shows (show_id);

ALTER TABLE Shows  ADD CONSTRAINT FK_Production_Shows 
FOREIGN KEY (production_id) REFERENCES Production (production_id);
ALTER TABLE Shows ADD CONSTRAINT FK_Genres_Shows 
FOREIGN KEY (genre_id) REFERENCES Genres (genre_id);