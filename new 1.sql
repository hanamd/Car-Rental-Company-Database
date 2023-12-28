-- Practice for midterm

--Chapter 4
SELECT Fname, Bdate
FROM	EMPLOYEE
WHERE	Salary < 30,000 or 
		Salary > 50,000;    -- there is an or statment
		
--2
SELECT Mgr_start_date
FROM DEPARTMENT
WHERE Dname = ' Research' ;

--3
SELECT Fname, Bdate
FROM	EMPLOYEE
WHERE	Salary >=30,000 and Salary <= 50,000;

--4

/*Diffrence between selct condition and joint condition
select works with one table where has joint works with creating a second table */

--5

SELECT	E.Fname
FROM	EMPLOYEE as E, DEPENDENT as D
WHERE	E.SSN = D.Essn AND
		D.Deendent_name = E.Fname;
		
		
--6

CREATE TABLE PROJECT
	( Pname					VARCHAR(50)						Not NULL,
	  Pnumber				INT								Not NULL,
	  Plocation				VARCHAR(60)						NOT NULL,
	  Dnum					INT								NOT NULL;
	  PRIMARY KEY(Pnumber);
	)
CREATE TABLE WORKS_ON
	(	Essn				CHAR(9)							Not NULL,,
		Pno					INT 							Not NULL,
		Hours				INT	,
		PRIMARY KEY(ESSN),
	    PRIMARY KEY (PNO)
		FOREIGN KEY (PNO);
	)
CREATE TABLE DEPENDENT
	(	Essn					CHAR(9)						Not NULL,
		Dependent_name			VARCHAR(30)						Not NULL,
		Sex						CHAR						Not NULL,
		Bdate					DATE						Not NULL,
		Relationship			VARCHAR(30)					;
	)

-- 7
SELECT attruibutes
FROM	tables list
WHERE 	contional

-- where is optional

--8

SELECT	Bdate, Address
FROM	EMPLOYEE;

--9
SELECT	 Fname
FROM	EMPLOYEE
WHERE	ADDRESS = '*Huston,TX';

--10
SELECT Fname 
FROM EMPOYEE, PROJECT, DEPARTMENT
WHERE	Pname = 'Research' AND
		Dnum = Dnumber AND
		Dnumber = Dno;
		
		
--11
--creat a schema fro a compnany

CREATE SCHEMA COMPANY ;


--12

SELECT	Dependent_name
FROM	EMPLOYEE, DEPENDENT
WHERE	Fname = ' John' AND
		Minit = 'B'	AND
		Lname = 'Smith' AND
		SSn = Essn;
		
--13

SELECT	Pnumber, Dnum, Lname, Address, Bdate
FROM EMPLOYEE, PROJECT, DEPARTMENT
WHERE Plocation = 'Stafford' AND
	Dnum = Dnumber AND
	Mgr_ssn = ssn;
	
--14
SELECT	Fname
FROM	EMPLOYEE, DEPARTMENT, PROJECT, WORKS_ON
WHERE	Dnumber= 5 AND 
		Dnumber = Dnum AND 
		Pname = 'ProjectX' AND
		Pnumber = pno ANd 
		Hours > 10;
		
--15
SELECT	bDATE , address
FROM	EMPLOYEE
WHERE	 Fname = 'john' AND
		Minit 'B' AND
		Lname = 'Smith';
		
--16
SELECT Fname , ADDRESS
FROM	EMPLOYEE, DEPARTMENT
WHERE	Dname = 'Research' AND
		Dnumber =Dno;
		
--Chapter 5

--Q1
SELECT Fname
FROM EMPLOYEE as E
WHERE EXISTS 
(SELECT Fname
 FROM Dependent as D 
 WHERE E.ssn = D.Essn)
		
		AND
		
	EXISTS ( SELECT * 
	FROM Department as R
	WHERE E.SSn = R.mgr_ssn)   ;
	
--Q2

--left join , outer join and other joins etc

--Q3

SELECT E. Fname
FROM EMPLOYE AS E
WHERE EXISTS(
SELECT *
FROM DEPENDENT AS D
WHERE E.Ssn = D.ESSN AND
E.FNAME = D.Dependent_name);


SELECT E.FNAME , E.LNAME 
FROM EMPLYEE AS EACHWHERE 
WHERE E.SSN IN 
(SELECT D.ESSN 
FROM DEPENDENT AS D
WHERE E.FNAME =.DPEPENDENT_NAME);


--Q4
SELECT FNAME , ADDRESS
FROM EMPLOYEE
WHERE  DNO IN
( SELECT DNUMBER 
FROM DEPARTEMNT 
WHERE DNAME = 'RESEARCH');


