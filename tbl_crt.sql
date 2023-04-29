CREATE TABLE category (
    category_id INT NOT NULL,
    cname VARCHAR(50),
    PRIMARY KEY(category_id),
)

CREATE TABLE customer(
    cust_id INT(11) NOT NULL,
    first_name VARCHAR(50) ,
    last_name VARCHAR(50),
    phone_number VARCHAR(11),
    PRIMARY KEY(cust_id)
)

CREATE TABLE employee(
    employee_id INT(11) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(50),
    email VARCHAR(100),
    phone_number VARCHAR(11),
    job_id INT(11),
    location_id INT(11),
    PRIMARY KEY(employee_id),
    FOREIGN KEY(phone_number) REFERENCES customer(phone_number),
    FOREIGN KEY(job_id) REFERENCES job(job_id),
    FOREIGN KEY(location_id) REFERENCES location(location_id),
)

CREATE TABLE job(
    job_id INT(11) NOT NULL,
    job_title VARCHAR(50),
    PRIMARY KEY(job_id)
)

CREATE TABLE location(
    location_id INT(11) NOT NULL,
    province VARCHAR(100),
    city VARCHAR(100),
    PRIMARY KEY(location_id)
)

CREATE TABLE manager(
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    location_id int(11) NOT NULL,
    email VARCHAR(50),
    FOREIGN KEY(location_id) REFERENCES location(location_id)
)

CREATE TABLE product(
    product_id INT(11) NOT NULL,
    product_code VARCHAR(20) NOT NULL,
    name VARCHAR(50),
    description VARCHAR(250) NOT NULL,
    qty_stock INT(50),
    on_hand INT(250) NOT NULL,
    price int(50),
    category_id INT(11),
    supplier_id INT(11),
    date_stock_in VARCHAR(50),
    PRIMARY KEY(product_id),
    FOREIGN KEY(category_id) REFERENCES category(category_id),
    FOREIGN key(supplier_id) REFERENCES supplier(supplier_id)
)

CREATE TABLE supplier(
    supplier_id INT(11) NOT NULL,
    company_name VARCHAR(50),
    location_id INT(11) NOT NULL,
    phone_number VARCHAR(11),
    PRIMARY KEY(supplier_id),
    FOREIGN KEY(location_id) REFERENCES loction(location_id)
)

CREATE TABLE transaction(
    trans_id INT(50) NOT NULL,
    cust_id INT(11),
    numofitems VARCHAR(250) NOT NULL,
    subtotal VARCHAR(50) NOT NULL,
    lessvat VARCHAR(50) NOT NULL,
    netvat VARCHAR(50) NOT NULL,
    addvat VARCHAR(50) NOT NULL,
    grandtotal VARCHAR(250) NOT NULL,
    cash VARCHAR(250) NOT NULL,
    date VARCHAR(50) NOT NULL,
    trans_d_id VARCHAR(250) NOT NULL,
    PRIMARY KEY(trans_id),
    FOREIGN KEY(cust_id) REFERENCES customer(cust_id),
    FOREIGN KEY(trans_d_id) REFERENCES transaction_details(trans_d_id)
)

CREATE TABLE transaction_details(
    id INT(11) NOT NULL,
    trans_d_id VARCHAR(250) NOT NULL,
    products VARCHAR(250) NOT NULL,
    qty VARCHAR(250) NOT NULL,
    price VARCHAR(250) NOT NULL,
    employee VARCHAR(250) NOT NULL,
    role VARCHAR(250) NOT NULL,
    PRIMARY KEY(id,trans_d_id)
)

CREATE TABLE type(
    type_id INT(11) NOT NULL,
    type VARCHAR(50),
    PRIMARY KEY(type_id)
)

CREATE TABLE users(
    id INT(11) NOT NULL,
    employee_id INT(11),
    username VARCHAR(50),
    password VARCHAR(50),
    type_id INT(11),
    PRIMARY KEY(id),
    FOREIGN KEY(employee_id) REFERENCES employee(employee_id),
    FOREIGN KEY(type_id) REFERENCES type(type_id)
)

-- trigger querie
delimiter $$
CREATE OR REPLACE TRIGGER phone_no_changes 
BEFORE INSERT ON customer 
FOR EACH ROW  
BEGIN
    DECLARE x int;
    declare mess varchar(100);
    set mess = "ERROR: Invalid phone number";
    set x=fphno(NEW.phone_number);
    if(x="NO") THEN 
        signal sqlstate '45000'
        set message_text = mess;
    end if;
END; 
$$
delimiter ;


-- function
delimiter $$
CREATE OR REPLACE FUNCTION fphno(phone_number VARCHAR(255))
RETURNS varchar(255)
BEGIN 
    declare x varchar(50);
    declare phonenum int;
    set phonenum = cast(phone_number as int);
    IF((phonenum<1000000000 or phonenum>9999999999)) THEN
        set x = "NO";
    ELSE
        set x = "YES";
    end if;
    return x;
END; 
$$
delimiter ;

--nested queries
select name,description,price from product where category_id in(select category_id from category where cname="Tranmission_parts");
select first_name,last_name,job_id from employee where location_id in (select location_id from supplier where location_id in(select location_id from location where company_name="Honda"));

--corelated queries
SELECT employee_id,username,type_id FROM users usr WHERE EXISTS ( SELECT * FROM type WHERE type_id = usr.type_id);
SELECT product_id,name,category_id from product extrnl where price < (SELECT AVG(price) from product where category_id=extrnl.category_id)

--
insert into customer values(34,"point","noice","1234567898765432")

--join
SELECT supplier.supplier_id, location.location_id FROM supplier INNER JOIN location ON supplier.location_id = location.location_id;
SELECT * FROM users CROSS JOIN type;

--view
CREATE VIEW [usr_info] AS SELECT username, password FROM users WHERE type_id = 2;

--Aggregate function
SELECT MIN(price) AS minimum_price from product;
SELECT COUNT(location_id) from location;

--set
SELECT * FROM location WHERE location_id NOT IN(SELECT location_id FROM employee);
SELECT * FROM customer WHERE first_name IN (SELECT first_name from employee);