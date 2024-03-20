USE AutomatedDatabase
go


IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'SalesOrderHeader')
-- Create UserInfo table with additional columns
CREATE TABLE [SalesOrderHeader](
    [SalesOrderID] [int],
    [OrderDate] [datetime],
    [PurchaseOrderNumber] [nvarchar](25) NULL,
    [CustomerID] [int],
    [SalesPersonID] [int] NULL,
 CONSTRAINT [PK_SalesOrderHeader_SalesOrderID] PRIMARY KEY CLUSTERED 
([SalesOrderID] ASC) ON [PRIMARY]);
GO

CREATE TABLE [SalesOrderDetail](
	[SalesOrderID] [int] NOT NULL,
	[SalesOrderDetailID] [int],
	[OrderQty] [smallint] NOT NULL,
	[ProductID] [int] NOT NULL,
	[UnitPrice] [money] NOT NULL,
    [UnitPriceDiscount] [money] NOT NULL,
	[LineTotal]  AS (isnull(([UnitPrice]*((1.0)-[UnitPriceDiscount]))*[OrderQty],(0.0))),	
 CONSTRAINT [PK_SalesOrderDetail_SalesOrderID_SalesOrderDetailID] PRIMARY KEY CLUSTERED 
([SalesOrderID] ASC,[SalesOrderDetailID] ASC) ON [PRIMARY]);
GO

-- Insert data into UserInfo table with new columns
INSERT INTO SalesOrderHeader ( SalesOrderID, OrderDate, PurchaseOrderNumber, CustomerID, SalesPersonID)
VALUES 
(43659, '2011-05-31 00:00:00.000','PO522145787', 29825, 279),
(43660, '2011-05-31 00:00:00.000','PO18850127500', 29672, 279),
(43661, '2011-05-31 00:00:00.000','PO18473189620', 29734, 282),
(43662, '2011-05-31 00:00:00.000','PO18444174044', 29994, 282),
(43663, '2011-05-31 00:00:00.000','PO18009186470', 29565, 276),
(43664, '2011-05-31 00:00:00.000','PO16617121983', 29898, 280),
(43665, '2011-05-31 00:00:00.000','PO16588191572', 29580, 283),
(43666, '2011-05-31 00:00:00.000','PO16008173883', 30052, 276),
(43667, '2011-05-31 00:00:00.000','PO15428132599', 29974, 277),
(43668, '2011-05-31 00:00:00.000','PO14732180295', 29614, 282);
GO

INSERT INTO SalesOrderDetail
    (SalesOrderID, SalesOrderDetailID, OrderQty, ProductID, UnitPrice, UnitPriceDiscount)
VALUES
    (43659, 1, 1, 776, 2024.994, 0.00),
    (43659, 2, 3, 777, 2024.994, 0.00),
    (43659, 3, 1, 778, 2024.994, 0.00),
    (43659, 4, 1, 771, 2039.994, 0.00),
    (43659, 5, 1, 772, 2039.994, 0.00),
    (43659, 6, 2, 773, 2039.994, 0.00),
    (43659, 7, 1, 774, 2039.994, 0.00),
    (43659, 8, 3, 714, 28.8404, 0.00),
    (43659, 9, 1, 716, 28.8404, 0.00),
    (43659, 10, 6, 709, 5.70, 0.00);
Go