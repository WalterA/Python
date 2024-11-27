-- Tabella Filiale
CREATE TABLE filiale (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Tabella Mezzi
CREATE TABLE mezzi (
    id SERIAL PRIMARY KEY,
    modello VARCHAR(100) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    magazzino INT REFERENCES filiale(id) ON DELETE SET NULL,
    disponibile BOOLEAN DEFAULT TRUE NOT NULL,
    tipo VARCHAR(20) CHECK (tipo IN ('automobili', 'motociclette')) NOT NULL
);

-- Tabella Accessori
CREATE TABLE accessori (
    id SERIAL PRIMARY KEY,
    mezzo_id INT REFERENCES mezzi(id) ON DELETE CASCADE,
    tipo VARCHAR(20) CHECK (tipo IN ('automobili', 'motociclette')) NOT NULL,
    dettagli VARCHAR(255)
);

-- Tabella Vendite
CREATE TABLE vendite (
    id SERIAL PRIMARY KEY,
    mezzo_id INT REFERENCES mezzi(id) ON DELETE CASCADE,
    filiale_id INT REFERENCES filiale(id) ON DELETE SET NULL,
    tipo VARCHAR(20) CHECK (tipo IN ('automobili', 'motociclette')) NOT NULL,
    data_vendita TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE automobili (
    id SERIAL PRIMARY KEY,
    modello VARCHAR(100) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    magazzino INT REFERENCES filiale(id) ON DELETE SET NULL,
    disponibile BOOLEAN DEFAULT TRUE NOT NULL
);
CREATE TABLE motociclette (
    id SERIAL PRIMARY KEY,
    modello VARCHAR(100) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    magazzino INT REFERENCES filiale(id) ON DELETE SET NULL,
    disponibile BOOLEAN DEFAULT TRUE NOT NULL
);


-- Inserimento Filiali
INSERT INTO filiale (nome) VALUES ('Filiale Roma'), ('Filiale Milano');

-- Inserimento Mezzi
INSERT INTO mezzi (modello, marca, magazzino, disponibile, tipo) VALUES
('Panda', 'Fiat', 1, TRUE, 'automobili'),
('Ducati Monster', 'Ducati', 2, TRUE, 'motociclette');

-- Inserimento Accessori
INSERT INTO accessori (mezzo_id, tipo, dettagli) VALUES
(1, 'automobili', 'Tappetini in gomma'),
(2, 'motociclette', 'Borse laterali');

-- Inserimento Vendite
INSERT INTO vendite (mezzo_id, filiale_id, tipo) VALUES
(1, 1, 'automobili'),
(2, 2, 'motociclette');



-- Inserimento Vendite con date diverse
INSERT INTO vendite (mezzo_id, filiale_id, tipo, data_vendita) VALUES
(1, 1, 'automobili', '2024-11-01 10:00:00'),
(2, 2, 'motociclette', '2024-11-05 15:30:00'),
(3, 3, 'automobili', '2024-11-10 09:45:00'),
(4, 1, 'motociclette', '2024-11-12 16:00:00'),
(5, 3, 'automobili', '2024-11-15 11:20:00');



-- Inserimento Vendite
INSERT INTO vendite (mezzo_id, filiale_id, tipo) VALUES
(1, 1, 'automobili'),
(2, 2, 'motociclette'),
(3, 3, 'automobili'),
(4, 1, 'motociclette'),
(5, 3, 'automobili');


-- Inserimento Accessori
INSERT INTO accessori (mezzo_id, tipo, dettagli) VALUES
(1, 'automobili', 'Kit di pulizia esterno'),
(2, 'motociclette', 'Coprisedile impermeabile'),
(3, 'automobili', 'Copertura per esterni'),
(4, 'motociclette', 'Guanti da moto in pelle'),
(5, 'automobili', 'Portapacchi per tetto');


-- Inserimento Filiali
INSERT INTO filiale (nome) VALUES 
('Filiale Roma'), 
('Filiale Milano'),
('Filiale Torino');


-- Inserimento Mezzi (automobili e motociclette)
INSERT INTO mezzi (modello, marca, magazzino, disponibile, tipo) VALUES
('Golf', 'Volkswagen', 1, TRUE, 'automobili'),
('Yamaha R1', 'Yamaha', 2, TRUE, 'motociclette'),
('Fiesta', 'Ford', 3, FALSE, 'automobili'),
('Harley-Davidson Sportster', 'Harley-Davidson', 1, TRUE, 'motociclette'),
('Alfa Romeo Giulia', 'Alfa Romeo', 3, TRUE, 'automobili');
