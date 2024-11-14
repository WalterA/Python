-- Table: public.cittadini

-- DROP TABLE IF EXISTS public.cittadini;

CREATE TABLE IF NOT EXISTS public.cittadini
(
    nome character varying(20) COLLATE pg_catalog."default" NOT NULL,
    cognome character varying(20) COLLATE pg_catalog."default" NOT NULL,
    codice_fiscale character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT cittadini_pkey PRIMARY KEY (codice_fiscale)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.cittadini
    OWNER to postgres;
-- Table: public.operatori

-- DROP TABLE IF EXISTS public.operatori;

CREATE TABLE IF NOT EXISTS public.operatori
(
    id integer NOT NULL DEFAULT nextval('operatoritelefonici_id_seq'::regclass),
    password character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT operatoritelefonici_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.operatori
    OWNER to postgres;
-- Table: public.operazioni

-- DROP TABLE IF EXISTS public.operazioni;

CREATE TABLE IF NOT EXISTS public.operazioni
(
    data timestamp without time zone NOT NULL,
    operatori integer,
    op character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT operazioni_pkey PRIMARY KEY (data),
    CONSTRAINT operazioni_operatori_fkey FOREIGN KEY (operatori)
        REFERENCES public.operatori (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.operazioni
    OWNER to postgres;