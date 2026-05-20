USE Financiera;

SELECT MIN(plazos) AS minPlazos, AVG(plazos * 1.0) AS promPlazos, MAX(plazos) as maxPlazos, COUNT(plazos) totalPlazos FROM dbo.ventas;