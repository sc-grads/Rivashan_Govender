USE AutomatedDatabase
go


IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Employee_Details')
CREATE TABLE Employee_Details

-- Create UserInfo table with additional columns
CREATE TABLE Employee_Details
(
    EmpID INT NOT NULL,
    Name VARCHAR(50) NOT NULL,
    Surname VARCHAR(50),
    [Date Of Empoyment] DATE,
    Position VARCHAR(50) CHECK (Position IN ('Representative', 'Agent', 'Manager'))
);


-- Insert data into UserInfo table with new columns
INSERT INTO Employee_Details (EmpID, Name, Surname, [Date Of Empoyment], Position)
VALUES 
(1234, 'Elon', 'Musk', '2001-06-28', 'Manager'),
(2341, 'Ted', 'Mosby', '2006-04-27', 'Agent'),
(3412, 'Chandler', 'Bing', '2023-04-16', 'Agent'),
(4512, 'Akira', 'Toriyama', '2002-01-01', 'Manager'),
(5123, 'Peppa', 'Pig', '2024-03-15', 'Representative');

