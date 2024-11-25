"""NOME DB AUTOMERCATO"""
"""AUTOMOBILE"""
-- Table: public.automobili

-- DROP TABLE IF EXISTS public.automobili;

CREATE TABLE IF NOT EXISTS public.automobili
(
    id integer NOT NULL DEFAULT nextval('automobili_id_seq'::regclass),
    modello character varying(50) COLLATE pg_catalog."default",
    magazzino character varying(50) COLLATE pg_catalog."default",
    disponibile boolean,
    CONSTRAINT automobili_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.automobili
    OWNER to postgres;
"""MOTOCICLETTA"""
-- Table: public.motociclette

-- DROP TABLE IF EXISTS public.motociclette;

CREATE TABLE IF NOT EXISTS public.motociclette
(
    id integer NOT NULL DEFAULT nextval('motociclette_id_seq'::regclass),
    modello character varying(50) COLLATE pg_catalog."default",
    magazzino character varying(50) COLLATE pg_catalog."default",
    disponibile boolean,
    CONSTRAINT motociclette_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.motociclette
    OWNER to postgres;

"""FILIALE"""
-- Table: public.filiale

-- DROP TABLE IF EXISTS public.filiale;

CREATE TABLE IF NOT EXISTS public.filiale
(
    id integer NOT NULL,
    filiale character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT filiale_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.filiale
    OWNER to postgres;
"""VENDITE"""
-- Table: public.vendite

-- DROP TABLE IF EXISTS public.vendite;

CREATE TABLE IF NOT EXISTS public.vendite
(
    id integer NOT NULL DEFAULT nextval('vendite_id_seq'::regclass),
    filiale character varying(50) COLLATE pg_catalog."default",
    tipo character varying(20) COLLATE pg_catalog."default",
    data_vendita date,
    CONSTRAINT vendite_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.vendite
    OWNER to postgres;