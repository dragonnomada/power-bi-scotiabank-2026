USE Financiera;

INSERT INTO dbo.ventas (
	folio,
	tipo,
	plazos,
	precio,
	anticipo,
	interes,
	subtotal,
	total,
	semanal,
	vendedorFolio,
	sucursalFolio
) VALUES (
	2,
	'renovacion',
	43,
	8999,
	999,
	150,
	12000,
	12999,
	279.07,
	1,
	1
);