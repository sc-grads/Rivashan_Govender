/*
1. Write a query in SQL to retrieve all rows and columns from the employee table in the Adventureworks database. Sort the result set in ascending order on jobtitle.
Sample Output:

*/

SELECT * FROM HumanResources.Employee

/*

businessentityid|nationalidnumber|loginid                     |jobtitle                                |birthdate |maritalstatus|gender|hiredate  |salariedflag|vacationhours|sickleavehours|currentflag|rowguid                             |modifieddate           |organizationnod----------------+----------------+----------------------------+----------------------------------------+----------+-------------+------+----------+------------+-------------+--------------+-----------+------------------------------------+-----------------------+---------------245|363910111       |adventure-works\barbara1    |Accountant                              |1976-01-04|M            |F     |2009-02-18|true        |           58|            49|true       |3ffba84e-8e97-4649-a5e1-859649d83aae|2014-06-30 00:00:00.000|/4/2/4/        248|480951955       |adventure-works\mike0       |Accountant                              |1979-07-01|S            |M     |2009-03-08|true        |           59|            49|true       |ac35337d-7c75-4dee-bb11-6564f257fe18|2014-06-30 00:00:00.000|/4/2/7/        241|30845           |adventure-works\david6      |Accounts Manager                        |1983-07-08|M            |M     |2009-01-30|true        |           57|            48|true       |2dc9d534-f5d1-4a14-8282-0a2a0eb6fd4d|2014-06-30 00:00:00.000|/4/2/          246|663843431       |adventure-works\dragan0     |Accounts Payable Specialist             |1977-02-14|M            |M     |2009-02-11|false       |           63|            51|true       |51c54d34-064b-44f7-a6b1-7702bd491980|2014-06-30 00:00:00.000|/4/2/5/        247|519756660       |adventure-works\janet0      |Accounts Payable Specialist             |1979-03-09|M            |F     |2009-03-01|false       |           64|            52|true       |0c641d77-8675-493f-9947-8c65136559cd|2014-06-30 00:00:00.000|/4/2/6/        243|60517918        |adventure-works\candy0      |Accounts Receivable Specialist          |1976-02-23|S            |F     |2009-01-06|false       |           61|            50|true       |9e9f713b-707c-4f7e-9504-de188052a045|2014-06-30 00:00:00.000|/4/2/2/        244|931190412       |adventure-works\bryan1      |Accounts Receivable Specialist          |1984-09-20|S            |M     |2009-01-24|false       |           62|            51|true       |cb3e71ec-a381-4716-87df-d3841ab9795a|2014-06-30 00:00:00.000|/4/2/3/        242|363923697       |adventure-works\deborah0    |Accounts Receivable Specialist          |1976-03-06|M            |F     |2008-12-18|false       |           60|            50|true       |09f75454-028c-46ca-bc08-0147bd0220d7|2014-06-30 00:00:00.000|/4/2/1/        272|525932996       |adventure-works\janaina0    |Application Specialist                  |1985-01-30|M            |F     |2008-12-23|true        |           71|            55|true       |241535c7-7a31-4a6a-9e0d-a83c30c2edda|2014-06-30 00:00:00.000|/5/7/          268|314747499       |adventure-works\ramesh0     |Application Specialist                  |1988-03-13|S            |M     |2009-02-03|true        |           73|            56|true       |be190269-4003-4d7f-809e-7b3fdc235da8|2014-06-30 00:00:00.000|/5/3/          ...


2. Write a query in SQL to retrieve all rows and columns from the employee table using table aliasing in the Adventureworks database. Sort the output in ascending order on lastname.
Sample Output:


 */

 SELECT * FROM Person.Person ORDER BY LastName

 /*

businessentityid|persontype|namestyle|title|firstname               |middlename      |lastname              |suffix|emailpromotion|additionalcontactinfo|demographics|rowguid                             |modifieddate           |----------------+----------+---------+-----+------------------------+----------------+----------------------+------+--------------+---------------------+------------+------------------------------------+-----------------------+285|SP        |false    |Mr.  |Syed                    |E               |Abbas                 |      |             0|                     |[XML]       |ff284881-01c2-4c77-95a7-4db96f59bb70|2013-03-07 00:00:00.000|293|SC        |false    |Ms.  |Catherine               |R.              |Abel                  |      |             1|[XML]                |[XML]       |d54e0552-c226-4c22-af3b-762ca854cdd3|2015-04-15 16:33:33.077|2170|GC        |false    |     |Kim                     |                |Abercrombie           |      |             2|                     |[XML]       |24f01b54-7a67-4b48-9ecc-72545d36c0ac|2009-11-29 00:00:00.000|295|SC        |false    |Ms.  |Kim                     |                |Abercrombie           |      |             0|[XML]                |[XML]       |f7cbdb48-0b44-470e-9f37-7060446fbfb9|2015-04-15 16:33:33.077|38|EM        |false    |     |Kim                     |B               |Abercrombie           |      |             2|                     |[XML]       |9a2163b3-2f4d-4f9a-91bd-07d326140f9c|2010-01-09 00:00:00.000|2357|GC        |false    |     |Sam                     |                |Abolrous              |      |             1|                     |[XML]       |78b8f41e-ed14-4e96-9531-ce9630e79e10|2009-02-21 00:00:00.000|211|EM        |false    |     |Hazem                   |E               |Abolrous              |      |             0|                     |[XML]       |c2637051-25a5-4461-b06a-523119259430|2009-02-21 00:00:00.000|297|SC        |false    |Sr.  |Humberto                |                |Acevedo               |      |             2|[XML]                |[XML]       |5a41d336-84cf-44d7-b12b-83b64b511f7e|2015-04-15 16:33:33.090|291|SC        |false    |Mr.  |Gustavo                 |                |Achong                |      |             2|[XML]                |[XML]       |d4c132d3-fcb5-4231-9dd5-888a54bec693|2015-04-15 16:33:33.060|299|SC        |false    |Sra. |Pilar                   |                |Ackerman              |      |             0|[XML]                |[XML]       |df1fb8ab-2323-4330-9ab8-54e13ce6d8f9|2015-04-15 16:33:33.090|121|EM        |false    |     |Pilar                   |G               |Ackerman              |      |             0|                     |[XML]       |81f50324-d0b5-4ea5-8b20-f99d46572c76|2008-12-26 00:00:00.000|4970|IN        |false    |     |Devin                   |                |Adams                 |      |             2|                     |[XML]       |ee57a0e0-d49e-4ca6-9c94-64e8eb0c05d6|2014-05-06 00:00:00.000|4429|IN        |false    |     |Xavier                  |C               |Adams                 |      |             1|                     |[XML]       |1578432b-b398-4359-b432-bf868c00a3c6|2013-10-19 00:00:00.000|4891|IN        |false    |     |Charles                 |R               |Adams                 |      |             2|                     |[XML]       |faa29129-5894-4f86-979d-015ee4733364|2013-07-07 00:00:00.000|4350|IN        |false    |     |Seth                    |L               |Adams                 |      |             0|                     |[XML]       |2b17fa8a-9643-4dcf-a61b-38fb9c3b0d3e|2014-03-06 00:00:00.000|3889|IN        |false    |     |Fernando                |S               |Adams                 |      |             0|                     |[XML]       |33fa7ddb-6372-48d7-92e4-75ef504a3746|2013-10-31 00:00:00.000|67|EM        |false    |     |Jay                     |G               |Adams                 |      |             0|                     |[XML]       |2fe289a7-ce57-49e5-be61-3e6580d22ea6|2009-02-26 00:00:00.000|1770|IN        |false    |Mr.  |Ben                     |                |Adams                 |      |             0|                     |[XML]       |ad322f5c-d052-4dde-84bc-d4b3b2682348|2011-10-24 00:00:00.000|...
 



3. Write a query in SQL to return all rows and a subset of the columns (FirstName, LastName, businessentityid) from the person table in the AdventureWorks database. The third column heading is renamed to Employee_id. Arranged the output in ascending order by lastname.
Sample Output:

*/
SELECT FirstName, LastName, (BusinessEntityID ) AS Employee_id FROM Person.Person ORDER BY LastName

