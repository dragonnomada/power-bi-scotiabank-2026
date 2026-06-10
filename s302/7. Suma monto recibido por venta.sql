SELECT folio, SUM(monto) AS [Suma Monto Recibido] FROM dbo.pagos
	GROUP BY folio
	ORDER BY folio DESC