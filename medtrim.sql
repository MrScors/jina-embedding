CREATE TABLE
  MEDTRIM (
    generic_name STRING(MAX) NOT NULL,
    brand_name STRING(MAX) NOT NULL,
    product_type STRING(MAX) NOT NULL,
    route STRING(MAX) NOT NULL,
    dosage_form STRING(36) NOT NULL,
    embedding ARRAY<FLOAT64> NOT NULL
    )
PRIMARY KEY
  (generic_name),
ON
DELETE
  CASCADE;