/*


firstname               |lastname              |employee_id|------------------------+----------------------+-----------+Syed                    |Abbas                 |        285|Catherine               |Abel                  |        293|Kim                     |Abercrombie           |         38|Kim                     |Abercrombie           |        295|Kim                     |Abercrombie           |       2170|Sam                     |Abolrous              |       2357|Hazem                   |Abolrous              |        211|Humberto                |Acevedo               |        297|Gustavo                 |Achong                |        291|Pilar                   |Ackerman              |        299|Pilar                   |Ackerman              |        121|Luke                    |Adams                 |      16884|Adam                    |Adams                 |      16901|Natalie                 |Adams                 |      10262|Isabella                |Adams                 |      10261|Morgan                  |Adams                 |      10259|Kaitlyn                 |Adams                 |      10258|
 



4. Write a query in SQL to return only the rows for product that have a sellstartdate that is not NULL and a productline of 'T'. Return productid, productnumber, and name. Arranged the output in ascending order on name.
Sample Output:

*/

 

 SELECT ProductID, ProductNumber, Production.Product.Name AS ProductName FROM production.product WHERE SellStartDate IS NOT NULL AND Production.Product.ProductLine = 'T' ORDER BY Production.Product.Name

 

/*


productid|productnumber|producname                   |---------+-------------+-----------------------------+890|FR-T98U-46   |HL Touring Frame - Blue, 46  |891|FR-T98U-50   |HL Touring Frame - Blue, 50  |892|FR-T98U-54   |HL Touring Frame - Blue, 54  |893|FR-T98U-60   |HL Touring Frame - Blue, 60  |887|FR-T98Y-46   |HL Touring Frame - Yellow, 46|888|FR-T98Y-50   |HL Touring Frame - Yellow, 50|889|FR-T98Y-54   |HL Touring Frame - Yellow, 54|885|FR-T98Y-60   |HL Touring Frame - Yellow, 60|947|HB-T928      |HL Touring Handlebars        |916|SE-T924      |HL Touring Seat/Saddle       |903|FR-T67U-44   |LL Touring Frame - Blue, 44  |895|FR-T67U-50   |LL Touring Frame - Blue, 50  |896|FR-T67U-54   |LL Touring Frame - Blue, 54  |897|FR-T67U-58   |LL Touring Frame - Blue, 58  |...
 
5. Write a query in SQL to return all rows from the salesorderheader table in Adventureworks database and calculate the percentage of tax on the subtotal have decided. Return salesorderid, customerid, orderdate, subtotal, percentage of tax column. Arranged the result set in ascending order on subtotal.
Sample Output:

*/
SELECT SalesOrderID, CustomerID, OrderDate, SubTotal,(TaxAmt*100)/SubTotal AS Tax_Percent FROM Sales.SalesOrderHeader ORDER BY SubTotal DESC

