SELECT [plan], SUM(precio) AS [Suma Precio], SUM(total) AS [Suma Total] FROM dbo.ventas
	GROUP BY [plan]