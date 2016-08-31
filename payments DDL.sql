CREATE DATABASE payments;
USE payments;
CREATE USER 'project'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON payment_records TO 'project'@'localhost';
FLUSH PRIVILEGES;
CREATE TABLE payment_records
(
    applicable_manufacturer_or_applicable_gpo_making_payment_country VARCHAR(100),
    applicable_manufacturer_or_applicable_gpo_making_payment_id MEDIUMTEXT,
    applicable_manufacturer_or_applicable_gpo_making_payment_name VARCHAR(100),
    applicable_manufacturer_or_applicable_gpo_making_payment_state VARCHAR(2),
    payment_publication_date DATE,
    physician_first_name VARCHAR(50),
    physician_last_name VARCHAR(50),
    physician_primary_type VARCHAR(100),
    physician_profile_id INT(32),
    physician_specialty VARCHAR(3000),
    program_year INT(11),
    recipient_city VARCHAR(20),
    recipient_country VARCHAR(40),
    recipient_primary_business_street_address_line1 VARCHAR(300),
    recipient_primary_business_street_address_line2 VARCHAR(300),
    recipient_state VARCHAR(2),
    recipient_zip_code VARCHAR(100),
    record_id INT(32) PRIMARY KEY NOT NULL,
    submitting_applicable_manufacturer_or_applicable_gpo_name VARCHAR(300),
    terms_of_interest VARCHAR(1000),
    total_amount_invested_usdollars FLOAT,
    value_of_interest FLOAT
);
CREATE UNIQUE INDEX payment_records_record_id_uindex ON payment_records (record_id);
CREATE INDEX payment_record_sepc_amount_index ON payment_records (physician_specialty, total_amount_invested_usdollars, physician_profile_id);