/*


salesorderid|customerid|orderdate              |subtotal   |tax_percent        |------------+----------+-----------------------+-----------+-------------------+51131|     29641|2013-05-30 00:00:00.000|163930.3943|10.9488656308319512|55282|     29641|2013-08-30 00:00:00.000|160378.3913|10.2805612815745958|46616|     29614|2012-05-30 00:00:00.000|150837.4387| 9.9382830477616695|46981|     30103|2012-06-30 00:00:00.000|147390.9328| 9.8971768635146327|47395|     29701|2012-07-31 00:00:00.000|146154.5653| 9.8391246078989227|47369|     29998|2012-07-31 00:00:00.000|140078.3959| 9.7785509407021986|47355|     29957|2012-07-31 00:00:00.000| 129261.254| 9.7141627606366870|51822|     29913|2013-06-30 00:00:00.000|128873.2206| 9.8028539530422816|44518|     29624|2011-10-01 00:00:00.000|126198.3362| 9.7285313496866847|57150|     29923|2013-09-30 00:00:00.000| 122285.724| 9.6171868762047809|51858|     29940|2013-06-30 00:00:00.000|122284.4578|11.0640782511610400|43875|     29624|2011-07-01 00:00:00.000|121761.9396| 9.7497652706576957|46607|     29994|2012-05-30 00:00:00.000| 120182.185| 9.7784823932099421|46660|     29646|2012-05-30 00:00:00.000|117274.3453|10.0397911153378232|..
 
6. Write a query in SQL to create a list of unique jobtitles in the employee table in Adventureworks database. Return jobtitle column and arranged the resultset in ascending order.
Sample Output:

*/

SElECT DISTINCT JobTitle FROM HumanResources.Employee ORDER BY JobTitle

