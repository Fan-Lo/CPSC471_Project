# Host: localhost    Database: 471
# ------------------------------------------------------
# Server version 5.0.51b-community-nt-log

DROP DATABASE IF EXISTS `471`;
CREATE DATABASE `471` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `471`;


DROP TABLE IF EXISTS DAILY_CLIENT_NEEDS;
CREATE TABLE DAILY_CLIENT_NEEDS (
	ClientID		int not null AUTO_INCREMENT,
	Client			varchar(25),
	WholeGrains		int,
	FruitVeggies	int,
	Protein			int,
	Other			int,
	Calories		int,
	primary key (ClientID)
);


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

DROP TABLE IF EXISTS PATIENT;
CREATE TABLE PATIENT (

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