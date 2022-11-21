# Host: localhost    Database: 471
# ------------------------------------------------------
# Server version 5.0.51b-community-nt-log

DROP DATABASE IF EXISTS `471`;
CREATE DATABASE `471` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `471`;

DROP TABLE IF EXISTS PATIENT;
CREATE TABLE PATIENT (
	AHC			CHAR(9) not null,
    SEX			CHAR(1),
    DOB			DATE not null,
    FName		varchar(25) not null,
    MidIN		char(1),
    LName		varchar(25) not null,
    PName		varchar(25),
    HeadAHC 	CHAR(9),
    StreetName 	varchar(100) not null,
    StreetNum 	varchar(10) not null,
    City 		varchar(10) not null,
    Country		varchar(10) not null,
    PostalCode	varchar(6) not null,
	CONSTRAINT PXPK PRIMARY KEY (AHC),
    CONSTRAINT HEADFK FOREIGN KEY (HeadAHC) REFERENCES PATIENT(AHC) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS EMPLOYEE;
CREATE TABLE EMPLOYEE (
    SIN		CHAR(9) not null,
    OPhone	varchar(14) DEFAULT '4031112222',
    JobType	varchar(20) not null,
    SuperSIN CHAR(9),
	DOB		DATE not null,
    FName	varchar(25) not null,
    MidIN	char(1),
    LName	varchar(25) not null,
	CONSTRAINT EMPPK PRIMARY KEY (SIN),
    CONSTRAINT SUPERFK foreign key (SuperSIN) REFERENCES EMPLOYEE(SIN) ON DELETE SET NULL ON UPDATE CASCADE
);

	
DROP TABLE IF EXISTS INSURANCE;
CREATE TABLE INSURANCE
(
	Policy		INT(5),
    MemberID 	INT(7),
    Name 		VARCHAR(25) NOT NULL,
    PatAHC		CHAR(9) NOT NULL,
    PRIMARY KEY(MemberID, Policy),
    FOREIGN KEY(PatAHC) REFERENCES PATIENT(AHC)
);

DROP TABLE IF EXISTS PAYS;
CREATE TABLE PAYS 
(
	Policy		INT(5),
    MemberID	INT(7),
    InvoiceID 	INT not NULL,
    PatAHC 		VARCHAR(25) NOT NULL,
	
    FOREIGN KEY(PatAHC) REFERENCES PATIENT(AHC), 
    FOREIGN KEY(MemberID) REFERENCES INSURANCE(MemberID),
    FOREIGN KEY(Policy) REFERENCES INSURANCE(Policy),
    FOREIGN KEY(InvoiceID) REFERENCES INVOICE(InvoiceID),
	PRIMARY KEY(Policy, MemberID, InvoiceID, PatAHC)
);

DROP TABLE IF EXISTS APPOINTMENT;
CREATE TABLE APPOINTMENT
(
	PatAHC		CHAR(9) NOT NULL,
    MedStaffSIN	CHAR(9) NOT NULL,
    ApptTime	TIME,
    
    FOREIGN KEY(PatAHC) REFERENCES PATIENT(AHC),
    FOREIGN KEY(MedStaffSIN) REFERENCES EMPLOYEE(SIN),
    PRIMARY KEY(PatAHC, MedStaffSIN)
);

DROP TABLE IF EXISTS REFERRAL;
CREATE TABLE REFERRAL
(
	PatAHC		CHAR(9) NOT NULL,
    MedStaffSIN	CHAR(9) NOT NULL,
    
    FOREIGN KEY(PatAHC) REFERENCES PATIENT(AHC),
    FOREIGN KEY(MedStaffSIN) REFERENCES EMPLOYEE(SIN),
    PRIMARY KEY(PatAHC, MedStaffSIN)
);

DROP TABLE IF EXISTS REFERRAL_LETTER;
CREATE TABLE REFERRAL_LETTER 
(
	PatAHC		CHAR(9) NOT NULL,
    	RefDate 	DATE,
    	FOREIGN KEY(PatAHC) REFERENCES PATIENT(AHC),
    	PRIMARY KEY(PatAHC, RefDate)
);

DROP TABLE IF EXISTS WRITES;
CREATE TABLE WRITES
(
	MedStaffSIN	CHAR(9) NOT NULL,
    ExamID 		INT(5),
    PatAHC		CHAR(9) NOT NULL,
    
    FOREIGN KEY(PatAHC) REFERENCES PATIENT(AHC),
    FOREIGN KEY(MedStaffSIN) REFERENCES EMPLOYEE(SIN),
    FOREIGN KEY(ExamID) REFERENCES EXAM_DETAIL(ExamID),
    PRIMARY KEY(MedStaffSIN, ExamID, PatAHC)
);
	
DROP TABLE IF EXISTS INVOICE;
CREATE TABLE INVOICE (
	InvoiceID		int(10) not null,
    	PatAHC			CHAR(9) not null,
    	InvoiceDate		DATE,
    	PRIMARY KEY (InvoiceID),
    	FOREIGN KEY(PatAHC) references PATIENT(AHC)
    );
    
DROP TABLE IF EXISTS CONTAINS;
CREATE TABLE CONTAINS (
	ProductID	int(10) not null,
	InvoiceID 	int(10) not null,
	PatAHC		CHAR(9) not null,
	FOREIGN KEY(InvoiceID) references INVOICE(InvoiceID),
	FOREIGN KEY(ProductID) references PRODUCTS(ProductID),
	FOREIGN KEY(PatAHC) references PATIENT(AHC),
	PRIMARY KEY (ProductID, InvoiceID, PatAHC)
);
   
DROP TABLE IF EXISTS GOV_BILLING;
CREATE TABLE GOV_BILLING (
	BillingNo	int(10) not null,
	PatAHC 		CHAR(9) not null,
	Total		int not null,
	BillingDate DATE,
	FOREIGN KEY(PatAHC) references PATIENT(AHC)
);

DROP TABLE IF EXISTS PRODUCTS;   
CREATE TABLE PRODUCTS (
	ID			int(7) not null,
	PName		varchar(20),
	Supplier 	varchar(25)
);

DROP TABLE IF EXISTS PAST_EXAM_RECORD;
CREATE TABLE PAST_EXAM_RECORD (
	PatAHC		CHAR(9)	not null,
	RecordID	int(9) not null,
	FOREIGN KEY(PatAHC) references PATIENT(AHC),
	FOREIGN KEY(RecordID) references EXAM_DETAIL(RecordID)
);
   
DROP TABLE IF EXISTS EXAM_DETAIL;
CREATE TABLE EXAM_DETAIL (
	ExamID 	int(5) not null,
	PatAHC 	CHAR(9) not null,
	RecordID int(9),
	FOREIGN KEY (ExamID) references WRITES(ExamID),
	FOREIGN KEY (PatAHC) references PATIENT(AHC) 
);
   