/*


jobtitle                                |----------------------------------------+Accountant                              |Accounts Manager                        |Accounts Payable Specialist             |Accounts Receivable Specialist          |Application Specialist                  |Assistant to the Chief Financial Officer|Benefits Specialist                     |Buyer                                   |Chief Executive Officer                 |Chief Financial Officer                 |Control Specialist                      |Database Administrator                  |Design Engineer                         |Document Control Assistant              |...
 
7. Write a query in SQL to calculate the total freight paid by each customer. Return customerid and total freight. Sort the output in ascending order on customerid.
Sample Output:


*/
SELECT CustomerID, sum(Freight) as Total_Freight FROM Sales.SalesOrderHeader GROUP BY CustomerID ORDER BY CustomerID ASC

/*

customerid|total_freight|----------+-------------+11000|     206.2249|11001|     159.5971|11002|     202.8511|11003|     203.4823|11004|     204.9003|11005|     203.0334|11006|     202.9759|11007|     205.2751|11008|     202.6578|11009|     202.2833|11010|     202.2011|11011|     203.3261|11012|       2.0315|11013|       2.8490|11014|       3.4613|11015|      62.5243|...
 
8. Write a query in SQL to find the average and the sum of the subtotal for every customer. Return customerid, average and sum of the subtotal. Grouped the result on customerid and salespersonid. Sort the result on customerid column in descending order.
Sample Output:


*/
SELECT CustomerID, SalesPersonID, AVG(SubTotal) AS AvgTotal, SUM(SubTotal) AS Sum_Total FROM Sales.SalesOrderHeader GROUP BY CustomerID, SalesPersonID ORDER BY CustomerID DESC

/*

customerid|salespersonid|avg_subtotal          |sum_subtotal|----------+-------------+----------------------+------------+30118|          275|    34638.152183333333| 207828.9131|30118|          277|    35369.828450000000|  70739.6569|30117|          275|    77171.792833333333| 463030.7570|30117|          277|    58954.136550000000| 353724.8193|30116|          276|    46778.550275000000| 187114.2011|30115|          289| 1114.6949250000000000|   8917.5594|30114|          290| 1456.6238875000000000|  11652.9911|30113|          282|    34148.236350000000| 273185.8908|30112|          280|    93591.621700000000|  93591.6217|30112|          284|    54909.378542857143| 384365.6498|30111|          277|    69131.600775000000| 276526.4031|30110|          276|  406.3188750000000000|   1625.2755|30109|          275|    59857.260500000000|  119714.521|30109|          277|    36114.523283333333| 216687.1397|30108|          289|    36150.645400000000| 144602.5816|...
 
9. Write a query in SQL to retrieve total quantity of each productid which are in shelf of 'A' or 'C' or 'H'. Filter the results for sum quantity is more than 500. Return productid and sum of the quantity. Sort the results according to the productid in ascending order.
Sample Output:


*/
SELECT ProductID, sum(Quantity) AS Total_Quantity FROM Production.ProductInventory WHERE Shelf IN ('A','C','H') GROUP BY ProductID HAVING SUM(Quantity) > 500 ORDER BY productid

/*



productid|total_quantity|---------+--------------+1|           761|2|           791|3|           909|4|           900|316|           532|317|           593|319|           797|320|          1136|321|          1750|322|          1684|323|          1684|324|          1629|325|          1210|326|          1097|328|          1044|329|          1025|330|          1005|331|           831|...
 
10. Write a query in SQL to find the total quantity for a group of locationid multiplied by 10.
Sample Output:

*/
SELECT SUM(Quantity) AS Total_Quantity FROM Production.ProductInventory GROUP BY (LocationID *10) 


/*


total_quantity|--------------+186|20295|110|83173|17319|5549|72899|958|13584|332|95477|5165|20419|508|
 
11. Write a query in SQL to find the persons whose last name starts with letter 'L'. Return BusinessEntityID, FirstName, LastName, and PhoneNumber. Sort the result on lastname and firstname.
Sample Output:


*/

SELECT P.BusinessEntityID, FirstName, LastName, PhoneNumber AS Person_Phone FROM Person.Person AS P JOIN Person.PersonPhone AS PH ON P.BusinessEntityID  = PH.BusinessEntityID  WHERE LastName %STARTSWITH 'L' ORDER BY LastName, FirstName;



