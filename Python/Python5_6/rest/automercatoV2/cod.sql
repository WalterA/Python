CREATE TABLE automobili (
    id SERIAL PRIMARY KEY,
    marca VARCHAR(100) NOT NULL,
    filiale VARCHAR(100) NOT NULL,
    id_accessori INT REFERENCES accessori(id) ON DELETE SET NULL,
    disponibile BOOLEAN DEFAULT TRUE NOT NULL
);
CREATE TABLE motociclette (
    id SERIAL PRIMARY KEY,
    marca VARCHAR(100) NOT NULL,
    filiale VARCHAR(100) NOT NULL,
    id_accessori INT REFERENCES accessori(id) ON DELETE SET NULL,
    disponibile BOOLEAN DEFAULT TRUE NOT NULL
);
CREATE TABLE vendite (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(100) NOT NULL,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
CREATE TABLE accessori (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(100) NOT NULL,
    descrizione TEXT
);
INSERT INTO accessori (tipo, descrizione) VALUES
('automobili', 'Kit di pulizia esterno per auto'),
('automobili', 'Copertura per esterni per auto'),
('motociclette', 'Guanti da moto in pelle'),
('motociclette', 'Coprisedile impermeabile per moto');
INSERT INTO automobili (marca, filiale, id_accessori, disponibile) VALUES
('Volkswagen', 'Roma', 1, TRUE),  -- Kit di pulizia esterno per auto
('Ford', 'Milano', 2, FALSE),     -- Copertura per esterni per auto
('Alfa Romeo', 'Torino', 1, TRUE), -- Kit di pulizia esterno per auto
('BMW', 'Roma', 2, TRUE);         -- Copertura per esterni per auto
INSERT INTO motociclette (marca, filiale, id_accessori, disponibile) VALUES
('Yamaha', 'Roma', 3, TRUE),  -- Guanti da moto in pelle
('Harley-Davidson', 'Milano', 4, FALSE), -- Coprisedile impermeabile per moto
('Ducati', 'Torino', 3, TRUE),  -- Guanti da moto in pelle
('Kawasaki', 'Roma', 4, TRUE);  -- Coprisedile impermeabile per moto
INSERT INTO vendite (tipo, data) VALUES
('automobile', '2024-11-01 10:00:00'),
('motociclette', '2024-11-05 15:30:00'),
('automobile', '2024-11-10 09:45:00'),
('motociclette', '2024-11-12 16:00:00');
