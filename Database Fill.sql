INSERT INTO PATIENT
VALUES( '123456789', 'F',  '2000-05-06', 'Sarah', 'D', 'Smith', 'Sarah', '123456789', 'Covepark Rise', '34', 'Calgary', 'Canada', 'T3J1S4');

INSERT INTO PATIENT
VALUES( '200220020', 'F',  '2007-08-20', 'Areej', 'J', 'Khan', 'Areej', '123456789', 'Covepark Rise', '34', 'Calgary', 'Canada', 'T3J1S4');

INSERT INTO PATIENT
VALUES( '113456789', 'M',  '1990-07-01', 'Micheal', 'D', 'Ash', 'Mike', '113456789', 'Covepark Drive', '90', 'Calgary', 'Canada', 'T3J2S4');


INSERT INTO PATIENT_PHONE(AHC, PhoneNum) VALUES
('123456789', '4031111111'),
('123456789', '4032222222');


INSERT INTO PATIENT_LOGIN 
VALUES('123456789', 'password');

INSERT INTO PATIENT_LOGIN 
VALUES('200220020', 'Happymeme11');

INSERT INTO PATIENT_LOGIN 
VALUES('113456789', 'pass');





INSERT INTO EMPLOYEE
VALUES('098765432', '4031231234', 'Doctor', '098765432', '1967-09-08', 'Noah', 'L', 'White');

INSERT INTO EMPLOYEE
VALUES('987654321', '4031231234', 'Nurse', '098765432', '1999-07-15', 'Emma', 'W', 'Oliver');

INSERT INTO EMPLOYEE_LOGIN
VALUES('987654321', 'Project');

INSERT INTO EMPLOYEE_LOGIN 
VALUES('098765432', 'Application');



SELECT * 
FROM EMPLOYEE AS E
WHERE E.SIN = '098765432';

SELECT * FROM EMPLOYEE;
SELECT * FROM EMPLOYEE_LOGIN;
SELECT * FROM PATIENT_PHONE;
SELECT * FROM PATIENT;
SELECT * FROM PATIENT_LOGIN;
SELECT * FROM PATIENT_PHONE;
SELECT * FROM INSURANCE;