/*

businessentityid|firstname  |lastname       |person_phone       |----------------+-----------+---------------+-------------------+5527|Aaron      |Lal            |605-555-0159       |5268|Adam       |Lal            |513-555-0110       |12539|Alejandro  |Lal            |1 (11) 500 555-0117|19786|Alicia     |Lal            |1 (11) 500 555-0161|12004|Alisha     |Lal            |1 (11) 500 555-0119|16649|Alison     |Lal            |1 (11) 500 555-0177|5005|Alvin      |Lal            |1 (11) 500 555-0168|5070|Andres     |Lal            |1 (11) 500 555-0127|10416|Arturo     |Lal            |638-555-0164       |8951|Ashlee     |Lal            |1 (11) 500 555-0148|6283|Austin     |Lal            |541-555-0141       |11600|Barbara    |Lal            |1 (11) 500 555-0176|6744|Benjamin   |Lal            |1 (11) 500 555-0148|17275|Bethany    |Lal            |1 (11) 500 555-0196|3694|Bonnie     |Lal            |1 (11) 500 555-0191|9390|Brad       |Lal            |463-555-0111       |20292|Bradley    |Lal            |1 (11) 500 555-0124|...
 
12. Write a query in SQL to find the sum of subtotal column. Group the sum on distinct salespersonid and customerid. Rolls up the results into subtotal and running total. Return salespersonid, customerid and sum of subtotal column i.e. sum_subtotal.
Sample Output:


*/

SELECT SalesPersonID, CustomerID, SUM(SubTotal) AS SUM_Total FROM Sales.SalesOrderHeader GROUP BY ROLLUP (CustomerID)


/*


salespersonid|customerid|sum_subtotal  |-------------+----------+--------------+274|     29491|    33406.7043|274|     29493|      2146.962|274|     29514|     3405.1668|274|     29523|    34349.2656|274|     29576|        53.994|274|     29579|      35331.66|274|     29604|       647.994|274|     29605|    29482.0603|274|     29616|   138046.3212|274|     29617|   198993.3507|274|     29623|      1946.022|274|     29650|        83.988|274|     29666|    15842.6141|274|     29669|     3962.2441|274|     29671|     11802.564|274|     29675|       4254.45|...
 
13. Write a query in SQL to find the sum of the quantity of all combination of group of distinct locationid and shelf column. Return locationid, shelf and sum of quantity as TotalQuantity.
Sample Output:


*/

SELECT LocationID, Shelf, SUM(Quantity) AS TotalQuantity FROM Production.ProductInventory GROUP BY CUBE (LocationID, Shelf)

/*





locationid|shelf|totalquantity|----------+-----+-------------+|     |       335974|50|J    |         3321|6|A    |         2734|50|B    |         3591|5|A    |         6572|45|N/A  |          332|60|K    |          107|10|D    |         1727|60|G    |         1050|60|A    |         1116|20|B    |          355|50|S    |         1333|50|K    |         8881|1|G    |         3954|6|K    |          164|20|A    |         1680|10|C    |         3464|...
 
14. Write a query in SQL to find the sum of the quantity with subtotal for each locationid. Group the results for all combination of distinct locationid and shelf column. Rolls up the results into subtotal and running total. Return locationid, shelf and sum of quantity as TotalQuantity.
Sample Output:

*/
SELECT LocationID, Shelf, SUM(Quantity) AS TotalQuantity, ModifiedDate FROM Production.ProductInventory GROUP BY GROUPING SETS ( ROLLUP (LocationID, Shelf), CUBE (LocationID, Shelf), (ModifiedDate) )

/*


locationid|shelf|totalquantity|----------+-----+-------------+|     |       335974||     |       335974|50|J    |         3321|6|A    |         2734|50|B    |         3591|5|A    |          6572|45|N/A  |          332|60|K    |          107|10|D    |         1727|60|G    |         1050|60|A    |         1116|20|B    |          355|50|S    |         1333|50|K    |         8881|1|G    |         3954|6|K    |          164|20|A    |         1680|...
 
15. Write a query in SQL to find the total quantity for each locationid and calculate the grand-total for all locations. Return locationid and total quantity. Group the results on locationid.
Sample Output:

*/
SELECT LocationID, SUM(Quantity) AS TotalQuantity FROM Production.ProductInventory GROUP BY LocationID