--Chapter 5 AGAIN

--Q1


-- What is Query modification implementation of view ? modifies the view query into a query on he underlying base table

--Q2

CREATE VIEW WORKS_ON_NEW AS
SELECT FNAME, LNAME, PNAME, HOURS
FROM EMPLOYEE, ProjectX
WHERE SSN = ESSN 
	AND PNO = PNUMBER
	GROUP BY PNAME
	
--Q3

--SUMMARIZES DEPARTMENT INFORMATION BY DEPARTMENT NUMBER THAT WHY THERE IS A GROUP BY

CREATE VIEW DEPT_INFO( DNO,NUM_EMP, TOTAL_SALARY) AS

SELECT DNO, COUNT(*), SUM(SALARY)
FROM EMPLOYEE
GROUP BY DNO

--Q4
-- what is view ? vire is a virtual table that is derived from other tables

--Q5

SELECT E.FNAME
FROM EMPLOYEE  AS E
WHERE NOT EXISTS
( SELECT *
	FROM DEPENDENT AS D
	WHERE E.SSN = D.ESSN )
	
	
--Q6

/*VIEW MATERALIZATION
-- phusically creating and keeping a temporary table that holds the view query result */

--Q7

SELECT PNO, PNAME, COUNT(*)
FROM PROJECT , WORKS_ON
WHERE PNUMBER = PNO
GROUP BY PNUMBER , PNAME
HAVING COUNT(*) > 2;

--Q8

/* WHAT DOES HAVING CLAUSE FO 
SPECIFIES A CONDITION FOR THE SELECTION GROUP ( NOT TUPLES --> GROUPS) */

--Q9
SELECT PNO , PNAME , COUNT(*)
FROM PROJECT AS P , WORKS_ON AS W
WHERE P.NUMNER = W.PNO
GROUP BY P.PNUMENR, P.NAME;

--Q10

SELECT DNO, COUNT(*), AVG(SALARY)
FROM EMPLOYEE
GROUP BY DNO;

--Q11

SELECT FNAME , LNAME, DNAME
FROM (DEPARTEMNT AS D JOIN EMPLOYEE AS E ON D.DNUMBER = E.DNO);

--Q12

SELECT FNAME , ADDRESS
FROM EMPLOYEE
WHERE DNO IN ( SELECT DNUMBER
				 FROM DEPARTEMNT
				 WHERE DNAME = 'RESEARCH');
				 

--Q13
/* WHAR IS GROUP BY 
GROUP BY is a sql command that is used with aggregate functions.  
Instead of collecting the information 
for the entire attribute,
it can be used to create subgroups of an attribute and 
collect the information within those subgroups. */

--Q14

SELECT FNAME
FROM EMPLOYEE AS E
WHERE NOT EXISTS ( SELECT *
					FROM DEPENDENT AS D
					WHERE E.SSN = D.ESSN);

--Q15

--QUERY 1

SELECT COUNT (*)
FROM EMPLOYEE

--QUERY 2
SELECT COUNT (*)
FROM EMPLOYEE, DEPARTMENT
WHERE DNO = DNUMBER
	AND DNAME = 'RESEARCH';

--Q16

SELECT MAX(SALARY), MIN(SALARY), AVG(SALARY)
FROM EMPLOYEE, DEPARTMENT
WHERE DNO = DNUMBER
	AND DNAME = 'RESEARCH';
	
	
--Q17

SELECT MAX(SALARY), MIN(SALARY), AVG(SALARY)
FROM EMPLOYEE;

--q18


/* what is aggregate functions ?
These can summarize information from multiple tuples into 
a single tuple like count, sum, max, min and average  */

--Q19

SELECT E.FNAME, E.LNAME,S.FNAME, S.LNAME,  
FROM (EMPLOYEE AS E INNER JOIN EMPLOYEE AS S ON E,SUPER_SSN = S.SSN);

--Q20

CREATE VIEW DEPT_NO ( DEP_NO, EMP_NO, TOTAL_SAL) AS 
SELECT DNO, COUNT(*), SUM(SALARY)
FROM EMPLOYEE
GROUP BY DNO;

--Q21

SELECT PNUMBER, PNAME , COUNT (*)
FROM PROJECT , WORKS_ON
WHERE PNUMBER = PNO
GROUP BY PNUMBER , PNAME
HAVING COUNT(*) > 2;

--Q22

SELECT PNUMBER , PNAME, COUNT (*)
FROM PROJECT AS P , WORKS_ON AS W
WHERE P.PNUMBER = W.PNO
GROUP NU P.PNUMBER , P.PNAME;

