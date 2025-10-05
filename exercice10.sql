/* # Exercise 10: Implementing the University Information System */
/* # In this exercise, as illustrated in the three figures provided, you need to create two tables: `Professor` and `Department`.*/

/* # 10.1 Create a database named 'University'*/
/* # You can create a database using the SQL command:*/
CREATE DATABASE University;


/* # 10.2 Create the `Professor` table*/
/* # This table can be created with the following SQL command, matching the structure shown in the images:*/
CREATE TABLE Professor (
    Professor_Id INT PRIMARY KEY,
    Professor_Name VARCHAR(255),
    Department_Id INT,
    Joining_Date DATE,
    Speciality VARCHAR(255),
    Salary DECIMAL,
    Experience VARCHAR(255)
);


/* # 10.3 Create the `Department` table*/
/* # The Department table can be created with this SQL command:*/

CREATE TABLE Department (
    Department_Id INT PRIMARY KEY,
    Department_Name VARCHAR(255),
    Number_Of_Students INT
);


/* # 10.4 Connect to your database server*/
/* # This step will depend on the database system you are using (e.g., MySQL, PostgreSQL). You typically use a connection string or a database client to connect.*/
/* # 10.5 Retrieve information from `Professor` and `Department` using `Professor_Id` and `Department_Id`*/
/* # To retrieve this information, you'll use a JOIN statement in SQL:*/

SELECT * FROM Professor
JOIN Department ON Professor.Department_Id = Department.Department_Id;


/* # 10.6 Get a list of professors by given specialty and salary*/
/* # You can use the SQL SELECT statement with WHERE clauses:*/
SELECT * FROM Professor
WHERE Speciality = 'YourSpeciality' AND Salary = YourSalary;


/* # 10.7 Get a list of professors from a given department*/
/* # Again, a SELECT statement with a WHERE clause will work:*/
SELECT * FROM Professor
WHERE Department_Id = YourDepartmentId;


/* # 10.8 Implement a function to update a given professor's experience in years*/
/* # For updating a professor's experience, you can use the SQL UPDATE statement:*/
UPDATE Professor
SET Experience = 'NewExperience'
WHERE Professor_Id = YourProfessorId;


/* #Remember to replace 'YourSpeciality', 'YourSalary', 'YourDepartmentId', and 'NewExperience' with actual values based on the requirement. Also, 'YourProfessorId' should be replaced with the actual ID of the professor whose experience you want to update.*/