/*


locationid|totalquantity|----------+-------------+|       335974|4|          110|30|          958|50|        95477|40|          508|60|        20419|3|          186|20|         5165|7|        17319|10|        13584|1|        72899|45|          332|5|        20295|2|         5549|6|        83173|...
 
16. Write a query in SQL to retrieve the number of employees for each City. Return city and number of employees. Sort the result in ascending order on city.
Sample Output:

*/
SELECT Pa.City, COUNT(Bi.AddressID) NoOfEmployees FROM Person.BusinessEntityAddress AS Bi INNER JOIN Person.Address AS Pa ON Bi.AddressID = Pa.AddressID GROUP BY Pa.City ORDER BY Pa.City

/*


city                 |noofemployees|---------------------+-------------+Abingdon             |            1|Albany               |            4|Alexandria           |            2|Alhambra             |            1|Alpine               |            1|Altadena             |            2|Altamonte Springs    |            1|Anacortes            |            3|Arlington            |            1|Ascheim              |            1|Atlanta              |            2|Auburn               |            1|Augsburg             |            2|Augusta              |            1|Aujan Mournede       |            1|Aurora               |            1|Austell              |            1|...
 
17. Write a query in SQL to retrieve the total sales for each year. Return the year part of order date and total due amount. Sort the result in ascending order on year part of order date.
Sample Output:
*/

SELECT DATEPART(YEAR,OrderDate) AS "Year",SUM(TotalDue) AS "Order Amount" FROM Sales.SalesOrderHeader GROUP BY DATEPART(YEAR,OrderDate) ORDER BY DATEPART(YEAR,OrderDate)

/*



Year  |Order Amount |------+-------------+2011.0|14155699.5250|2012.0|37675700.3120|2013.0|48965887.9632|2014.0|22419498.3157|
 
18. Write a query in SQL to retrieve the total sales for each year. Filter the result set for those orders where order year is on or before 2016. Return the year part of orderdate and total due amount. Sort the result in ascending order on year part of order date.
Sample Output:


*/

SELECT DATEPART(YEAR,OrderDate) AS YearOfOrderDate, SUM(TotalDue) AS TotalDueOrder FROM Sales.SalesOrderHeader GROUP BY DATEPART(YEAR,OrderDate) HAVING DATEPART(YEAR,OrderDate) <= '2016' ORDER BY DATEPART(YEAR,OrderDate);
/*

yearoforderdate|totaldueorder|---------------+-------------+2011.0|14155699.5250|2012.0|37675700.3120|2013.0|48965887.9632|2014.0|22419498.3157|
 
19. Write a query in SQL to find the contacts who are designated as a manager in various departments. Returns ContactTypeID, name. Sort the result set in descending order.
Sample Output:

*/
SELECT ContactTypeID, Name FROM Person.ContactType WHERE Name LIKE '%Manager%' ORDER BY ContactTypeID DESC
/*


contacttypeid|name                           |-------------+-------------------------------+19|Sales Manager                  |15|Purchasing Manager             |13|Product Manager                |8|Marketing Manager              |6|International Marketing Manager|1|Accounting Manager             |	
 
20. From the following tables write a query in SQL to make a list of contacts who are designated as 'Purchasing Manager'. Return BusinessEntityID, LastName, and FirstName columns. Sort the result set in ascending order of LastName, and FirstName.
Sample Output:


*/

SELECT Pp.BusinessEntityID, LastName, FirstName FROM Person.BusinessEntityContact AS Pb INNER JOIN Person.ContactType AS Pc ON Pc.ContactTypeID = Pb.ContactTypeID INNER JOIN Person.Person AS PP ON pp.BusinessEntityID = Pb.PersonID WHERE Pc.Name = 'Purchasing Manager' ORDER BY LastName, FirstName;
/*

businessentityid|lastname      |firstname  |----------------+--------------+-----------+1149|Alexander     |Mary       |363|Arakawa       |Hannah     |365|Arbelaez      |Kyley      |377|Ault          |John       |379|Avalos        |Robert     |389|Bailey        |James      |391|Baldwin       |Douglas    |399|Banks         |Darrell    |401|Barbariol     |Angela     |403|Barber        |David      |409|Barlow        |Brenda     |411|Barnhill      |Josh       |413|Barr          |Adam       |423|Bauer         |Ciro       |425|Beanston      |Glenna     |427|Beasley       |Shaun      |447|Ben-Sachar    |Ido        |...			 	
 
21. Write a query in SQL to retrieve the salesperson for each PostalCode who belongs to a territory and SalesYTD is not zero. Return row numbers of each group of PostalCode, last name, salesytd, postalcode column. Sort the salesytd of each postalcode group in descending order. Shorts the postalcode in ascending order.
Sample Output:
*/