--Q23

SELECT FNAME , DNAME
FROM (DEPARTEMNT AS D FULL PUTTER JOIN EMPLOYEE AS E ON D.DNUMBER = E.DNO)

--Q24

SELECT  PNUMBER, PNAME , COUNT (*)
FROM PROJECT, WORKS_ON
WHERE PNUMBER = PNO 
GROUP BY PNUMBER, PNAME


--Q25

SELECT E.FNAME, S.FNAME
FROM  (EMPLOYEE AS E INNER JOIN EMPLOYEE AS S 
	   ON E.SSN = S.SUPPER_SSN)
	   
	   
	   
--Q26

SELECT FNAME, DNAME 
FROM EMPLOYEE, DEPARTMENT
WHERE DNO = DNUMBER
	  
--OR
SELECT E.FNAME , E.DNAME 
FROM (EMPLOYEE AS E FULL JOIN  DEPARTMENT  AS D ON E.DNO = D.DNUMBER)


--Q27

SELECT FNAME , DNAME 
FROM (EMPLOYEE AS E FULL JOIN  DEPARTMENT  AS D ON E.DNO = D.DNUMBER)

--Q28

SELECT FNAME , DNAME 
FROM (EMPLOYEE AS E INNER JOIN  DEPARTMENT  AS D ON E.DNO = D.DNUMBER)

-- YOU CAN WRITE INNER JOIN AS JOIN 

--Q29

SELECT DISTINCT ESSN
FROM WORKS_ON 
WHERE PNO IN (1,2,3);

--q30
--Retrieve the names of all employees who do not have supervisors →
SELECT FNAME
FROM EMPLOYEE
WHERE SUPPER_SSN IS NULL

--Q31
SELECT FNAME
FROM EMPLOYEE
WHERE DNO IN (SELECT DNUMBER 
			  FROM DEPARTEMNT
			  WHERE DNAME = 'RESEARCH');
			  
--Q32
/*Using a nested query - Retrieve the name of each employee who has 
a dependent with the same first name as the employee */
SELECT FNAME 
FROM EMPLOYEE AS M
WHERE EXISTS ( SELECT *
				FROM DEPENDENT
				WHERE M.SSN = ESSN)
		EXISTS ( SELECT *
				FROM DEPARTMENT 
				WHERE M.SSN = MGR_SSN);
				
				
--Q33

/*What is a correlated nested Query → If a condition in the inner query
 references an attribute in the outer query, the two queries are said to be correlated */
 
 
 
 --test
 
 --21
 
SELECT NAME
FROM STUDENT AS S ,  GRADE AS G, SECTION AS O, COURSE AS C
WHERE S.SSN = G.SSN
	  AND G.CNO = O.CNO
	  AND O.CNO = C.CNO
	  AND DEPARTEMNT = 'MATH';
	  
--22

SELECT S.NAME , S.SSN,G.CNO, SEMESTER , YEAR, NUMERIC_GRADE
FROM STUDENT AS S ,  GRADE AS G, SECTION AS O, COURSE AS C
WHERE S.CLASS = 'SENIOR'
	  AND C.CNO = O.CNO
	  AND O.CNO = G.CNO
ORDER BY S.NAME, G.YEAR, G.SEMESTER;
	
--23

SELECT S.NAME, S.SSN, COUNT(*), SUM(C.CREDITHOURS)
FROM STUDENT AS S ,GRADES AS G , SECTION AS S, COURSE AS C
WHERE S.SSN = G.SSN
	  AND G.CNO = S.CNO
	  AND S.CNO = C.CNO
HAVING COUNT(C.CREDITHOURS) > 60 ;

--24

SELECT CNAME, CNO
FROM COURSE AS C 
WHERE C.DEPARTMENT = 'CSE'
	  AND C.LEVEL IN (1,2);
	  
--25

SELECT NAME
FROM STUDENT
WHERE MAJOR = 'CSE';

--26

SELECT DISTINCT  MAJOR, COUNT(*)
FROM STUDENT;

--27

SELECT S.NAME
FROM STUDENT AS S 
WHERE NOT EXISTS ( SELECT *
				   FROM GRADE AS G,SECTION AS O, COUSES AS C
				   WHERE S.SSN = G.SSN
				   AND G.CNO = O.CNO
				   AND O.CNO = C.CNO
				   AND DEPARTMENT = 'MATH');
				   
				   
--28

SELECT S.SNAME, S.SSN, COUNT(G.SECNO),SUM(C.CREDITHOURS)
FROM STUDENT AS S,COURSE AS C, GRADE AS G, 
WHERE S.SSN = G.SSN;