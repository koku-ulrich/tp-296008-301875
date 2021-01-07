DROP TABLE IF EXISTS "personne";
DROP SEQUENCE IF EXISTS personne_id_automatique;
CREATE SEQUENCE personne_id_automatique INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."personne"
(
    "id"               integer                DEFAULT nextval('personne_id_automatique') NOT NULL,
    "campusId"         integer                NOT NULL UNIQUE,
    "nom"              character varying(100) NOT NULL,
    "prenom"           character varying(100) NOT NULL,
    "dateNaissance"    date(10)               NULL,
    "email"            character varying(250) NOT NULL
) WITH (oids = false);