SELECT ROW_NUMBER() OVER win AS "Row Number", Pp.LastName, Sp.SalesYTD, Pa.PostalCode FROM Sales.SalesPerson AS Sp INNER JOIN Person.Person AS Pp ON Sp.BusinessEntityID = Pp.BusinessEntityID INNER JOIN Person.Address AS Pa ON pa.AddressID = pp.BusinessEntityID WHERE TerritoryID IS NOT NULL AND SalesYTD <> 0 WINDOW win AS (PARTITION BY PostalCode ORDER BY SalesYTD DESC) ORDER BY PostalCode;
/*



Row Number|lastname         |salesytd    |postalcode|----------+-----------------+------------+----------+1|Mitchell         |4251368.5497|98027     |2|Blythe           |3763178.1787|98027     |3|Carson           |3189418.3662|98027     |4|Reiter           | 2315185.611|98027     |5|Vargas           |1453719.4653|98027     |6|Ansman-Wolfe     |1352577.1325|98027     |1|Pak              |4116871.2277|98055     |2|Varkey Chudukatil|3121616.3202|98055     |3|Saraiva          |2604540.7172|98055     |4|Ito              |2458535.6169|98055     |5|Valdez           |1827066.7118|98055     |6|Mensa-Annan      |1576562.1966|98055     |7|Campbell         |1573012.9383|98055     |8|Tsoflias         |1421810.9242|98055     |
 
22. Write a query in SQL to count the number of contacts for combination of each type and name. Filter the output for those who have 100 or more contacts. Return ContactTypeID and ContactTypeName and BusinessEntityContact. Sort the result set in descending order on number of contacts.
Sample Output:

*/
SELECT Pc.ContactTypeID, Pc.Name AS ContactTypeName, COUNT(*) AS NoContacts FROM Person.BusinessEntityContact AS Pbc INNER JOIN Person.ContactType AS Pc ON Pc.ContactTypeID = Pbc.ContactTypeID GROUP BY Pc.ContactTypeID, Pc.Name HAVING COUNT(*) >= 100 ORDER BY COUNT(*) DESC;
/*


contacttypeid|ctypename         |nocontacts|-------------+------------------+----------+11|Owner             |       266|15|Purchasing Manager|       245|14|Purchasing Agent  |       242|
 
23. Write a query in SQL to retrieve the RateChangeDate, full name (first name, middle name and last name) and weekly salary (40 hours in a week) of employees. In the output the RateChangeDate should appears in date format. Sort the output in ascending order on NameInFull.
Sample Output:

*/

SELECT CAST(Hep.RateChangeDate AS DATE) AS FromDate,CONCAT(LastName, ', ', FirstName, ' ', MiddleName) AS NameInFull, (40 * Hep.Rate) AS SalaryInAWeek FROM Person.Person AS Pp INNER JOIN HumanResources.EmployeePayHistory AS Hep ON Hep.BusinessEntityID = Pp.BusinessEntityID ORDER BY NameInFull;


/*


fromdate  |nameinfull                     |salaryinaweek|----------+-------------------------------+-------------+2013-03-14|Abbas, Syed E                  |     1924.040|2010-01-16|Abercrombie, Kim B             |       498.00|2009-02-28|Abolrous, Hazem E              |    1153.8480|2009-01-02|Ackerman, Pilar G              |     769.2320|2009-03-05|Adams, Jay G                   |       498.00|2009-01-17|Ajenstat, François P           |    1538.4600|2012-04-16|Alberts, Amy E                 |     1924.040|2008-12-02|Alderson, Greg F               |          400|2008-12-28|Alexander, Sean P              |     423.0760|2009-12-02|Altman, Gary E.                |     961.5400|2009-01-02|Anderson, Nancy A              |       498.00|2011-05-31|Ansman-Wolfe, Pamela O         |     923.0760|2009-01-04|Arifin, Zainal T               |     711.5400|2009-01-11|Bacon, Dan K                   |    1096.1520|2009-01-21|Baker, Bryan                   |       498.00|2009-12-25|Baker, Mary R                  |       538.00|2009-01-20|Barbariol, Angela W            |          440|...	
 
24. Write a query in SQL to calculate and display the latest weekly salary of each employee. Return RateChangeDate, full name (first name, middle name and last name) and weekly salary (40 hours in a week) of employees Sort the output in ascending order on NameInFull.
Sample Output:

*/

