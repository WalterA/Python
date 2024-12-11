CREATE TABLE filiali (
    partita_iva VARCHAR(20) PRIMARY KEY,         -- Unique VAT number
    nome VARCHAR(100) NOT NULL,                  -- Branch name
    indirizzo_sede VARCHAR(255) NOT NULL,        -- Office address
    civico VARCHAR(20) NOT NULL,                 -- Civic number
    telefono VARCHAR(15)                        -- Phone number
);
CREATE TABLE case_in_vendita (
    catastale VARCHAR(20) PRIMARY KEY,           -- Unique property identifier
    indirizzo VARCHAR(255) NOT NULL,             -- Property address
    numero_civico VARCHAR(20) NOT NULL,          -- Civic number
    piano INTEGER,                               -- Floor number
    metri INTEGER,                               -- Square meters
    vani INTEGER,                                -- Number of rooms
    prezzo DECIMAL(10, 2),                       -- Sale price
    stato VARCHAR(10) CHECK (stato IN ('LIBERO', 'OCCUPATO')),  -- Property status (free/occupied)
    filiale_proponente VARCHAR(20),              -- Branch proposing the sale
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva)
);
CREATE TABLE vendite_casa (
    catastale VARCHAR(20),                       -- Property identifier
    data_vendita DATE NOT NULL,                  -- Sale date
    filiale_proponente VARCHAR(20),              -- Branch proposing the sale
    filiale_venditrice VARCHAR(20),              -- Branch selling the property
    prezzo_vendita DECIMAL(10, 2),               -- Sale price
    PRIMARY KEY (catastale, data_vendita),       -- Composite primary key (catastale, data_vendita)
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva),
    FOREIGN KEY (filiale_venditrice) REFERENCES filiali(partita_iva),
    FOREIGN KEY (catastale) REFERENCES case_in_vendita(catastale)
);
CREATE TABLE case_in_affitto (
    catastale VARCHAR(20) PRIMARY KEY,           -- Unique property identifier
    indirizzo VARCHAR(255) NOT NULL,             -- Property address
    numero_civico VARCHAR(20) NOT NULL,          -- Civic number
    tipo_affitto VARCHAR(10) CHECK (tipo_affitto IN ('PARZIALE', 'TOTALE')),  -- Type of rental (partial/full)
    bagno_personale BOOLEAN,                     -- Personal bathroom (TRUE/FALSE)
    prezzo_mensile DECIMAL(10, 2),               -- Monthly rent price
    filiale_proponente VARCHAR(20),              -- Branch proposing the rental
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva)
);
CREATE TABLE affitti_casa (
    catastale VARCHAR(20),                       -- Property identifier
    data_affitto DATE NOT NULL,                  -- Rental start date
    filiale_proponente VARCHAR(20),              -- Branch proposing the rental
    filiale_venditrice VARCHAR(20),              -- Branch managing the rental
    prezzo_affitto DECIMAL(10, 2),               -- Monthly rental price
    durata_contratto INTEGER,                    -- Contract duration (in months)
    PRIMARY KEY (catastale, data_affitto),       -- Composite primary key (catastale, data_affitto)
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva),
    FOREIGN KEY (filiale_venditrice) REFERENCES filiali(partita_iva),
    FOREIGN KEY (catastale) REFERENCES case_in_affitto(catastale)
);
