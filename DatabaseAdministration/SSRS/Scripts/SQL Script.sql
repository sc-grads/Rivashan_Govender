SELECT  
    YEAR(soh.OrderDate) AS SalesYear,
    DATENAME(MONTH, soh.OrderDate) AS SalesMonth,
    SUM(sod.LineTotal) AS TotalSalesRevenue
FROM 
    Sales.SalesOrderDetail AS sod
JOIN 
    Sales.SalesOrderHeader AS soh ON sod.SalesOrderID = soh.SalesOrderID
GROUP BY 
    YEAR(soh.OrderDate),
    DATENAME(MONTH, soh.OrderDate)
ORDER BY 
    SalesYear;