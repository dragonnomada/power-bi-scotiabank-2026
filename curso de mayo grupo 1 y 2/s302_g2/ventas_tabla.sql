CREATE TABLE dbo.ventas (
	folio INT NOT NULL,
	tipo NVARCHAR(20) NOT NULL,
	plazos INT NOT NULL,
	precio DECIMAL(20, 2) NOT NULL,
	anticipo DECIMAL(20, 2) NOT NULL,
	interes DECIMAL(20, 2) NOT NULL,
	subtotal DECIMAL(20, 2) NOT NULL,
	total DECIMAL(20, 2) NOT NULL,
	semanal DECIMAL(20, 2) NOT NULL,
	vendedorFolio INT NOT NULL,
	sucursalFolio INT NOT NULL
);