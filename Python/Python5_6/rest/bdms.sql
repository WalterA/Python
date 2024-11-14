
CREATE TABLE Cittadini (
    nome VARCHAR(20) NOT NULL,
    cognome VARCHAR(20) NOT NULL,
    codice_fiscale VARCHAR(20) NOT NULL,
    PRIMARY KEY (codice_fiscale)
);

CREATE TABLE Operatori (
    id SERIAL,
    password VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);

psql -h 127.0.0.1 -U postgres postgres