SELECT CAST(Hep.RateChangeDate AS DATE) AS FromDate,CONCAT(FirstName, ', ', MiddleName, ' ', LastName) AS FullName,(40 * Hep.Rate) AS SalaryInAWeek FROM Person.Person AS Pp INNER JOIN HumanResources.EmployeePayHistory AS Hep ON Hep.BusinessEntityID = Pp.BusinessEntityID WHERE Hep.RateChangeDate = (SELECT MAX(RateChangeDate) FROM HumanResources.EmployeePayHistory WHERE BusinessEntityID = Hep.BusinessEntityID) ORDER BY FullName;
/*


fromdate  |nameinfull                     |salaryinaweek|----------+-------------------------------+-------------+2013-03-14|Abbas, Syed E                  |     1924.040|2010-01-16|Abercrombie, Kim B             |       498.00|2009-02-28|Abolrous, Hazem E              |    1153.8480|2009-01-02|Ackerman, Pilar G              |     769.2320|2009-03-05|Adams, Jay G                   |       498.00|2009-01-17|Ajenstat, François P           |    1538.4600|2012-04-16|Alberts, Amy E                 |     1924.040|2008-12-02|Alderson, Greg F               |          400|2008-12-28|Alexander, Sean P              |     423.0760|2009-12-02|Altman, Gary E.                |     961.5400|2009-01-02|Anderson, Nancy A              |       498.00|2011-05-31|Ansman-Wolfe, Pamela O         |     923.0760|2009-01-04|Arifin, Zainal T               |     711.5400|2009-01-11|Bacon, Dan K                   |    1096.1520|2009-01-21|Baker, Bryan                   |       498.00|2009-12-25|Baker, Mary R                  |       538.00|2009-01-20|Barbariol, Angela W            |          440|...
 
25. Write a query in SQL to find the sum, average, count, minimum, and maximum order quentity for those orders whose id are 43659 and 43664. Return SalesOrderID, ProductID, OrderQty, sum, average, count, max, and min order quantity.
Sample Output:


*/

SELECT SalesOrderID, ProductID, OrderQty, 
SUM(OrderQty) OVER (PARTITION BY SalesOrderID) AS "TotalQuantity",
AVG(Floor(OrderQty)) OVER (PARTITION BY SalesOrderID) AS "AvgQuantity",
COUNT(OrderQty) OVER (PARTITION BY SalesOrderID) AS "NoOfOrders",
MIN(OrderQty) OVER (PARTITION BY SalesOrderID) AS "MinQuantity",
MAX(OrderQty) OVER (PARTITION BY SalesOrderID) AS "MaxQuantity"
FROM Sales.SalesOrderDetail WHERE SalesOrderID IN (43659,43664)

/*

salesorderid|productid|orderqty|Total Quantity|Avg Quantity      |No of Orders|Min Quantity|Max Quantity|------------+---------+--------+--------------+------------------+------------+------------+------------+43659|      776|       1|            26|2.1666666666666667|          12|           1|           6|43659|      777|       3|            26|2.1666666666666667|          12|           1|           6|43659|      778|       1|            26|2.1666666666666667|          12|           1|           6|43659|      771|       1|            26|2.1666666666666667|          12|           1|           6|43659|      772|       1|            26|2.1666666666666667|          12|           1|           6|43659|      773|       2|            26|2.1666666666666667|          12|           1|           6|43659|      774|       1|            26|2.1666666666666667|          12|           1|           6|43659|      714|       3|            26|2.1666666666666667|          12|           1|           6|43659|      716|       1|            26|2.1666666666666667|          12|           1|           6|43659|      709|       6|            26|2.1666666666666667|          12|           1|           6|43659|      712|       2|            26|2.1666666666666667|          12|           1|           6|43659|      711|       4|            26|2.1666666666666667|          12|           1|           6|43664|      772|       1|            14|1.7500000000000000|           8|           1|           4|43664|      775|       4|            14|1.7500000000000000|           8|           1|           4|...
 




*/