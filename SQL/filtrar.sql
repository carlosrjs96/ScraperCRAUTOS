CREATE PROCEDURE [dbo].[filtrarPublicacion](@Nombre varchar(50),
                                           @Apellido varchar(50),
                                           @Anno varchar(4),
                                           @Kilometros int,
                                           @Tipo varchar(50),
                                           @Transmision varchar(50),
                                           @Combustible varchar(50),
                                           @Localizacion varchar(200),
                                           @Marca varchar(50),
                                           @Modelo varchar(50),
                                           @Precio float,
                                           @Motor varchar(50),
                                           @Estilo varchar(50),
                                           @Asientos int,
                                           @Chasis varchar(50),
                                           @NombrePagina varchar(50),
                                           @FechaPublicacion datetime,
                                           @FechaScraping datetime,
                                           @UrlPublicacion varchar(250))
AS
BEGIN

SELECT * FROM AUTO A INNER JOIN VENDEDOR V
ON A.IdVendedor = V.IdVendedor AND
   CAST(A.Anno AS int) >= '2001' AND
   CAST(A.Anno AS int) <= '2015' AND
   A.Kilometros = '1500000' AND
   A.Tipo = 'bmo' AND
   A.Transmision = 'Manual' AND
   A.Combustible = 'Gasolina' AND
   A.Localizacion= 'Heredia' AND
   A.Marca= 'BMW' AND
   A.Precio >= 1000000 AND
   A.Precio <= 15000000 AND
   A.Motor= '1600' AND
   A.Estilo= 'bmo'AND
   A.Asientos= '5'AND
   A.Chasis= '5'

END